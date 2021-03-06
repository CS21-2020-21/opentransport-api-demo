from django.forms import ModelForm
from django import forms

from allauth.account.forms import SignupForm

from .models import *


class CustomSignupForm(SignupForm):
    operator_id = forms.CharField(max_length=10, label='Operator ID')

    class Meta:
        model = UserProfile
        fields = ('operator_id')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.userprofile.operator_id = self.cleaned_data['operator_id']
        user.userprofile.save()
        return user


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class ItemMetadataForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
