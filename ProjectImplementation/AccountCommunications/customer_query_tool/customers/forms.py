from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import requests
from .models import *

#this form will be used on the page where the user selects which query they would like to perform
class customerQueryForm(forms.Form):
    QUERY_CHOICES = [('purchase', 'My purchases'),
                ('concession', 'My concessions'),
                ('usage', 'My usages'),]
    query_type = forms.CharField(label="Please select what you would like to view", 
                                widget=forms.Select(choices=QUERY_CHOICES))

#once the user has decided on the query they would like to perform, they can specify option arguments to pass into the query
class requestDetailsForm(forms.Form):
    from_date = forms.DateTimeField(label="All records after the date  (optional)", required=False)
    to_date = forms.DateTimeField(label="All records before the date  (optional)", required=False)
    skip = forms.IntegerField(label="How many records would you like to skip for pagination?  (optional)", required=False)
    limit = forms.IntegerField(label="What is the maximum number of records you would like to see? (optional)", required=False)

class linkAccountForm(forms.Form):
    URL = "https://cs21operatorapi.pythonanywhere.com/operator/"
    headers = {'Authorization': 'Token e49c12b8afba06c33f3b88e4c4d93f1a94748dca'}
    request = requests.get(url=URL, headers=headers)
    operators_json = request.json()
    operators = [operator['item_metadata'][0]['val'] for operator in operators_json]
    for operator in operators:
        if not User.objects.filter(username=operator).exists():
            User.objects.create_superuser(username=operator, password="12345678abc", email="")
        
    operator_choices = [(operator, operator) for operator in operators]
    operator_cbo_box = forms.CharField(label="What company would you like to link your account to?", widget=forms.Select(choices=operator_choices))
    email = forms.EmailField(label="What email account do you have registered on the account with which you would like to link?")
    username = forms.CharField(label="What is the username on the account with which you would like to link?")
    
class verificationForm(forms.Form):
    code = forms.CharField(label="Please enter the verification code sent to the email you provided")




   


