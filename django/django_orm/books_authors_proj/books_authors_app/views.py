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
    context = {
        "All_the_authors":
        Author.objects.all()
    }
    return render (request, "Authors.html", context)
def show_author(request):
    if request.method == 'POST':
        add_author = Author.objects.create(
            first_name =  request.POST['first'],
            last_name = request.POST['last'],
            notes = request.POST['notes'],
        )
    return redirect('/authors')
def View_Book(request, id):
    Books = {
        "Authors":Author.objects.all(),
        "book" : Book.objects.get(id = id)
    }

    return render(request, 'show_books.html', Books )
def display_authors(request, id):
    book = Book.objects.get(id = id)
    ex_author = Book.objects.exclude( id__in=author.books.values('id'))
    author = {
        "ex_author": ex_author,
        'Book': Book.objects.get(id = id),
    }
    authors = Author.objects.get(id=id)
    book.authors.add(authors)
    return redirect('book', id = id)

def View_author(request, id):
        author = {
        "books":Book.objects.all(),
        "author" : Author.objects.get(id = id)
    }
        return render(request, 'show_authors.html', author)
    
    

        # author = Author.objects.get(id = id)
    # ex_book = Book.objects.exclude( id__in=author.books.values('id'))
    # author = {
    #     "ex_book": ex_book,
    #     'Author': Author.objects.get(id = id),
    # }
