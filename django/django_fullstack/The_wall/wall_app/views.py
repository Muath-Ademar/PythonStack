from django.shortcuts import render, redirect
from .models import User, Comment, Message
from django.contrib import messages
import bcrypt
def index(request):
    
    return render(request , 'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            Password = request.POST['password']
            pw_hash = bcrypt.hashpw(Password.encode(), bcrypt.gensalt()).decode() 
            user = User.objects.create(
            first_name = request.POST['first'],
            last_name = request.POST['last'],
            email = request.POST['email'],
            password = pw_hash
        )
        user.save()
        request.session['userId'] = user.id
        return redirect('/home') 
    return redirect('/')
def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userId'] = logged_user.id
            return redirect('/home')
    messages.error(request, "login failed")
    return redirect('/')

def logout(request):
    del request.session['userId']
    return redirect('/')

def home(request):
        if 'userId' in request.session:
            user_id = request.session.get('userId')
            user = User.objects.get(id = user_id)
            context = {
            'user': user,
            'messages': Message.objects.all().order_by('-created_at')
        }
            return render(request, 'home.html', context)
        else:
            return redirect('/')
def message(request):
    if request.method == 'POST':
        user_id = User.objects.get(id = request.session.get('userId'))
        message = Message.objects.create(
            message = request.POST['message'],
            user = user_id
        )
        message.save()
        return redirect('/home')
    
def wall(request):
    if 'userId' in request.session:
        context = {
            'user': User.objects.get(id = request.session.get('userId')),
            'messages': Message.objects.all(),
            
        }
        return render(request, 'wall.html', context)
    else:  
        return redirect('/')

def comment(request):
    if request.method == 'POST':
        user_id = User.objects.get(id = request.session.get('userId'))
        message_id = request.POST['message_id']
        message = Message.objects.get(id = message_id)
        comment = Comment.objects.create(
            comment =request.POST['comment'],
            user = user_id,
            message = message
        )
        comment.save()
    return redirect('/wall')
   