from django.shortcuts import render,HttpResponse,redirect
from .models import *

def index(request):
    context={
        'all_users': dojos.objects.all()
    }
    return render(request,'index.html',context)

def add_dojo(request):
    if request.method == "POST":
        name =request.POST['name']
        city=request.POST['city']
        state=request.POST['state']
    dojos.create(name,city,state)
    return redirect('/')

def add_ninja(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dojos_id=request.POST['dojo']
        ninjas.create(first_name,last_name,dojos_id)
    return redirect('/')

def delete(request):
    if request.method == "POST":
        id = request.POST['delete']
        print('Hellooo',id)
        ninjas.ninja_delete(id)
        dojos.dojos_delete(id)
    return redirect('/')
