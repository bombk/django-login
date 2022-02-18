import re
from django import forms
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm ###default form
from .forms import CreateUserForm  ##custume form
from django.contrib import messages  ##for flash message

#for login and logout
from django.contrib.auth import authenticate, login,logout

##for access page only athorised persion
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    data={}
    return render(request,'home.html',data)

def signup(request):
    form=CreateUserForm
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created '+user +"sucessfully")

            return redirect('login')
    data={'form':form}
    return render(request,'signup.html',data)

def loginPage(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password incorrect')

    data={}
    return render(request,'login.html',data)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def about(request):
    data={}
    return render(request,'about.html',data)

@login_required(login_url='login')
def contact(request):
    data={}
    return render(request,'contact.html',data)