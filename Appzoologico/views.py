from django.shortcuts import render
from datetime import datetime
#from Appzoologico.models import A
from django.http import HttpResponse
from .models import Animal_GrupoSecundario1, Animal_GrupoSecundario2, Empleado
# Create your views here.

def view_zool(request):

    vertebrados = Animal_GrupoSecundario1.objects.all()
    
    return render(request, "indexZoo.html",  {"vertebrados": vertebrados})

def view_posts(request):
    
    return render(request, "Posts.html")

def view_about(request):
    
    return render(request, "About.html")

def view_contact(request):
    
    return render(request, "Contact.html")

