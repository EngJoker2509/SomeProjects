from django.shortcuts import render, redirect, HttpResponse
import random


def greate_number_game(reqeust):
    if 'server_number' not in reqeust.session:
        reqeust.session['server_number'] = random.randint(1, 100)
        reqeust.session['counter'] = 0
    return render(reqeust, 'GreatNumberGame.html')


def guess(request):
    request.session['counter'] = request.session['counter']+1
    if (request.session['counter'] <= 5):
        if request.method == 'POST':
            number = request.POST['number']
            if request.session['server_number'] == int(number):
                request.session['flag'] = 0
            elif request.session['server_number'] < int(number):
                request.session['flag'] = 1
            elif request.session['server_number'] > int(number):
                request.session['flag'] = 2
            else:
                request.session['flag'] = 4
                # return redirect('/')
    # request.session['flag'] = 5
    # request.session['counter'] = request.session['counter']+1
    return redirect('/')


def destroy(request):
    del request.session['server_number']
    del request.session['flag']
    return redirect('/')
