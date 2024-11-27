from dinner.views import *
from django.urls import path
urlpatterns=[
    path('chapati/',chapati,name='chapati'),
    path('upma/',upma,name='upma'),
]