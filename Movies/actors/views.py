from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def hello(request : HttpRequest):
    hello : str = "tom cruise"
    return HttpResponse(f"Hello World, This is my new HOME ! {hello}")