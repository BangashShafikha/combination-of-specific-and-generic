from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def chapati(request):
    return HttpResponse('<h1>chapati with egg</h1>')
def upma(request):
    return HttpResponse('<h1>upma with pickle</h1>')
