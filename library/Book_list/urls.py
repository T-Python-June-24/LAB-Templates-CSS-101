from django.urls import path
from . import views

name_app='Book_list'


urlpatterns = [
    path('',views.index , name='home_page'),
]
