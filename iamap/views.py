from django.http import HttpResponse
from django.utils import simplejson

from django.contrib.gis.db.models import Union

from iamap.models import Project, Municipality, Strategy, Goal, Supergoal, PROJECT_STATUS


def get_filters(request):
    """
    Returns a JSON object with lists of all available filters.
    """
    municipalities = Municipality.objects.filter(projects__active=True).distinct()
    strategies = Strategy.objects.filter(project__active=True).distinct()
    goals = Goal.objects.filter(project__active=True).distinct()
    supergoals = Supergoal.objects.filter(project__active=True).distinct()

    response = {
        'municipalities' : [],
        'strategies': [],
        'goals': [],
        'supergoals': [],
        'status': [],
    }

    for municipality in municipalities:
        response['municipalities'].append(dict(
            id = municipality.muni_id,
            name = municipality.name, 
        ))
    for strategy in strategies:
        response['strategies'].append(dict(
            id = strategy.id,
            name = strategy.title or strategy.nr or 'n/a',
        ))
    for goal in goals:
        response['goals'].append(dict(
            id = goal.nr,
            name = goal.title or 'n/a',
            supergoal = goal.supergoal.id,
        ))
    for supergoal in supergoals:
        response['supergoals'].append(dict(
            id = supergoal.id,
            name = supergoal.title,   
        ))
    for k,v in PROJECT_STATUS:
        response['status'].append(dict(
            id = k,
            name = v,
        ))

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
