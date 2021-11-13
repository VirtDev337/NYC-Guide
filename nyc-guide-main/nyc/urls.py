from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from nyc import views

urlpatterns = [
    # all the urls are for free
    path('', views.city, name = 'city'),
    path('about', views.about, name = 'about'),
    path('<str:borough>', views.borough, name = 'borough'),
    path('<str:borough>/<str:activity>', views.activity, name = 'activity'),
    path('<str:borough>/<str:activity>/<str:venue>', views.venue, name = 'venue'),
] + static(settings.STATIC_URL)