from django.shortcuts import render, redirect
import random

def index(request):
    if 'random' not in request.session:
        request.session['random'] = random.randint(1, 100)
    print(request.session['random'])
    return render(request, 'index.html')
def play(request):
    guessNum = int(request.POST['number'])
    if int(guessNum) < request.session['random']:
        request.session['text'] ="too low"
        request.session['color'] = "red"
    elif int(guessNum) > request.session['random']:
        request.session['text'] ="too high"
        request.session['color'] = "red"
    else:
        request.session['text'] = f"{request.session['random']} was the number"
        request.session['color'] = "green"
    return redirect("/")


