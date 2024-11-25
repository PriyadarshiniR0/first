from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hardhik(response):
    return HttpResponse('Hardhik is a captain')
def pandya(response):
    return HttpResponse('Pandya')
