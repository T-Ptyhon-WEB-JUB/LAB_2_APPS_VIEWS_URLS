from importlib.resources import path
from django.urls import path
from . import views

app_name = "lab2App"

urlpatterns = [
    path("home/", views.home_t, name="home")
]