from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random
import string

def home(request):

    return render(request, "main/home.html")

def about(request):
  
    return render(request, "main/about.html")

def messi(request):
  
    return render(request, "main/messi.html")

def maradona(request):
  
    return render(request, "main/maradona.html")

def argentina_history(request):
  
    return render(request, "main/argentina_history.html")

def wc_history(request):
  
    return render(request, "main/wc_history.html")

def chi_givara(request):
  
    return render(request, "main/chi_givara.html")
