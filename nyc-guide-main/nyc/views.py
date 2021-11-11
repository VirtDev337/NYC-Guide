from django.shortcuts import render
from .boroughs import boroughs

# Home Screen
def city(request):
    if request.method == 'GET':
        return render(request=request, template_name = 'city.html', context = { 'boroughs': boroughs.keys() })

def borough(request, borough):
    if request.method == 'GET':
        return render(request = request, template_name = 'borough.html', context = { 'borough': borough, 'activities': boroughs[borough].keys() })

def activity(request, borough, activity):
    if request.method == 'GET':
        cards = {}
        places = boroughs[borough][activity].keys()
        for itm in places:
            cards[itm] = boroughs[borough][activity][itm]['image']
        print(cards)
        return render(request = request, template_name = 'activity.html', context = { 'borough': borough, 'activity': activity, 'places' : boroughs[borough][activity].keys(), 'cards' : cards })

def venue(request, borough, activity, venue):
    if request.method == 'GET':
        return render(request = request, template_name = 'venue.html', context={ 'borough': borough, 'activity': activity, 'place' : venue, 'venue' : boroughs[borough][activity][venue] })

def about(request):
    return render(request, 'about.html')
