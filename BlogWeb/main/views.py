from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest):
    return render(request, "main/home.html")

def contactUs_view (request: HttpRequest):
    return render(request, "main/contactUs.html")

def logIn_view (request: HttpRequest):
    return render(request, "main/logIn.html")

def singUp_view (request: HttpRequest):
    return render(request, "main/singUp.html")

