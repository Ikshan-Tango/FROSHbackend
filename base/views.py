from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login as dj_login
from django.http import HttpResponse
from .models import Branches
# Create your views here.

def home(request):
    return render(request,'base/homepage.html')

def branchfees(request):
    return render(request,'base/branfee.html')

def hostel(request):
    return render(request,'base/hostelinfo.html')

def docuveri(request):
    return render(request,'base/docveri.html')

def camtour(request):
    return render(request,'base/campustour.html')

def digihand(request):
    return render(request,'base/digihandbook.html')

def offcouns(request):
    return render(request,'base/offcounseling.html')

def maps(request):
    return render(request,'base/maps.html')

def landing(request):
    branches=Branches.objects.all()
    context={"branches":branches}
    return render(request,'base/landing.html',context)

def login(request):
    if request.method == 'POST': # loads the data of user credentials from the form 
        username = request.POST.get('username')
        password =  request.POST.get('password')

        try:
            user=User.objects.get(username = username)
        except:
             messages.error(request, "Error: User does not exist")
        user=authenticate(request,username = username ,password=password)

        if user is not None:
            dj_login(request,user)
            return redirect('landing')
        else:
            messages.error(request, "Error: Username or password does not exist")
    return render(request,'base/login.html')