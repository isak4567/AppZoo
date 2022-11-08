from django.shortcuts import render
from datetime import datetime
#from Appzoologico.models import A
from django.http import HttpResponse
# Create your views here.

def view_zool(request):
    
    return render(request, "index.html")

def form_add_animal(request):

    return render(request, "form_add_animal.html")