from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserSignup,UserLogin,ToDoForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import TODO
# Create your views here.
def home(request):
    return render(request,'index.html')

def user_login(request):
    return render(request,'login.html')


def user_signup(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pass1=form.cleaned_data['password1']
            pass2=form.cleaned_data['password2']
            if pass1 == pass2:
                form.save()
                messages.success(request,'Successfully Registered...Now Login ...')
                return redirect('/login')
            else:
                messages.success(request,'Password Mismatch..')
                return redirect('/signup')
        else:
            messages.error(request,"Something went wrong..")
            return redirect('/signup')
    else:
        form=UserSignup()
        return render(request,'signup.html',{'form':form})
    

def user_login(request):
    # if not request.user.is_authenticated:
    if request.method == 'POST':
            form=UserLogin(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Successful Login")
                    return redirect('/addtodo')
                else:
                    return redirect('/signup')
            else:
                messages.error(request,'Form is not valid')
                return redirect('/login')
    else:
        form=UserLogin()
        return render(request,'login.html',{'form':form})       
    
    # else:
    #     pass


def user_logout(request):
    logout(request)
    return redirect('/')



def addtodo(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            user=request.user
            form=ToDoForm(request.POST)
            if form.is_valid():
                title=request.POST['title']
                status=request.POST['status']
                priority=request.POST['priority']
                todo=TODO.objects.create(title=title,status=status,priority=priority,user=user)
                todo.save()
                return redirect('/alltodo')
            else:
                messages.error(request,"Invalid Form")
                return redirect('/addtodo')
        else:
            form=ToDoForm()
            return render(request,'addtodo.html',{'form':form})
    else:
        return redirect('/login')

def alltodo(request):
    todos=TODO.objects.filter(user=request.user)
    return render(request,'showtodo.html',{'todos':todos})


def editTodo(request,rid):
    if request.user.is_authenticated:
        if request.method =='POST':
            todo=TODO.objects.get(id=rid)
            form=ToDoForm(request.POST,instance=todo)
            if form.is_valid():
                form.save()
                return redirect('/alltodo')
        else:
            todo=TODO.objects.get(id=rid)
            form=ToDoForm(instance=todo)
            return render(request,'edittodo.html',{'form':form})    
    else:
        return redirect('/login')

def deleteTodo(requst,rid):
    todo=TODO.objects.get(id=rid)
    todo.delete()
    return redirect('/alltodo')