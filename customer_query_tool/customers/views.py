from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from customers.forms import *
import requests
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import routers, serializers, viewsets
from customers.models import *
from customers.serializers import *
from django.core.mail import send_mail
from django.conf import settings
from urllib.parse import urlencode
from django.core.paginator import Paginator




def index(request):
    return render(request, 'customers/index.html')

def my_account(request):
        
    try:
        customer = Customer.objects.get(customer_id=request.user.username)
    except:
        user = request.user
    
        customer_id = request.user.username
         
        name = request.user.first_name
    
        email = request.user.email
    
        customer = Customer.objects.get_or_create(user=user, customer_id=customer_id, name=name, email=email)
    
    return render(request, 'customers/my_account.html')

def query(request):
    #the user selects the query they would like to perform

    form = customerQueryForm()

    if request.method == "POST":

        form = customerQueryForm(request.POST)

        if form.is_valid():

            query_type = form.cleaned_data.get('query_type')

            #they are redirected to the page which they choose
            if query_type == 'purchase':
                return redirect(reverse('customers:query_purchases'))
            elif query_type == 'concession':
                return redirect(reverse('customers:query_concessions'))
            elif query_type == 'usage':
                return redirect(reverse('customers:query_usages'))

    context = {'form': form}

    return render(request, 'customers/query.html', context=context)


def change_data(request):
    return render(request, 'customers/change_data.html')


def query_purchases(request):
    #the user will be able to query view their purchases on this page

    context = {}

    form = requestDetailsForm()

    if request.method == "POST":

        form = requestDetailsForm(request.POST)

        if form.is_valid():

            #this is the URL of the API we want to query
            URL = "http://CS21CustomerProject.pythonanywhere.com/purchase/"
           
            #get the optional arguments from the form which the user submits
            date_from = form.cleaned_data.get('from_date')
            date_to = form.cleaned_data.get('to_date')
            skip = form.cleaned_data.get('skip')
            limit = form.cleaned_data.get('limit')

            #the request will be performed with the filterString set to the user name
            #this means that only the purchases for this user will be returned
            params = {'filterString': request.user.username}
            
            #get the data from the user through the form
            if date_from != "":
                params['travel_valid_during_from'] = date_from

            if date_to != "":
                params['travel_valid_during_to'] = date_to

            if skip is not None:
                params['skip'] = int(skip)

            if limit is not None:
                params['limit'] = int(limit)

            
            try:
                #try the request, passing in the necessary parameters
                response = requests.get(url=URL, params=params)
                
                #if the status code is 500, the request met unexpected conditions meaning there are no purchases
                if response.status_code==500:
                    context['empty'] = True
               
                #turn the request into json to parse
                data = response.json()
               
                context['purchases'] = []
                
                for item in data:
                    #add details of each purchase to a list which is passed in through the context dictionary
                    details = {}
                    details['booking_date'] = item['booking_date_time'][:10]
                    details['mode'] = item['mode']['short_desc']
                    details['operator'] = item['operator']['name']
                    details['class'] = item['travel_class']
                    details['price'] = item['transaction']['price']['amount']
                    details['passengers'] = item['passenger_type']
                    details['leaving_date'] = item['travel_from_date_time'][:10]
                    details['arriving_date'] = item['travel_to_date_time'][:10]
                    details['leaving_time'] = item['travel_from_date_time'][11:19]
                    details['arriving_time'] = item['travel_to_date_time'][11:19]
                    details['concession'] = item['concession']
                    details['position'] = item['reserved_position']
                    details['services'] = item['service_request']

                    context['purchases'].append(details)
                
            except:
                #if the request is not successful, we have no purchases to display
                context['purchases'] = False
                

    context['form'] = form
    return render(request, 'customers/query_purchases.html', context=context)


def query_concessions(request):

    context = {}

    form = requestDetailsForm()

    if request.method == "POST":

        form = requestDetailsForm(request.POST)

        if form.is_valid():

            #url of the API we want to query
            URL = "http://CS21CustomerProject.pythonanywhere.com/concession/"

            #get the data from the form to pass into the request
            date_from = form.cleaned_data.get('from_date')
            date_to = form.cleaned_data.get('to_date')
            skip = form.cleaned_data.get('skip')
            limit = form.cleaned_data.get('limit')

            #the username will be used to get the concessions for this user only
            params = {'filterString': request.user.username}
            
            if date_from != "":
                params['travel_valid_during_from'] = date_from

            if date_to != "":
                params['travel_valid_during_to'] = date_to

            if skip is not None:
                params['skip'] = int(skip)

            if limit is not None:
                params['limit'] = int(limit)


            try:
                #try the request
                response = requests.get(url=URL, params=params)

                #use the status code to check whether there were any concessions returned
                if response.status_code==500:
                    context['empty'] = True

                #turn the request into json to parse
                data = response.json()
                
                context['concessions'] = []
                
                for item in data:
                    #add the details of each concession to a list to be returned through the context dictionary
                    details = {}
                    details['name'] = item['name']
                    details['vehicle'] = item['mode']['short_desc']
                    details['company'] = item['operator']['name']
                    details['discount_value'] = str(item['discount']['discount_value'])+item['discount']['discount_type']
                    details['discount_details'] = item['discount']['discount_description']
                    details['valid_from'] = item['valid_from_date_time'][:10]
                    details['valid_to'] = item['valid_to_date_time'][:10]
                    details['conditions'] = item['conditions']

                    context['concessions'].append(details)
                
            except:
                context['concessions'] = False

    context['form'] = form

    return render(request, 'customers/query_concessions.html', context=context)


def query_usages(request):

    context = {}

    form = requestDetailsForm()

    if request.method == "POST":

        form = requestDetailsForm(request.POST)

        if form.is_valid():

            #URL of the API we want to query
            URL = "http://CS21CustomerProject.pythonanywhere.com/usage/"
           
            #get the data from the form
            date_from = form.cleaned_data.get('from_date')
            date_to = form.cleaned_data.get('to_date')
            skip = form.cleaned_data.get('skip')
            limit = form.cleaned_data.get('limit')

            #get the username to pass as a parameter into the request
            params = {'filterString': request.user.username}

            if date_from != "":
                params['travel_valid_during_from'] = date_from

            if date_to != "":
                params['travel_valid_during_to'] = date_to

            if skip is not None:
                params['skip'] = int(skip)

            if limit is not None:
                params['limit'] = int(limit)


            try:
                #try the request
                response = requests.get(url=URL, params=params)

                #use the status code to check whether any usages were returned
                if response.status_code==500:
                    context['empty'] = True
                
                #turn the response into json to parse
                data = response.json()

                context['usages'] = []

                for item in data:
                    
                    #add details of each usage to a list to be passed into the context dictionary
                    details = {}                   
                    details['mode'] = item['mode']['short_desc']
                    details['operator'] = item['operator']['name']
                    details['class'] = item['travel_class']
                    details['price'] = item['price']['amount']
                    details['pre_paid'] = 'yes' if item['pre_paid'] else 'no'
                    details['leaving_date'] = item['travel_from']['date_time'][:10]
                    details['arriving_date'] = item['travel_to']['date_time'][:10]
                    details['position'] = item['reference']['reference']

                    #in the case of many services, we want a string of a list of them
                    services = [service['service_type'] for service in item['services']]
                    details['services'] = ''
                    for service in services:
                        details['service'] = details['service'] + service + ' '
                    
                    context['usages'].append(details)
                
            except:
                context['usages'] = False

    context['form'] = form
    return render(request, 'customers/query_usages.html', context=context)


def link_account(request):

    form = linkAccountForm()

    if request.method == "POST":

        form = linkAccountForm(request.POST)

        if form.is_valid():
            linked_accounts = LinkedAccount.objects.filter(customer=request.user.username)
            linked_operators = [account.operator for account in linked_accounts]

    
            operator = form.cleaned_data.get('operator_cbo_box')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            url_params = {'operator':operator, 'email':email, 'username':username}
            if operator in linked_operators:
                return redirect(reverse('customers:link_failed'))
            else:
                return redirect('{}?{}'.format(reverse('customers:check_email'), urlencode(url_params)))
           
    context = {'form': form}

    return render(request, 'customers/link_account.html', context=context)
"""
            send_mail(
            subject = 'Account Verification',
            message = '''A user on PSD Ferries would like to link to your account on {}.
            If this is you, please enter the code 123456 when prompted on the PSD ferries website.
            '''.format(operator),
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [email,],
            fail_silently = False,
             )
"""
            

            
   

def check_email(request):

    form = verificationForm()
    
    if request.method == "POST":

        form = verificationForm(request.POST)

        if form.is_valid():
            
            code = form.cleaned_data.get('code')        
            if code == "123456":
                operator = request.GET.get('operator')
                email = request.GET.get('email')
                username = request.GET.get('username')
                customer = Customer.objects.get(customer_id=request.user.username)
                linked_account = LinkedAccount.objects.get_or_create(operator=operator, email=email, customer=customer, username=username)
                linked_account[0].save()
                return redirect(reverse('customers:account_linked'))
            else:
                return redirect(reverse('customers:link_failed'))
            
        
            
    context = {'form': form}

    return render(request, 'customers/check_email.html', context=context)

def account_linked(request):

    return render(request, 'customers/account_linked.html')

def link_failed(request):
    return render(request, 'customers/link_failed.html')

def linked_accounts(request):

    linked_accounts = LinkedAccount.objects.filter(customer=request.user.username)
    context = {'linked_accounts':linked_accounts}

    return render(request, 'customers/linked_accounts.html', context=context)


def show_linked_account_purchases(request, id_slug):
    context_dict = {}
    try:
    
        linked_account = LinkedAccount.objects.get(slug=id_slug)
       
        context_dict['account'] = linked_account

        URL = "https://cs21operatorapi.pythonanywhere.com/operator"

        all_operators = requests.get(url=URL).json()

        for operator in all_operators:
            if operator['item_metadata'][0]['val']==linked_account.operator:
                purchase_url = operator['item_metadata'][1]['val'] + 'purchase/?filterString=' + linked_account.username
                purchases = requests.get(url=purchase_url).json()
                purchase_list = []
                for purchase in purchases:
                    details = {}
                    details['operator'] = purchase['operator']['name']
                    details['date_from'] = purchase['travel_from_date_time'][:10]
                    details['date_to'] = purchase['travel_to_date_time'][:10]
                    details['price'] = purchase['transaction']['price']['amount']
                    purchase_list.append(details)
                               
                page_num = request.GET.get('page')
                if page_num is None:
                    context_dict['purchases'] = Paginator(purchase_list, 3).page(1)
                else:
                    context_dict['purchases'] = Paginator(purchase_list, 3).page(page_num)


    except:
        context_dict['account'] = None
        context_dict['purchases'] = None
    
    
    return render(request, 'customers/show_linked_account_purchases.html', context=context_dict)

def show_linked_account_concessions(request, id_slug):
    context_dict = {}
    try:
    
        linked_account = LinkedAccount.objects.get(slug=id_slug)
       
        context_dict['account'] = linked_account

        URL = "https://cs21operatorapi.pythonanywhere.com/operator"

        all_operators = requests.get(url=URL).json()

        for operator in all_operators:
            if operator['item_metadata'][0]['val']==linked_account.operator:
                
                concession_url = operator['item_metadata'][1]['val'] + 'concession/?filterString=' + linked_account.username
                concessions = requests.get(url=concession_url).json()
                concession_list = []
                for concession in concessions:
                    details = {}
                    details['name'] = concession['name']
                    details['operator'] = concession['operator']['name']
                    details['price'] = concession['price']['amount']
                    details['discount'] = str(concession['discount']['discount_value'])+concession['discount']['discount_type']
                    details['date_from'] = concession['valid_from_date_time'][:10]
                    details['date_to'] = concession['valid_from_date_time'][:10]
                    details['conditions'] = concession['conditions']
                    concession_list.append(details)
                               
                page_num = request.GET.get('page')
                if page_num is None:
                    context_dict['concessions'] = Paginator(concession_list, 3).page(1)
                else:
                    context_dict['concessions'] = Paginator(concession_list, 3).page(page_num)

                

    except:
        context_dict['account'] = None
        context_dict['concession'] = None
    
    
    return render(request, 'customers/show_linked_account_concessions.html', context=context_dict)

def show_linked_account_usages(request, id_slug):
    context_dict = {}
    try:
    
        linked_account = LinkedAccount.objects.get(slug=id_slug)
       
        context_dict['account'] = linked_account

        URL = "https://cs21operatorapi.pythonanywhere.com/operator"

        all_operators = requests.get(url=URL).json()

        for operator in all_operators:
            if operator['item_metadata'][0]['val']==linked_account.operator:
                usage_url = operator['item_metadata'][1]['val'] + 'usage/?filterString=' + linked_account.username
                usages = requests.get(url=usage_url).json()
                usage_list = []
                for usage in usages:
                    details = {}
                    details['operator'] = usage['operator']['name']
                    details['date_from'] = usage['travel_from']['date_time'][:10]
                    details['date_to'] = usage['travel_to']['date_time'][:10]
                    details['price'] = usage['price']['amount']
                    usage_list.append(details)
                
                               
                page_num = request.GET.get('page')
                if page_num is None:
                    context_dict['usages'] = Paginator(usage_list, 3).page(1)
                else:
                    context_dict['usages'] = Paginator(usage_list, 3).page(page_num)
                print(context_dict)
          

    except:
        context_dict['account'] = None
        context_dict['usage'] = None
    
    
    return render(request, 'customers/show_linked_account_usages.html', context=context_dict)




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
        return redirect("customers:index")
    else:
        return HttpResponse("Cannot delete account")



class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TravelFromViewSet(viewsets.ModelViewSet):
    queryset = TravelLocation.objects.all()
    serializer_class = TravelLocationSerializer

class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class Monetary_ValueViewSet(viewsets.ModelViewSet):
    queryset = Monetary_Value.objects.all()
    serializer_class = Monetary_ValueSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



class AccountBalanceViewSet(viewsets.ModelViewSet):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class LatLongViewSet(viewsets.ModelViewSet):
    queryset = LatLong.objects.all()
    serializer_class = LatLongSerializer

class LocationFromViewSet(viewsets.ModelViewSet):
    queryset = LocationFrom.objects.all()
    serializer_class = LocationFromSerializer

class LocationToViewSet(viewsets.ModelViewSet):
    queryset = LocationTo.objects.all()
    serializer_class = LocationToSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    
    serializer_class = PurchaseSerializer
    def get_queryset(self):
        queryset = Purchase.objects.all()
        customer_id = self.request.query_params.get('filterString', None)
        limit = self.request.query_params.get('limit', None)
        travel_valid_during_from = self.request.query_params.get('travel-valid-during-from', None)
        travel_valid_during_to = self.request.query_params.get('travel-valid-during-to', None)
        skip = self.request.query_params.get('skip', None)

        if customer_id is not None:
            customer = Customer.objects.get(customer_id=customer_id)
            queryset = queryset.filter(customer=customer)


        if travel_valid_during_from is not None and travel_valid_during_to is None:
            queryset = queryset.filter(travel_from_date_time__gte=travel_valid_during_from)

        elif travel_valid_during_to is not None and travel_valid_during_from is None:
            queryset = queryset.filter(travel_from_date_time__lte=travel_valid_during_to)
        
        elif travel_valid_during_to is not None and travel_valid_during_from is not None:
            queryset = queryset.filter(travel_from_date_time__range=(travel_valid_during_from, travel_valid_during_to))

        
        if limit is not None:
            queryset = queryset[:int(limit)]
        
        if skip is not None:
            queryset = queryset[::int(skip)]


        #sort out travel dates
        

        return queryset

class ConcessionViewSet(viewsets.ModelViewSet):
    serializer_class = ConcessionSerializer

    def get_queryset(self):
        queryset = Concession.objects.all()
        customer_id = self.request.query_params.get('filterString', None)
        limit = self.request.query_params.get('limit', None)
        travel_valid_during_from = self.request.query_params.get('concession-valid-during-from', None)
        travel_valid_during_to = self.request.query_params.get('concession-valid-during-to', None)
        skip = self.request.query_params.get('skip', None)

        if customer_id is not None:
            customer = Customer.objects.get(customer_id=customer_id)
            queryset = queryset.filter(customer=customer)

        if travel_valid_during_from is not None and travel_valid_during_to is None:
            queryset = queryset.filter(valid_from_date_time__gte=travel_valid_during_from)

        elif travel_valid_during_to is not None and travel_valid_during_from is None:
            queryset = queryset.filter(valid_to_date_time__lte=travel_valid_during_to)
        
        elif travel_valid_during_to is not None and travel_valid_during_from is not None:
            queryset = queryset.filter(valid_from_date_time__range=(travel_valid_during_from, travel_valid_during_to))


        if limit is not None:
            queryset = queryset[:int(limit)]
        
        
        if skip is not None:
            queryset = queryset[::int(skip)]

        return queryset

class UsageViewSet(viewsets.ModelViewSet):
    
    serializer_class = UsageSerializer

    def get_queryset(self):
        queryset = Usage.objects.all()
        customer_id = self.request.query_params.get('filterString', None)
        travel_valid_during_from = self.request.query_params.get('usage-occured-during-from', None)
        travel_valid_during_to = self.request.query_params.get('usage-occured-during-to', None)
        limit = self.request.query_params.get('limit', None)
        skip = self.request.query_params.get('skip', None)

        if customer_id is not None:
            customer = Customer.objects.get(customer_id=customer_id)
            queryset = queryset.filter(customer=customer)

        if travel_valid_during_from is not None and travel_valid_during_to is None:            
            queryset = queryset.filter(usage_date_time__gte=travel_valid_during_from)

        elif travel_valid_during_to is not None and travel_valid_during_from is None:
            queryset = queryset.filter(usage_date_time__lte=travel_valid_during_to)
        
        elif travel_valid_during_to is not None and travel_valid_during_from is not None:
            queryset = queryset.filter(usage_date_time__range=(travel_valid_during_from, travel_valid_during_to))



        if limit is not None:
            queryset = queryset[:int(limit)]
        
        
        if skip is not None:
            queryset = queryset[::int(skip)]

        return queryset
        
