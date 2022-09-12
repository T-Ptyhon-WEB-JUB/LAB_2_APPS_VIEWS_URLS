from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def homePage(request):
    return HttpResponse("home/")

  
def homePageView(request):
    return HttpResponse("Hello World, This is my new HOME !")