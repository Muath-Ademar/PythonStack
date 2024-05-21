from django.shortcuts import render

from .models import*
def index(request):
    if request.method == 'POST':
        add = Show.objects.create(
            
        ) 
        return render(request, "show.html")
def view(request):
    context = {
        "All_the_shows":
        Show.objects.all()

    }
    return render(request, "All_shows.html", context)

# Create your views here.
