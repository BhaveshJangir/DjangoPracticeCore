from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('templet.index')


    peoples = [
        {'name':'Bhavesh Jangir','age':22},
        {'name':'Hitesh Kumar','age':15},
        {'name':'Ramesh Jangir','age':24},
        {'name':'Hitu ','age':10},
        {'name':'Dada Jangir','age':26},
      
    ]
    title = 'Home'
    return render(request,"home/index.html",context = {'peoples':peoples,'title':title})

def about(request):
    title = 'About'
    # return HttpResponse('templet.index')
    return render(request,'home/about.html',context={'title':title})
