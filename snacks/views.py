from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def panipoori(request):
    return HttpResponse('<h1>favoriate one</h1>')
def bhel(request):
    return HttpResponse('<h1>chatpata snack</h1>')

