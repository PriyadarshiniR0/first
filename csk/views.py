from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<h1>dhoni is a captain</h1>')
def ruturaj(request):
    return HttpResponse('<h1>Ruturaj is New Captain of CSK</h1>')
