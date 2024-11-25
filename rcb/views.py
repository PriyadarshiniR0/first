from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(response):
    return HttpResponse('Virat is a captain')
def kohli(response):
    return HttpResponse('<h1>Captain King Kohli Will Lift The Trophy This Year</h1>')

