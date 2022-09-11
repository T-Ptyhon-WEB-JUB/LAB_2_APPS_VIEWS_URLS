from importlib.resources import path
from django.urls import path
from . import views

app_name = "appProject"

urlpatterns = [
    path("home/", views.home_message,name="home_message")
]
