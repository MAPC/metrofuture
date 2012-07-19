from django.http import HttpResponse
from django.utils import simplejson

from django.contrib.gis.db.models import Union

from iamap.models import Project, Municipality, Subregion, Strategy, SubStrategy, Goal, Supergoal, PROJECT_STATUS


def get_filters(request):
    """
    Returns a JSON object with lists of all available filters.
    """
    municipalities = Municipality.objects.filter(projects__active=True).distinct()
    subregions = Subregion.objects.filter(municipality__projects__active=True).distinct()
    strategies = Strategy.objects.filter(project__active=True).distinct()
    substrategies = SubStrategy.objects.filter(project__active=True).distinct()
    goals = Goal.objects.filter(project__active=True).distinct()
    supergoals = Supergoal.objects.filter(project__active=True).distinct()

    response = {
        'municipalities' : [],
        'subregions': [],
        'strategies': [],
        'substrategies': [],
        'goals': [],
        'supergoals': [],
        'status': [],
    }

    for municipality in municipalities:
        response['municipalities'].append(dict(
            id = municipality.pk,
            name = municipality.name, 
        ))
    for subregion in subregions:
        response['subregions'].append(dict(
            id = subregion.pk,
            name = subregion.name,
            municipalities = subregion.muni_string(),
        ))
    for strategy in strategies:
        response['strategies'].append(dict(
            id = strategy.pk,
            name = strategy.title or strategy.nr or 'n/a',
            substrategies = strategy.substrategies_string(),
        ))
    for substrategy in substrategies:
        response['substrategies'].append(dict(
            id = substrategy.pk,
            name = substrategy.title or strategy.nr or 'n/a',
        ))
    for goal in goals:
        response['goals'].append(dict(
            id = goal.pk,
            name = goal.title or 'n/a',
            supergoal = goal.supergoal.id,
        ))
    for supergoal in supergoals:
        response['supergoals'].append(dict(
            id = supergoal.pk,
            name = supergoal.title,   
        ))
    for k,v in PROJECT_STATUS:
        response['status'].append(dict(
            id = k,
            name = v,
        ))

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')

