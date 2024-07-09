from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request: HttpRequest):

    return render(request, "books/home.html")



def contact_us(request: HttpRequest):

    return render(request, 'books/contact_us.html')