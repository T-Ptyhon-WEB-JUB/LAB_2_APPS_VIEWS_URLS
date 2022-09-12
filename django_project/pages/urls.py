# pages/urls.py
from django.urls import path
from .views import homePageView,homePage

urlpatterns = [
    path("home/", homePageView, name="home"),
     path("", homePage, name="home"),
]