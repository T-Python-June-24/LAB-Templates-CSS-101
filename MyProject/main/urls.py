from django.urls import path
from . import views
app_name ="main"
urlpatterns=[
    path('', views.home_page, name='home_page'),
    path('movies/',views.movies_page,name='movies_page'),

]