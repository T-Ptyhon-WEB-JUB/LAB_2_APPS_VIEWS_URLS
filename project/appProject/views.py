from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_message(request):
    home_message = "HOME"
    return  HttpResponse(f" Hello World, This is my new  {home_message}!")

