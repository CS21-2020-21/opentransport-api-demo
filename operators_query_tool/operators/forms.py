from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

QUERY_CHOICES = [('mode', 'modes of transport'),
                 ('operator', 'operators'), ]


class operatorQueryForm(forms.Form):
    query_type = forms.CharField(label="What type of query would you like to perform?",
                                 widget=forms.Select(choices=QUERY_CHOICES))
