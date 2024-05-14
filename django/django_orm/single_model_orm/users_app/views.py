from django.shortcuts import render, redirect
from .models import Users
def index(request):
    users = {
        "All_the_users":
        Users.objects.all()
    }
    return render(request, "index.html",users)
def form(request):
    if request.method == 'POST':
        add_user= Users.objects.create(
            first_name= request.POST['first'],
            last_name = request.POST['Last'],
            email_address = request.POST['email'],
            age= request.POST['age'],
        )
        add_user.save()
    return redirect("/")
