from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Produto, Vendas, Vendedor
from datetime import datetime
from django.db.models import Sum


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


def retorna_total_vendido(request):
    total = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
    if request.method == "GET":
        return JsonResponse({'total': total})


