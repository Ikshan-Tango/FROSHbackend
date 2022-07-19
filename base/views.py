from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'homepage.html')

def branchfees(request):
    return render(request,'branfee.html')

def hostel(request):
    return render(request,'hostelinfo.html')

def docuveri(request):
    return render(request,'docveri.html')

def camtour(request):
    return render(request,'campustour.html')

def digihand(request):
    return render(request,'digihandbook.html')

def offcouns(request):
    return render(request,'offcounseling.html')

def maps(request):
    return render(request,'maps.html')

def login(request):
    return render(request,'login.html')

