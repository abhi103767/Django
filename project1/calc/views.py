from django.shortcuts import render
from django.http import HttpResponse
from .models import Places
# Create your views here.

def home(request):

    if(request.method == 'POST') :
       print(request)
   

   
    
   
