from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dosa(request):
    return HttpResponse('<h1>dosa with groundnut chutney</h1>')
def pongal(request):
    return HttpResponse(('<h1>pongal with sambar</h1>'))