from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from operators.forms import operatorQueryForm



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
    form = operatorQueryForm()

    if request.method=="POST":
        form = operatorQueryForm(request.POST)

        if form.is_valid():
            query_type = form.cleaned_data.get('query_type')
            if query_type=='mode':
                return redirect(reverse('operators:viewmodes'))
            elif query_type=='operator':
                #redirect to the page showing operators info
                #need to understand what is going on before we can implement this
                return redirect(reverse('operators:viewoperators'))


            
    context = {'form':form}
    
    return render(request, 'operators/querydata.html', context=context )

def changedata(request):
    return render(request, 'operators/changedata.html')

def viewmodes(request):
    #query the operators API with the get request /mode
    #the context dictionary will contain the data we have returned from the query

    return render(request, 'operators/viewmodes.html')

def viewoperators(request):
    return render(request, 'operators/viewOperators.html')