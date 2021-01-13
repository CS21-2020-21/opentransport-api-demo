from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

   


