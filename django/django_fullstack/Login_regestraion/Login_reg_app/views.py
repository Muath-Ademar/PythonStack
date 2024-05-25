from django.shortcuts import render, redirect
from django.contrib import messages
from .models import*
import bcrypt

def index(request):
    context1 = {
        'registration':
        Registration.objects.all()
    }
    return render (request, 'index.html', context1)

def create(request):
    if request.method == 'POST':
        errors = Registration.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user =  Registration.objects.create(
                first_name = request.POST['first'],
                Last_name = request.POST['last'],
                email = request.POST['email'],
                password = pw_hash,
                CMpassword = pw_hash,
                )
            request.session['user_id'] = user.id
            
        return redirect('/success')
        

def login(request):
    user = Registration.objects.filter(email=request.POST['loginemail']) 
    if user: 
        email = user[0] 
        if bcrypt.checkpw(request.POST['loginpassword'].encode(), email.password.encode()):
            request.session['userid'] =email.id
            return redirect('/success')
    messages.error(request,"Login failed")
    return redirect("/")
    
def success(request):
    # user_id = request.session.get('user_id')
    if 'userid' in request.session:
        # user = Registration.objects.get(id=user_id)
        context = {
            'user':Registration.objects.get(id=request.session['userid'])
        }
        return render(request,'success.html',context)
    else:
        return redirect('/')


def logout(request):
    # if ('user_id' in request.session):
    del request.session['userid']
    return redirect('/')

