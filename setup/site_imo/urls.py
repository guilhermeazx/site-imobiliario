from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name= "index"),
    path("Home",views.index, name= "index"),
    path("contact",views.contact, name= "contact"),
    path("properties",views.properties, name= "properties"),
    path("property",views.property, name= "property-details"),
    path('dashboard', views.dashboard, name="dashboard"),
    
    
]