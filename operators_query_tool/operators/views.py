from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'operators/index.html')

def signup(request):
    return render(request, 'operators/signup.html')

def signin(request):
    return render(request, 'operators/signin.html')

def myaccount(request):
    return render(request, 'operators/myaccount.html')

def querydata(request):
    return render(request, 'operators/querydata.html')

def changedata(request):
    return render(request, 'operators/changedata.html')

def viewdata(request):
    return render(request, 'operators/viewdata.html')