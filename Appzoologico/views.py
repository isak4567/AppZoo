from django.shortcuts import render
from datetime import datetime
#from Appzoologico.models import A
from django.http import HttpResponse
# Create your views here.

def view_zool(request):
    
    return HttpResponse("Hello")