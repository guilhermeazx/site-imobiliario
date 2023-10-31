from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request,'index.html')
def contact(request):
    return render (request,'contact.html')
def properties(request):
    return render (request,'properties.html')
def property(request):
    return render (request,'property-details.html')
def dashboard(request):
    return render (request,'dashboard.html')