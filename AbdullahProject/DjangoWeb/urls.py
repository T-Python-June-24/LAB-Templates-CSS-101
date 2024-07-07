from . import views
from django.urls import path



app_name = 'DjangoWeb'

urlpatterns = [
    path('', views.home, name='home'),
    path('learn/', views.learnMore, name='learn'),
    path('contact/', views.sendMessages, name='contact'),
    
]
