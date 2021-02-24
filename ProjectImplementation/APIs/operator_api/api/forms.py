from django.forms import ModelForm
from .models import *
from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    operator_id = forms.CharField(max_length=10, label="Operater ID")

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
