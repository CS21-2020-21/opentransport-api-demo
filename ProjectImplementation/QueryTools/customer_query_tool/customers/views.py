import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.mail import send_mail # Currently disabled
from django.conf import settings # Currently disabled

from rest_framework import routers, serializers, viewsets

from urllib.parse import urlencode

from customers.forms import *
from customers.models import *
from customers.serializers import *


def index(request):
    """
    Returns index view

    :param request: request from the user
    """

    return render(request, 'customers/index.html')


def my_account(request):
    """
    Returns account view, if a Customer object doesn't exist it creates one.

    :param request: request from the user
    """
        
    user = request.user
    customer_id = request.user.username
    name = request.user.first_name
    email = request.user.email

    Customer.objects.get_or_create(user=user, customer_id=customer_id, name=name, email=email)
    
    return render(request, 'customers/my_account.html')


def ferry_query_selection(request):
    """
    Returns query from to view data held via the Customer API

    :param request: request from the user
    """

    return render(request, 'customers/ferry_query_selection.html')


def ferry_purchases(request):
    """
    Returns purchase data via the Customer API

    :param request: request from the user
    """

    context_dict = {}
    customer = Customer.objects.get(customer_id=request.user.username)
    purchases = Purchase.objects.filter(customer=customer)

    purchase_list = []
    for purchase in purchases:
        details = {}
        details['date_from'] = str(purchase.travel_from_date_time)[:10]
        details['date_to'] = str(purchase.travel_to_date_time)[:10]
        details['price'] = purchase['transaction']['price']['amount']
        purchase_list.append(details)
    
    page_num = request.GET.get('page')
    if page_num is None:
        context_dict['purchases'] = Paginator(purchase_list, 3).page(1)
    else:
        context_dict['purchases'] = Paginator(purchase_list, 3).page(page_num)

    return render(request, 'customers/ferry_purchases.html', context=context_dict)


def ferry_concessions(request):
    """
    Returns concession data via the Customer API

    :param request: request from the user
    """

    context_dict = {}
    customer = Customer.objects.get(customer_id=request.user.username)
    concessions = Concession.objects.filter(customer=customer)

    concession_list = []
    for concession in concessions:
        details = {}
        details['name'] = concession.name
        details['date_from'] = str(concession.valid_from_date_time)[:10]
        details['date_to'] = str(concession.valid_from_date_time)[:10]
        details['discount'] = str(concession.discount.discount_value) + concession.discount.discount_type
        concession_list.append(details)
    
    page_num = request.GET.get('page')
    if page_num is None:
        context_dict['concessions'] = Paginator(concession_list, 3).page(1)
    else:
        context_dict['concessions'] = Paginator(concession_list, 3).page(page_num)

    return render(request, 'customers/ferry_concessions.html', context=context_dict)


def ferry_usages(request):
    """
    Returns usage data via the Customer API

    :param request: request from the user
    """

    context_dict = {}
    customer = Customer.objects.get(customer_id=request.user.username)
    usages = Usage.objects.filter(customer=customer)

    usage_list = []
    for usage in usages:
        details = {}
        
        details['date'] = str(usage.usage_date_time)[:10]
        details['travel_class'] = usage.travel_class
        usage_list.append(details)
    
    page_num = request.GET.get('page')
    if page_num is None:
        context_dict['usages'] = Paginator(usage_list, 3).page(1)
    else:
        context_dict['usages'] = Paginator(usage_list, 3).page(page_num)

    return render(request, 'customers/ferry_usages.html', context=context_dict)


def link_account(request):
    """
    Allows users to link accounts from other operators

    :param request: request from the user
    """

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
            
            # If account is already linked
            if operator in linked_operators:
                return redirect(reverse('customers:link_failed'))
            else:
                return redirect('{}?{}'.format(reverse('customers:check_email'), urlencode(url_params)))
           
    context = {'form': form}

    return render(request, 'customers/link_account.html', context=context)


def check_email(request):
    """
    Enables email verification of account linkage

    :param request: request from the user
    """

    # Email is currently disabled, but this is the code for it.
    # To re-enable, uncomment below, go to settings.py and enable there then go to the google account settings and enable there too.
    #
    # send_mail(
    # subject = 'Account Verification',
    # message = '''A user on PSD Ferries would like to link to your account on {}.
    # If this is you, please enter the code 123456 when prompted on the PSD ferries website.
    # '''.format(operator),
    # from_email = settings.EMAIL_HOST_USER,
    # recipient_list = [email,],
    # fail_silently = False,
    #     )

    form = verificationForm()
    
    if request.method == "POST":

        form = verificationForm(request.POST)

        if form.is_valid():
            
            code = form.cleaned_data.get('code')        
            if code == "123456": # would need this to link to value in email
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
    """
    Account linking success page

    :param request: request from the user
    """

    return render(request, 'customers/account_linked.html')


def link_failed(request):
    """
    Account linking failure page

    :param request: request from the user
    """

    return render(request, 'customers/link_failed.html')


def linked_accounts(request):
    """
    Allows the user to view their linked accounts

    :param request: request from the user
    """

    context = {}
    linked_accounts = LinkedAccount.objects.filter(customer=request.user.username)

    page_num = request.GET.get('page')
    
    if page_num is None:
        context['linked_accounts'] = Paginator(linked_accounts, 1).page(1)
    else:
        context['linked_accounts'] = Paginator(linked_accounts, 1).page(page_num)

    return render(request, 'customers/linked_accounts.html', context=context)


def show_linked_account_purchases(request, id_slug):
    """
    Retrieves linked account purchase data and displays to user
    
    :param request: request from the user
    """
    
    context_dict = {}
    try:
        linked_account = LinkedAccount.objects.get(slug=id_slug)
       
        context_dict['account'] = linked_account
        
        URL = "https://cs21operatorapi.pythonanywhere.com/operator"
        headers = {'Authorization': 'Token 61a5afd286c1c0ec9f3c74a843186cefe458dc2c'}
        params = {'rel': 'urn:X-hypercat:rels:hasDescription:en', 'val': linked_account.operator}
        operator = requests.get(url=URL, headers=headers, params=params).json()

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
    """
    Retrieves linked account concession data and displays to user
    
    :param request: request from the user
    """

    context_dict = {}
    try:
        linked_account = LinkedAccount.objects.get(slug=id_slug)
       
        context_dict['account'] = linked_account

        URL = "https://cs21operatorapi.pythonanywhere.com/operator"
        headers = {'Authorization': 'Token 61a5afd286c1c0ec9f3c74a843186cefe458dc2c'}
        params = {'rel': 'urn:X-hypercat:rels:hasDescription:en', 'val': linked_account.operator}
        operator = requests.get(url=URL, headers=headers, params=params).json()
     
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
    """
    Retrieves linked account usage data and displays to user
    
    :param request: request from the user
    """

    context_dict = {}
    try:
        linked_account = LinkedAccount.objects.get(slug=id_slug)

        context_dict['account'] = linked_account

        URL = "https://cs21operatorapi.pythonanywhere.com/operator"
        headers = {'Authorization': 'Token 61a5afd286c1c0ec9f3c74a843186cefe458dc2c'}
        params = {'rel': 'urn:X-hypercat:rels:hasDescription:en', 'val': linked_account.operator}
        operator = requests.get(url=URL, headers=headers, params=params).json()

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
                
    except:
        context_dict['account'] = None
        context_dict['usage'] = None
    
    return render(request, 'customers/show_linked_account_usages.html', context=context_dict)


@login_required
def delete_user_view(request):
    """
    Enables users to delete their accounts
    
    :param request: request from the user
    """

    return render(request, "account/delete_user_account.html")


# Possibility of removing HTTPResponse from this code, will help clean up imports
@login_required
def delete_user(request):
    """
    Performs the deletion of a user account
    
    :param request: request from the user
    """

    pk = request.user.id
    user = request.user

    if request.user.is_authenticated and request.user.id == user.id:
        user.is_active = False
        user.delete()
        return redirect("customers:index")
    else:
        return redirect("customers:delete_user_failed")


@login_required
def delete_user_failed(request):
    """
    Returns to user if account deletion fails
    
    :param request: request from the user
    """

    return render(request, 'customers/delete_user_failed.html')


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
        