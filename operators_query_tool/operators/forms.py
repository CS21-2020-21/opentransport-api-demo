from django import forms


class operatorQueryForm(forms.Form):
    QUERY_CHOICES = [('mode', 'Modes'),
                     ('operator', 'Operators'), ]
    query_type = forms.CharField(label="What type of query would you like to perform?",
                                 widget=forms.Select(choices=QUERY_CHOICES))


class requestDetailsForm(forms.Form):
    href = forms.CharField(label="Website of an operator (optional)", max_length=50, required=False)
    description = forms.CharField(label="Description of an operator (optional)", max_length=50, required=False)
    operator_id = forms.CharField(label="ID of an operator (optional)", max_length=50, required=False)
    phone = forms.CharField(label="Phone number of an operator (optional)", max_length=50, required=False)
    email = forms.CharField(label="Email of an operator (optional)", max_length=50, required=False)
    homepage = forms.CharField(label="Homepage of an operator (optional)", max_length=50, required=False)
    language = forms.CharField(label="Default language of an operator (optional)", max_length=50, required=False)
    modes = forms.IntegerField(label="Number of modes of an operator (optional)", required=False)
    mode = forms.CharField(label="Mode of an operator (optional)", max_length=50, required=False)
    url = forms.CharField(label="MIPTAURL of an operator (optional)", max_length=50, required=False)
