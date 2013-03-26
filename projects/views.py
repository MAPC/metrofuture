from django.http import HttpResponse
from django.utils import simplejson

from django.contrib.gis.db.models import Union

from projects.models import Project, Municipality, Subregion, Strategy, SubStrategy, SubGoal, Goal


def get_filters(request):
    """
    Returns a JSON object with lists of all available filters.
    """
    municipalities = Municipality.objects.filter(projects__active=True).distinct()
    subregions = Subregion.objects.filter(municipality__in=municipalities)
    substrategies = SubStrategy.objects.filter(project__active=True).distinct()
    strategies = Strategy.objects.filter(substrategy__in=substrategies)
    subgoals = SubGoal.objects.filter(project__active=True).distinct()
    goals = Goal.objects.filter(subgoal__in=subgoals)

    response = {
        'municipalities' : {},
        'subregions': {},
        'strategies': {},
        'substrategies': {},
        'subgoals': {},
        'goals': {},
        'status': {},
    }

    for municipality in municipalities:
        response['municipalities'][municipality.pk] = dict(
            name = municipality.name, 
        )
    for subregion in subregions:
        response['subregions'][subregion.pk] = dict(
            name = subregion.name,
            abbr = subregion.abbr,
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
    for subgoal in subgoals:
        response['subgoals'][subgoal.pk] = dict(
            name = subgoal.title or 'n/a',
            goal = subgoal.goal.id,
        )
    for goal in goals:
        response['goals'][goal.pk] = dict(
            name = goal.title,  
            subgoals = goal.subgoals_string(),
        )
    for k,v in Project.PROJECT_STATUS:
        response['status'][k] = dict(
            name = v
        )

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')

