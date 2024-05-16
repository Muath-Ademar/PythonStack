from django.shortcuts import render, redirect
from .models import *

def index(request):
    Books = {
        "All_the_books":
        Book.objects.all()
    }
    return render(request, "book.html", Books)
def show_books(request):
    if request.method == 'POST':
        add_book = Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
        )
    return redirect('/')
def authors(request):
    authors = {
        "All_the_authors":
        Author.objects.all()
    }
    return render (request, "Authors.html", authors)
def show_author(request):
    if request.method == 'POST':
        add_author = Author.objects.create(
            first_name =  request .POST['first']
            last_name = request.POST['last']
            books = request.POST['']
            notes = request.POST['notes']
        )
