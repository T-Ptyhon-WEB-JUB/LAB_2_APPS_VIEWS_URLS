from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# Create your views here.

def home(request):
    home: str = "Tom Cruise"
    return HttpResponse(f"Hello World, This is my new HOME ! {home}")
    