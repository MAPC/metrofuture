from django.http import HttpResponse
from django.utils import simplejson

from django.contrib.gis.db.models import Union

from iamap.models import Project, Municipality, Subregion, Strategy, SubStrategy, Goal, Supergoal, PROJECT_STATUS


def get_filters(request):
    """
    Returns a JSON object with lists of all available filters.
    """
    municipalities = Municipality.objects.filter(projects__active=True).distinct()
    subregions = Subregion.objects.filter(municipality__in=municipalities)
    substrategies = SubStrategy.objects.filter(project__active=True).distinct()
    strategies = Strategy.objects.filter(substrategy__in=substrategies)
    goals = Goal.objects.filter(project__active=True).distinct()
    supergoals = Supergoal.objects.filter(goal__in=goals)

    response = {
        'municipalities' : {},
        'subregions': {},
        'strategies': {},
        'substrategies': {},
        'goals': {},
        'supergoals': {},
        'status': {},
    }

    for municipality in municipalities:
        response['municipalities'][municipality.pk] = dict(
            name = municipality.name, 
        )
    for subregion in subregions:
        response['subregions'][subregion.pk] = dict(
            name = subregion.name,
            municipalities = subregion.muni_string(),
        )
    for strategy in strategies:
        response['strategies'][strategy.pk] = dict(
            name = strategy.title or strategy.nr or 'n/a',
            substrategies = strategy.substrategies_string(),
        )
    for substrategy in substrategies:
        response['substrategies'][substrategy.pk] = dict(
            name = substrategy.title or strategy.nr or 'n/a',
        )
    for goal in goals:
        response['goals'][goal.pk] = dict(
            name = goal.title or 'n/a',
            supergoal = goal.supergoal.id,
        )
    for supergoal in supergoals:
        response['supergoals'][supergoal.pk] = dict(
            name = supergoal.title,  
            goals = supergoal.goals_string(),
        )
    for k,v in PROJECT_STATUS:
        response['status'][k] = dict(
            name = v
        )

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')

