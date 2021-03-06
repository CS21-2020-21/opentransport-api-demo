import requests
from django import forms


# once the user has decided on the query they would like to perform, they can specify option arguments to pass into the query
class requestDetailsForm(forms.Form):
    from_date = forms.DateTimeField(label="All records after the date (optional)", required=False)
    to_date = forms.DateTimeField(label="All records before the date (optional)", required=False)
    skip = forms.IntegerField(label="How many records would you like to skip for pagination? (optional)",
                              required=False)
    limit = forms.IntegerField(label="What is the maximum number of records you would like to see? (optional)",
                               required=False)


class linkAccountForm(forms.Form):
    token_url = "https://cs21operatorapi.pythonanywhere.com/api-token-auth/"
    data = {'username': 'cs21operatorapi', 'password': '123'}
    token = requests.post(url=token_url, data=data).json()['token']

    URL = "https://cs21operatorapi.pythonanywhere.com/operator/"
    headers = {'Authorization': 'Token ' + token}
    request = requests.get(url=URL, headers=headers)
    operators_json = request.json()

    operators = [operator['item_metadata'][0]['val'] for operator in operators_json]
    operator_choices = [(operator, operator) for operator in operators]
    operator_cbo_box = forms.CharField(label="What company would you like to link your account to?",
                                       widget=forms.Select(choices=operator_choices))
    email = forms.EmailField(
        label="What email account do you have registered on the account with which you would like to link?",
        required=False)
    username = forms.CharField(label="What is the username on the account with which you would like to link?")


class verificationForm(forms.Form):
    code = forms.CharField(label="Please enter the verification code sent to the email you provided")
