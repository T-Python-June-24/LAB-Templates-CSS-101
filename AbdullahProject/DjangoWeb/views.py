from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request:HttpResponse):
    return render(request, 'DjangoWeb/home.html')


def learnMore(request:HttpResponse):
    return render(request, 'DjangoWeb/form.html')

def sendMessages(request:HttpResponse):
    return render(request, 'DjangoWeb/contactus.html')