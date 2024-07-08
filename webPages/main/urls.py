from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('',views.home_views,name="home_views"),
    path('mini1/',views.mini1_views,name="mini1_views"),
    path('mini2/',views.mini2_views,name="mini2_views"),
    path("final/project/",views.final_views,name="final_views")
]
