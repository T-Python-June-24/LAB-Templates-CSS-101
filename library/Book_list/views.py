from django.shortcuts import render
from django.http import HttpRequest
import json
# Create your views here.

def index(Http_RQ:HttpRequest):
    
    with open("./Book_list/static/json/Book.json" ,'r',encoding="UTF-8") as list:
        list.seek(0)
        books=json.load(list)
        
        
    return render(Http_RQ , 'library/books.html' , {'books':books})

def cv(Http_RQ:HttpRequest):
    return render(Http_RQ , 'CV/CV.html')