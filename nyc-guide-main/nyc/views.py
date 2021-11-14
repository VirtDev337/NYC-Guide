from django.shortcuts import render
from .boroughs import boroughs

# Home Screen
def city(request):
    if request.method == 'GET':
        return render(request=request, template_name = 'city.html', context = { 'boroughs': boroughs.keys() })

def borough(request, borough):
    if request.method == 'GET':
        # categories = boroughs[borough]["activities"]
        main_borough = boroughs[borough]
        todo = {}
        # for thing in categories:
        #     todo[thing] = f"{thing}.jpeg"
        return render(request = request, template_name = 'borough.html', context = { 'borough': borough, 'main_borough': main_borough, 'activities': boroughs[borough]["activities"], 'categories' : todo  })

def activity(request, borough, activity):
    if request.method == 'GET':
        cards = {}
        # places = boroughs[borough]["activities"][activity]["venues"]

        main_activity = ''
        for _activity in boroughs[borough]["activities"]:
            if _activity['name'] == activity:
                main_activity = _activity

        # print(main_activity)

        places = main_activity["venues"]

        # for itm in places:
        #     cards[itm] = boroughs[borough][activity][itm]['image']
        print(cards)
        return render(request = request, template_name = 'activity.html', context = { 'borough': borough, 'activity': activity, 'places' : places, 'cards' : cards, "main_activity": main_activity})

def venue(request, borough, activity, venue):
    if request.method == 'GET':

        main_activity = ''
        for _activity in boroughs[borough]["activities"]:
            if _activity['name'] == activity:
                main_activity = _activity

        main_venue = ''
        for _venue in main_activity["venues"]:
            if _venue['name'] == venue:
                main_venue = _venue

        return render(request = request, template_name = 'venue.html', context={ 'borough': borough, 'activity': activity, 'place' : main_venue, 'venue' : venue })

def about(request):
    return render(request, 'about.html')
