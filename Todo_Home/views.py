from django.shortcuts import render,HttpResponse,redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .models import Todos
# Create your views here.
def Home(request):
    tasks=Task.objects.all().order_by('date')
    # return render(request,'templates/Home.html')
    # return HttpResponse("Home")
    return render(request,'Home.html',{'data':tasks})

def register(request):
    if request.method=='GET':
        return render(request,'signup.html',{'form':UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user=User.objects.create_user(request.POST["username"],password=request.POST["password1"])
                user.save()   #saves user object

                login(request,user)  #and also logs in the user
                return redirect("currenttodo")   #then we redirect to currenttodo
            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm() , 'message':"User is already exists."})

            return render(request,'signup.html',{'form':UserCreationForm() , 'message':user.username+"  created successfully."})
        else:
            return render(request,'signup.html',{'form':UserCreationForm() , 'message':"Passwords did't  matched."})
def currenttodo(request):
    return render(request,'currenttodo.html')
def logoutuser(request):
    if request.method == "POST":
        logout(request)

        return render(request,'signup.html',{'form':UserCreationForm() , 'message':"Logged out."})
    else:
        pass
def loginuser(request):
    if request.user.is_authenticated:
        return redirect("currenttodo")
    elif request.method=="GET":
        return render(request,'loginuser.html',{'form':AuthenticationForm()})
    else:
        # username = request.POST['username']
        # password = request.POST['password']
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'] )  #this gets the username and password form one who  wants to login and create the user object which is checked searched in the db
        if user is not None:
            login(request, user)
            return redirect("currenttodo")
        else:
            return render(request,'loginuser.html',{'form':AuthenticationForm(), 'message':"Username or Password did not match"})
