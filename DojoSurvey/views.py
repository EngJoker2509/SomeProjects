from django.shortcuts import render,redirect

def home(request):
    return render(request,'home.html')

def result(request):
    if request.method =="POST":
        first_name = request.POST['first_name']
        favorite_language = request.POST['favorite_language']
        dojo_location=request.POST['dojo_location']
        comment=request.POST['comment']

        context= {
            'first_name':first_name,
            'favorite_language':favorite_language,
            'dojo_location':dojo_location,
            'comment':comment
        }
    else:
        context={}

    return render(request,'result.html',context)