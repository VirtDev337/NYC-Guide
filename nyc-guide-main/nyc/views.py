from django.shortcuts import render
from .boroughs import boroughs

# Home Screen
def city(request):
    if request.method == 'GET':
        # borough_img = {
        #     'brooklyn' : "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdm0qx8t0i9gc9.cloudfront.net%2Fthumbnails%2Fvideo%2FEyvF0jkPg%2Fvideoblocks-aerial-view-of-the-brooklyn-bridge-to-manhattan-in-new-york-america-through-the-east-river-in-sunny-day_su4fjfbs_thumbnail-1080_01.png&f=1&nofb=1",
        # }  'images' : borough_img
        return render(request=request, template_name = 'city.html', context = { 'boroughs': boroughs.keys() })

def borough(request, borough):
    if request.method == 'GET':
        categories = boroughs[borough].keys ()
        todo = {}
        for thing in categories:
            todo[thing] = f"{thing}.jpeg"
        return render(request = request, template_name = 'borough.html', context = { 'borough': borough, 'activities': boroughs[borough].keys(), 'categories' : todo  })

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
