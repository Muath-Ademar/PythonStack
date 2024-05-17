from django.shortcuts import render, redirect 

from .models import Dojo, ninja
# Create your views here.
def index(request):
    Dojos = {
        "All_the_Dojos":
        Dojo.objects.all()
    }
    return render(request, "index.html" ,Dojos)

def show_dojo(request):
    if request.method == 'POST':
        Dojo.objects.create(
            name = request.POST['name'],
            city = request.POST['city'],
            state = request.POST['state'],
        )
        
    return redirect('/')

def show_ninja(request):

    if request.method == 'POST':
        dojo_id = request.POST['Dojo']
        dojos = Dojo.objects.get(id = dojo_id) 
        ninja.objects.create(
            first_name = request.POST['First'],
            last_name = request.POST['Last'],
            dojo_id = dojos
        )
        
    return redirect('/')