from django.shortcuts import render, redirect # type: ignore
import random
from datetime import datetime

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'index.html')

def add(request):
    earnings = 0
    current_time = datetime.now().strftime("%B %d %Y, %I:%M %p")
    if 'message' not in request.session:
        request.session['message'] = ""
    request.session['box']= request.POST['box']
    if request.POST['box'] == 'Farm' or request.POST['box'] == 'Cave' or request.POST['box'] == 'House':
        earnings = random.randint(10, 20)
        request.session['message']= '<li class = "M"> You entered'  + " " + request.POST['box']+ " " + 'and earned'  + " " + str(earnings) + " " + "Gold." + " " + f'({current_time})' + "</li>"  + request.session['message'] 
    elif request.POST['box'] == 'Quest':
        earnings = random.randint(-50, 50)
        if earnings <0 :
            request.session['message'] = '<li Class = "R"> You faild a'+ " " + request.POST['box'] + ', and lost ' + str(earnings*-1) + " Gold... ouch!!"+ " " + f'({current_time})' + "</li>"+ request.session['message']
        else :
            request.session['message'] = '<li Class = "M"> You finished a' + " " + request.POST['box'] + ', and Won ' + str(earnings*1)+ " " + "Gold."+ " " + f'({current_time})' + "</li>" + request.session['message']
    request.session['counter']+=earnings
    return redirect('/')
