from django.urls import path
from . import views
app_name = "quiz"


urlpatterns = [
  path('', views.start_view, name="start_view")
]
