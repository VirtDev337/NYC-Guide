from django.shortcuts import render
from .boroughs import boroughs

# Function renders Home Screen city.html with 5 boroughs
def city(request):
    if request.method == 'GET':
        return render(request=request, template_name = 'city.html', context = { 'boroughs': boroughs.keys() })
# Function renders activities of specific borough
def borough(request, borough):
    if request.method == 'GET':
        main_borough = boroughs[borough]
        return render(request = request, template_name = 'borough.html', context = { 'borough': borough, 'main_borough': main_borough, 'activities': boroughs[borough]["activities"],})
# Function renders all the venues of a specific activity
def activity(request, borough, activity):
    if request.method == 'GET':
        main_activity = ''
        for _activity in boroughs[borough]["activities"]:
            if _activity['name'] == activity:
                main_activity = _activity
        places = main_activity["venues"]
        return render(request = request, template_name = 'activity.html', context = { 'borough': borough, 'activity': activity, 'places' : places, "main_activity": main_activity})
# Function renders the details of the venue chosen by the user
def venue(request, borough, activity, venue):
    if request.method == 'GET':
        main_activity = ''
        for _activity in boroughs[borough]["activities"]:
            if _activity['name'] == activity:
                main_activity = _activity
            print(main_activity)
        main_venue = ''
        for _venue in main_activity["venues"]:
            if _venue['name'] == venue:
                main_venue = _venue
        bg = f"/static/images/{main_activity['bimage']}"
        return render(request = request, template_name = 'venue.html', context={ 'borough': borough, 'activity': activity, 'place' : main_venue, 'venue' : venue, 'display' : bg })
# Function renders the about page
def about(request):
    return render(request, 'about.html')
