from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def cosmic_mysteries(request):
    return render(request, 'core/cosmic_mysteries.html')