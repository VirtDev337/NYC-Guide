from django.shortcuts import render
from .boroughs import boroughs


def city(request):
    if request.method == 'GET':
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


def borough(request, borough):
    if request.method == 'GET':
        return render(request=request, template_name='borough.html', context={'borough': borough, 'activities': boroughs[borough].keys()})

# Create your views here.


def activity(request, activity):
    if request.method == 'GET':
        return render(request=request, template_name='activity.html', context={'activities': activity, 'venues': boroughs[borough][activity].keys()})


def venue():
    pass
