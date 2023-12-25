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

    return render(request,'reciepes.html')
