from django.shortcuts import render, redirect
from django.contrib import messages
from .models import*
import bcrypt

def index(request):

    return render (request, 'index.html')

def create(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user =  User.objects.create(
                first_name = request.POST['first'],
                Last_name = request.POST['last'],
                email = request.POST['email'],
                password = pw_hash,
                CMpassword = pw_hash,
                )
            request.session['user_id'] = user.id
        return redirect('/books')
        

def login(request):
    user = User.objects.filter(email=request.POST['loginemail']) 
    if user: 
        email = user[0] 
        if bcrypt.checkpw(request.POST['loginpassword'].encode(), email.password.encode()):
            request.session['user_id'] =email.id
            return redirect('/books')
    messages.error(request,"Login failed")
    return redirect('/')
    

def main(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "books": Book.objects.all()
    }
    return render(request, "main.html", context)
def add_book(request):
    if request.method == 'POST':
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/books')
        else:
            user = User.objects.get(id = request.session['user_id'])
            book = Book.objects.create(
                title = request.POST['title'],
                desc = request.POST['desc'],
                uploaded_by = user
            )
            book.users.add(user)
            return redirect('/books')
    return redirect('/books')


def details(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context ={
        "user": User.objects.get(id = request.session['user_id']),
        "book": Book.objects.get(id = book_id)
    }
    return render(request, "details.html", context)
def update(request, book_id):
    book = Book.objects.get(id = book_id)
    if request.method == 'POST':
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/books/{book_id}')
        else:
            book.title = request.POST['title']
            book.desc = request.POST['desc']
            book.save()
            return redirect(f'/books/{book_id}')
    context = {
            'book': book
    }
    return render(request, "details.html", context)

def un_favor(request, book_id):
    user = User.objects.get(id = request.session['user_id'])
    book = Book.objects.get(id = book_id)
    book.users.remove(user)
    return redirect('/books')

def favor(request, book_id):
    user = User.objects.get(id = request.session['user_id'])
    book = Book.objects.get(id = book_id)
    book.users.add(user)
    return redirect('/books')

def logout(request):
    request.session.flush() 
    return redirect ('/')

def Delete(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        if book.uploaded_by.id == request.session['user_id']:
            book.delete()
    return redirect('/books')