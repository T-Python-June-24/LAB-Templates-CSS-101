from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('messi/', views.messi, name='messi'),
    path('maradona/', views.maradona, name='maradona'),
    path('chi/givara/', views.chi_givara, name='chi_givara'),
    path('wc/history/', views.wc_history, name='wc_history'),
    path('argentina/history/', views.argentina_history, name='argentina_history'),
]