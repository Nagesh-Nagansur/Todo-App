from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import TodoForm
from django.forms import  modelformset_factory
from .models import Todos
from django.utils import timezone
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
    todos = Todos.objects.filter(user=request.user,datecompleted__isnull=True) #important__isnull=False    #no completed todos it wont show those which are datecompleted is true
    return render(request,'currenttodo.html',{'todo':todos})

def viewtodo(request,pk_id):
    todo = get_object_or_404(Todos,pk=pk_id,user=request.user)   #this is instance of Todos model
    if  request.method == "GET":
        form = TodoForm(instance=todo)                   #we are sending instance to form so it fills th data
        return render(request,'viewtodo.html',{'todo':todo,'form':form})
    else:
        form=TodoForm(request.POST,instance=todo)
        form.save()
        return redirect('currenttodo')
def completetodo(request,pk_id):
    todo = get_object_or_404(Todos,pk=pk_id,user=request.user)
    if request.method=="POST":
        todo.datecompleted=timezone.now()
        todo.save()
        return redirect('currenttodo')
        
def deletetodo(request,pk_id):
    # todo = get_object_or_404(Todos,id=pk_id,user=request.user)
    todo=Todos.objects.get(id=pk_id,user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect('currenttodo')
# def completedtodo(request):
#     todos = Todos.objects.filter(user=request.user,datecompleted=True)
#     if request.method == "POST":
#         return render(request,'completedtodo.html',{'todo':todos })


# instance = SomeModel.objects.get(id=id)
# instance.delete()
