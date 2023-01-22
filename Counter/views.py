from django.shortcuts import render, redirect

def home(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
        request.session['flag'] = 0
    if request.session['flag'] == 0:
        request.session['counter'] = request.session['counter']+1
    else:
        request.session['flag'] = 0
    return render(request, 'home.html')

def increment_by_two(request):
    if request.method == 'POST':
        request.session['counter'] = request.session['counter']+2
        request.session['flag'] = 1
    return redirect('/counter')

# def scsess(request):
#     return redirect('/')

def destroy_session(request):
    del request.session['counter']
    del request.session['flag']
    return redirect('/counter')
