from django.shortcuts import render,redirect
from vege.models import *

# Create your views here.
def Receipes(request):
    if request.method == "POST":

        data = request.POST

        Vreciepe_name = data.get('reciepe_name') 
        Vreciepe_description = data.get('reciepe_description')
        Vreciepe_image = request.FILES.get('reciepe_image')
        print(Vreciepe_image)
        
        
        print(data) 

        Receipe.objects.create(
            reciepe_name = Vreciepe_name,
            reciepe_description = Vreciepe_description,
            reciepe_image = Vreciepe_image

        )

        return redirect('/reciepes/')
    
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__iconatains = request.GET.get('search'))
        

    context = {'Receipe':queryset}
    return render(request,'reciepes.html',context)


def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    
    if request.method=='POST':
        data = request.POST
        Vreciepe_name = data.get('reciepe_name') 
        Vreciepe_description = data.get('reciepe_description')
        Vreciepe_image = request.FILES.get('reciepe_image')
        
        queryset.reciepe_name= Vreciepe_name
        queryset.reciepe_description = Vreciepe_description
        if Vreciepe_image:
            queryset.reciepe_image = Vreciepe_image
        queryset.save()
        return redirect('/reciepes/')
    
    context = {'Receipe':queryset}
    return render(request,'update_recipe.html',context) 

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/reciepes/')


