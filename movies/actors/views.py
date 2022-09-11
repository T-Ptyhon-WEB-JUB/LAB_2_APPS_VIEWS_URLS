from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home(request : HttpResponse):
    home : str = "HOME "
    return HttpResponse(f"Hello World, This is my new {home}")

# Create your views here.
