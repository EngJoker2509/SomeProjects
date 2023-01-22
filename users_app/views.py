from django.shortcuts import render, HttpResponse,redirect
from .models import users


def index(request):
    # models.delete(41)
    # users.create()
    context = {
        'all_the_users': users.objects.all()
    }
    return render(request, 'index.html', context)
    # return HttpResponse('Success')


def fetch_date(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        users.create(first_name, last_name, email, age)
    return redirect('/')
