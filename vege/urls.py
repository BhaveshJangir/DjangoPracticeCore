from django.urls import path

from . import views
from django.contrib import admin
from vege.views import *


urlpatterns = [
   
    path('reciepes/',Receipes,name= 'reciepes'),
    path('delete_receipe/<id>/',delete_receipe,name= 'delete_receipe'),
    path('update_receipe/<id>/',update_receipe,name= 'update_receipe'),
    path('admin/',admin.site.urls)
]




