from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_t(request):
    return HttpResponse(f"Hello World, This is my new HOME !")