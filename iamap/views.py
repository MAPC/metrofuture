from django.http import HttpResponse
from django.utils import simplejson

from django.contrib.gis.db.models import Union

from iamap.models import Project, Municipality, Strategy, Goal, Supergoal


def get_filters(request):
    """
    Returns a JSON object with lists of all available filters.
    """
    municipalities = Municipality.objects.filter(projects__isnull=False).distinct()
    strategies = Strategy.objects.filter(project__isnull=False).distinct()
    goals = Goal.objects.filter(project__isnull=False).distinct()
    supergoals = Supergoal.objects.filter(project__isnull=False).distinct()

    response = {
        'municipalities' : [],
        'strategies': [],
        'goals': [],
        'supergoals': [],
    }

    for municipality in municipalities:
        response['municipalities'].append(dict(
            id=municipality.muni_id,
            name=municipality.name, 
        ))
    for strategy in strategies:
        response['strategies'].append(dict(
            id=strategy.id,
            name="%s %s" % (strategy.nr, strategy.title),
        ))
    for goal in goals:
        response['goals'].append(dict(
            id=goal.id,
            name="%s %s" % (goal.nr, goal.title),
        ))
    for supergoal in supergoals:
        response['supergoals'].append(dict(
            id=supergoal.id,
            name=supergoal.title,   
        ))

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
