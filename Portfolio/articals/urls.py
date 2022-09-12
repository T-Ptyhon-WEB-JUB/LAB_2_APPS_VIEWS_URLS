from django.urls import url
from . import views

app_name = 'articals'

urlpatterns = [
    path('home/', views.Home, name='home')
]
