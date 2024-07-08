from django.urls import path
from . import views
app_name ="main"
urlpatterns=[
    path('', views.movies_page, name='movies_page'),
    path('FantasticMrFox/',views.FantasticMrFox,name='FantasticMrFox'),
    path('spiritedAway/',views.spiritedAway,name='spiritedAway'),
    path('Coco/',views.Coco,name='Coco'),
    path('It_2017/',views.It_2017,name='It_2017'),
    path('split/',views.split,name='split'),

]