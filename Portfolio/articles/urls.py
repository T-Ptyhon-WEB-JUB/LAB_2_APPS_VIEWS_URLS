from django.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    path('home/', views.Home, name='home')
]
