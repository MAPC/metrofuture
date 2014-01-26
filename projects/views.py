from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import render

from django.contrib.gis.db.models import Union

from projects.models import Project, Municipality, Subregion, Strategy, SubStrategy, SubGoal, Goal

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def active(request):
    projects = Project.objects.filter(active=True)
    return render(request, 'projects.html', {'projects': projects})


def inactive(request):
    projects = Project.objects.filter(active=False)
    return render(request, 'projects.html', {'projects': projects})


def by_municipality(request):
    munis_with_projects = []
    munis = Municipality.objects.order_by('name')
    for muni in munis:
        munis_with_projects.append( { 'name': muni.name, 'projects': muni.projects.all() } )

    return render(request, 'munis.html', { 'mwp': munis_with_projects })


def by_subregion(request):
    subregion_projects = []
    subregions = Subregion.objects.all()

    for subregion in subregions:
        projects = Project.objects.filter(subregions__pk=subregion.pk)
        subregion_projects.append( { 'name': subregion.name, 'projects': projects })

    return render(request, 'munis.html', { 'mwp': subregion_projects })


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

