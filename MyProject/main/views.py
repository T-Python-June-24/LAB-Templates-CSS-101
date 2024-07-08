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
def Coco(request:HttpRequest):
    return render(request,"main/Coco.html")
def It_2017(request:HttpRequest):
    return render(request,"main/It_2017.html")

def split(request:HttpRequest):
    return render(request,"main/split.html")