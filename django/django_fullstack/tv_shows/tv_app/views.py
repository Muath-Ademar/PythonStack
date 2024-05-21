from django.shortcuts import render, redirect

from .models import*
def index(request):

    return render(request, "add.html")

def add(request):
    if request.method == "POST":
        add = Show.objects.create(
            title = request.POST['title'],  
            release_date = request.POST["date"],
            Description = request.POST["desc"],
            network = request.POST["network"]
        )
        my_id = Show.objects.all().last()
        my_id2 = Show.objects.get(id=my_id.id)
        
        return redirect(f"info/{my_id2.id}")

def display(request):
    context ={
        "shows": Show.objects.all()
    }
    return render(request,"All.html", context)

def info(request,id):
    context = {
        "shows": Show.objects.get(id=id)
    }
    return render(request, "show_info.html", context)
def delete(request, id):
    show = Show.objects.get(id = id)
    show.delete()
    return redirect("/shows/new")

def edit_show(request,id):
    data={
        "show":Show.objects.get(id=id)
    }
    return render (request,"edit.html",data)

def make_edit(request, id):
    if request.method == 'POST':
        edit = Show.objects.get(id = id)
        edit.title = request.POST['title']
        edit.release_date = request.POST["date"]
        edit.Description = request.POST["desc"]
        edit.network = request.POST["network"]
        edit.save()
        return redirect('/shows')
    
def red(request):
    return redirect ('/shows')
    
