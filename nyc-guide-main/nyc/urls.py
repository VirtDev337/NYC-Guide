from django.urls import path

from nyc import views

urlpatterns = [
    # all the urls are for free
    path('', views.city, name='city'),
    path('<str:borough>', views.borough, name='borough'),
    path('<str:borough>/<str:activity>', views.activity, name='activity'),
    path('<str:borough>/<str:activity>/<str:venue>', views.venue, name='venue')
]