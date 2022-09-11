from django.urls import path 
from . import views

app_name= "actors"

urlpatterns= [path("home/",views.home ,name="home")]
