from django.http import HttpResponse
from django.utils import simplejson

from django.contrib.gis.db.models import Union

from models import Project, Municipality, Strategy, Goal, Supergoal


def get_projects(request):
    """
    Returns a JSON object with projects according to query parameters.
    Possible query parameters are: municipality, strategy, goal, supergoal
    """

    kwargs = {
        'active': True,
    }

    # build filter arguments
    # TODO: clean this
    try:
        kwargs['municipalities__muni_id'] = request.GET['municipality']
    except:
        pass
    try:
        kwargs['strategies__nr__contains'] = request.GET['strategy']
    except:
        pass
    try:
        kwargs['goals__nr'] = request.GET['goal']
    except:
        pass
    try:
        kwargs['supergoals__abbr'] = request.GET['supergoal']
    except:
        pass

    projects = Project.objects.filter(**kwargs).select_related()

    response = []

    for project in projects:
        try:
        # get the area covered by project municipalities
        # TODO: pass encoded polygon instead of centroid
        # TODO: data problem, some projects don't have municipalities assigned
            project_area = project.municipalities.aggregate(Union('geometry'))
            project_area_geom = project_area['geometry__union']
            project_area_geom.transform(4326)

            response.append(dict( 
                id=project.id,
                name = project.name, 
                status=project.status, 
                timing=project.timing, 
                lonlat=project_area_geom.centroid.coords,
                municipalities=list(project.municipalities.values_list('name', flat=True)), 
            ))
        except:
             pass
    
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')

def get_filters(request):
    """
    Returns a JSON object with a list of all available filters.
    """
    municipalities = Municipality.objects.filter(project__active=True).distinct()
    strategies = Strategy.objects.filter(project__active=True).distinct()
    goals = Goal.objects.filter(project__active=True).distinct()
    supergoals = Supergoal.objects.filter(project__active=True).distinct()

    response = []

    # TODO: clean that...
    for municipality in municipalities:
        response.append(dict(
            id=municipality.muni_id,
            name=municipality.name,
            type='municipality'  ,  
        ))
    for strategy in strategies:
        response.append(dict(
            id=strategy.nr,
            name=strategy.title,
            type='strategy',  
        ))
    for goal in goals:
        response.append(dict(
            id=goal.nr,
            name=goal.title,
            type='goal',   
        ))
    for supergoal in supergoals:
        response.append(dict(
            id=supergoal.abbr,
            name=supergoal.title,
            type='supergoal',    
        ))

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
