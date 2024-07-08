from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.


def home_views(request:HttpRequest):
    return render(request,"main/home.html")
def mini1_views(request:HttpRequest):
    return render(request,"main/miniP1.html")
def mini2_views(request:HttpRequest):
    return render(request,"main/miniP2.html")
def final_views(request:HttpRequest):
    return render(request,"main/finalProject.html")

