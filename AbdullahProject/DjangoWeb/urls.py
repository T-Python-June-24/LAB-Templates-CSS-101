from . import views
from django.urls import path



app_name = 'DjangoWeb'

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.learnMore, name='form'),
    path('contact/', views.sendMessages, name='contact'),
    
]
