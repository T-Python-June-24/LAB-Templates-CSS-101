from django.shortcuts import render
from django.http import HttpResponse ,HttpRequest


def home_page(request:HttpRequest):
    return render(request,"main/home_page.html")

def movies_page(request:HttpRequest):
    return render(request,"main/movies_page.html")
def FantasticMrFox(request:HttpRequest):
    return render(request,"main/FantasticMrFox.html")

def spiritedAway(request:HttpRequest):
    return render(request,"main/spiritedAway.html")