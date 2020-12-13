from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import TodoForm
from django.forms import  modelformset_factory
from .models import Todos
# Create your views here.
def Home(request):
    return render(request,'Home.html')



def register(request):
    if request.method == 'GET':
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




def logoutuser(request):
    if request.method == "POST":
        logout(request)

        return render(request,'signup.html',{'form':UserCreationForm() , 'message':"Logged out."})
    else:
        pass


def loginuser(request):
    # if request.user.is_authenticated:
    #     return redirect('currenttodo')
    if request.method=="GET":
        return render(request,'loginuser.html',{'form':AuthenticationForm()})
    else:
        # username = request.POST['username']
        # password = request.POST['password']
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'] )  #this gets the username and password form one who  wants to login and create the user object which is checked searched in the db
        if user is not None:
            login(request, user)
            return redirect('currenttodo')
        else:
            return render(request,'loginuser.html',{'form':AuthenticationForm(), 'message':"Username or Password did not match"})



def createtodo(request):
    if request.method == 'GET':
        return render(request,"createtodo.html",{'form':TodoForm()})
    else :
        form = TodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user =request.user
        newtodo.save()
        return redirect('currenttodo')

def currenttodo(request):

    todos = Todos.objects.filter(user=request.user)
    return render(request,'currenttodo.html',{'todo':todos})
