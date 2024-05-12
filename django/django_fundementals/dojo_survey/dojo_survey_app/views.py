from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def show(request):
    name = request.POST['username']
    location = request.POST['locations']
    language = request.POST['languages']
    comment = request.POST['comments']
    context = {
    	"name" : name,
    	"location" : location,
        "language": language,
        "comment": comment
    }
    return render(request,"show.html",context)