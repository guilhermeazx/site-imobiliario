from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reqquest):
    return HttpResponse ('<h1>das</h1>')