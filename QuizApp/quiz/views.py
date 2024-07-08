from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse

def start_view(request: HttpRequest):
  return render(request, "quiz/start.html")

def question_view(request: HttpRequest):
  return

def answer_view(request: HttpRequest):
  return