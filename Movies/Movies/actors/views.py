from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.

def top_actor(request):
    top_actor='Tom'
    return HttpResponse(f'top actor is {top_actor}')