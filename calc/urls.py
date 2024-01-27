from django.urls import path

from . import views
from django.contrib import admin
from vege.views import *


urlpatterns = [
    # path('',views.home,name='home'),
    path('',Receipes,name='rec'),
    path ('about/',views.about,name='about'),
    # path('reciepes/',Receipes,name='rec'),
    path('admin/',admin.site.urls)


]