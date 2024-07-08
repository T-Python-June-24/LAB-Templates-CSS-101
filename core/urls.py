from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/cosmic_mysteries', views.cosmic_mysteries, name='cosmic_mysteries'),
]