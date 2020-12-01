from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from operators.forms import operatorQueryForm
import requests
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Modes


# Create your views here.

def index(request):
    return render(request, 'operators/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        email = request.POST['email']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'operators/signup.html', {'error': "Username already taken"})
            elif User.objects.filter(email=email).exists():
                return render(request, 'operators/signup.html', {'error': "Email already taken"})
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                print('user created')
                return render(request, 'operators/signup.html', {'success': "You are successfully signed up"})

        else:
            return render(request, 'operators/signup.html', {'error': "Password don't match"})

    else:
        return render(request, 'operators/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return render(request, 'operators/myaccount.html', {'success': "You're logged in now "})
        else:
            return render(request, 'operators/signin.html', {'error': "Invalid credentials"})

    else:
        return render(request, 'operators/signin.html', {'error': "Try logging again"})


def myaccount(request):
    return render(request, 'operators/myaccount.html')


def querydata(request):
    form = operatorQueryForm()

    if request.method == "POST":
        form = operatorQueryForm(request.POST)

        if form.is_valid():
            query_type = form.cleaned_data.get('query_type')
            if query_type == 'mode':
                return redirect(reverse('operators:viewmodes'))
            elif query_type == 'operator':
                # redirect to the page showing operators info
                # need to understand what is going on before we can implement this
                return redirect(reverse('operators:viewoperators'))

    context = {'form': form}

    return render(request, 'operators/querydata.html', context=context)


def changedata(request):
    return render(request, 'operators/changedata.html')


def viewmodes(request):
    # query the operators API with the get request /mode
    # the context dictionary will contain the data we have returned from the query

    context = {}
    # if the status code says the request went ok
    try:

        # this URL is just a placeholder for now, we will know the exact URL when we host the API
        modes_response = requests.get("http://open-transport/mode")
        # the json returned by the query can be translated to a python list of dictionaries
        # each dictionary has a key 'short-desc' which is mapped to a string detailing the mode of transport
        mode_list_of_dict = modes_response.json()

        # create a list of dictionaries, where each dictionary has a mapping for short-desc and long-desc
        # these descriptions describe the mode of transport
        # e.g short-desc: "train"
        #    long-desc: "includes intercity, Eurostar / TGV, etc."
        # rewritten this part below, left it just in case we might change back
        # modes = [{'short':dictionary['short-desc'], 'long':dictionary['long-desc']}
        #          for dictionary in mode_list_of_dict]

        modes = []
        for i, dictionary in enumerate(mode_list_of_dict):
            modes.append({'short': dictionary['short-desc'], 'long': dictionary['long-desc']})

            # create modes object and save it in the db
            m = Modes(mode_id=dictionary['id'], op_id=i, short_desc=dictionary['short-desc'],
                      long_desc=dictionary['long-desc'])  # not sure about op_id
            m.save()

        context['modes'] = modes

    except:
        context['modes'] = False

    return render(request, 'operators/viewmodes.html', context=context)


def viewoperators(request):
    context = {}
    try:
        operators_response = requests.get("http://open-transport/operator")
        operator_list_of_dict = operators_response.json()

        for i, dictionary in enumerate(operator_list_of_dict):
            print(i, dictionary)

    except:
        context['operators'] = False

    return render(request, 'operators/viewOperators.html')
