from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home_view(request: HttpRequest):
  return render(request, "main/home.html")