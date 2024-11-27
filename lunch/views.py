from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def biryani(request):
    return HttpResponse(('<h1>biryani with chicken</h1>'))
def dal(request):
    return HttpResponse('<h1>dal with rice</h1>')


# Create your views here.
