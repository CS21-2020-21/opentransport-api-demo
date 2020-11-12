from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'ferries/index.html')

def signup(request):
    return render(request, 'ferries/signup.html')

def signin(request):
    return render(request, 'ferries/signin.html')

def myaccount(request):
    return render(request, 'ferries/myaccount.html')

def querydata(request):
    return render(request, 'ferries/querydata.html')

def changedata(request):
    return render(request, 'ferries/changedata.html')

def viewdata(request):
    return render(request, 'ferries/viewdata.html')