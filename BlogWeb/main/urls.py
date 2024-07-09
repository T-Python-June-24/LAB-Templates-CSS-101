from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path("contactUs/", views.contactUs_view,  name= "contactUs_view"),
    path("login/", views.logIn_view,  name= "logIn_view"),
    path("singup/", views.singUp_view,  name= "singUp_view"),
]

