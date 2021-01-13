from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from operators.forms import operatorQueryForm
import requests
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages


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
                return render(request, 'operators/signin.html', {'success': "You are successfully signed up"})

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
        # I am currently working by hosting the api on the django development server
        modes_response = requests.get("http://127.0.0.1:8000/mode/")
        # the json returned by the query can be translated to a python list of dictionaries
  
        # these descriptions describe the mode of transport
        # e.g id: "1"
        #     short-desc: "train"
        #     long-desc: "includes intercity, Eurostar / TGV, etc."
    
        mode_list_of_dict = modes_response.json()    
    
        context['modes'] = mode_list_of_dict

    except:
        context['modes'] = False

    return render(request, 'operators/viewmodes.html', context=context)


def viewoperators(request):
    '''
    context = {}

    try:
        operators_response = requests.get("http://open-transport/operator")
        #get the json returned
        operator_list_of_dict = operators_response.json()

        operators = []

        #we are returned a list of dictionaries
        #the first dictionary is a meta-data stating that this is a list of operator dictionaries
        #the second dictionary is the list of operators
        #each operator has an item-metadata list of rel,val pairs
        #the rel will be for example name and the val will be the name of the company
        #we want to loop through each operator dictionary and get the details from its rel,val pairs

        for dictionary in operator_list_of_dict['items']:
            
            #we are looking at the list of rel,val pairs
            item_metadata = dictionary['item-metadata']

            #get the details of the operator from the rel,val pairs
            for item in item_metadata:
                if item['rel']=='urn:X-hypercat:rels:hasDescription:en':
                    operator_name = item['val']
                elif item['rel']=='urn:X-hypercat:rels:hasHomepage':
                    operator_url = item['val']
                elif item['rel'] == 'urn:X-opentransport:rels:hasId':
                    operator_id = item['val']
                elif item['rel'] == 'urn:X-opentransport:rels:hasEmail':
                    operator_email = item['val']
                elif item['rel'] == 'urn:X-opentransport:rels:hasPhone':
                    operator_phone = item['val']
                elif item['rel'] == 'urn:X-opentransport:rels:hasDefaultLanguage':
                    operator_default_language = item['val']

            #append the details that we will put in the context dictionary
            operators.append({'name':operator_name, 'url':operator_url})

           

         
        
        context['operators'] = operators
        
    except:
        context['operators'] = False
    '''

    return render(request, 'operators/viewOperators.html')


@login_required
def deactivate_user_view(request):
    return render(request, "account/delete_user_account.html")


@login_required
def deactivate_user(request):
    pk = request.user.id
    user = request.user

    if request.user.is_authenticated and request.user.id == user.id:
        user.is_active = False
        user.delete()
        return redirect("operators:index")
    else:
        return HttpResponse("Cannot delete account")
