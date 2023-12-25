from django.urls import path

from . import views
from django.contrib import admin
from vege.views import *


urlpatterns = [
   
    path('reciepes/',Receipes,name= 'reciepes'),
    path('admin/',admin.site.urls)
]

