
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import user

def home(request):
    return render(request, "signin.html")


def signup(request):
    return render(request, "signup.html")

def insert_user(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    username = request.POST['Username']
    password = request.POST['password']
    us = user (fname, lname,email, username, password)
    us.save()
    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password = password)

        if user is not None:
            fname = user.first_name
            login(request, user)
            # messages.success(request,"Login Sucessfully!")
            # return render(request, "app/index.html",{'fname':fname})
        else:
            return redirect('home')
    return render(request, "signin.html")

# def employeesignin(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         pwd1 = request.POST['pwd1']
#         user = authenticate(username=username, password=pwd1)

#         if user is not None:
#             fname=user.first_name
#             login(request, user)
#             messages.success(request,"Login Sucessfully!")
#             return render(request, "employeesignin.html",{'fname':fname})
#         else:
#             messages.success(request,"Bad Credentials")
#             return redirect('home')
#     return render(request, "employeesignin.html")
 
def signout(request):
    logout(request)
    return redirect('signin')
    