from django.shortcuts import render
from .boroughs import boroughs

def home(request):
    return render(request, 'base.html', context={ 'boroughs': boroughs.keys() })
    
def city(request):
    if request.method == 'GET':
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})

def borough(request, borough):
    if request.method == 'GET':
        return render(request=request, template_name='borough.html', context={'borough': borough, 'activities': boroughs[borough].keys()})

# Create your views here.
def activity(request, borough, activity):
    if request.method == 'GET':
        return render(request=request, template_name='activity.html', context={ 'borough': borough, 'activity': activity, 'places' : boroughs[borough][activity].keys() })

def venue(request, borough, activity, venue):
    if request.method == 'GET':
        return render(request=request, template_name='venue.html', context={ 'borough': borough, 'activity': activity, 'place' : venue, 'venue' : boroughs[borough][activity][venue] })

def about(request):
    return render(request, 'about.html')