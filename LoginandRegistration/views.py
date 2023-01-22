from django.shortcuts import render,HttpResponse,redirect
import bcrypt
from .models import user

def index(request):
    return render(request,'login.html')

def register(request):    
    # include some logic to validate user input before adding them to the database!
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
      # create the hash    
    print(pw_hash)
          # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
    # be sure you set up your database so it can store password hashes this long (60 characters)
    # make sure you put the hashed password in the database, not the one from the form!
    user.objects.create(first_name=request.POST['username'], password=pw_hash,email_address=request.POST['email']) 
    return redirect("/") # never render on a post, always redirect!  

def validate_login(request):
    user1 = user.objects.filter(email_address=request.POST['email']) 
    if bcrypt.checkpw(request.POST['password'].encode(),):
        print("password match")
    else:
        print("failed password")