from snacks.views import *
from django.urls import path
urlpatterns=[
    path('panipoori/',panipoori,name='panipoori'),
    path('bhel/',bhel,name='bhel'),
]