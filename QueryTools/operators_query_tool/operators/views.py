import requests

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator

from urllib.parse import urlencode

from operators.forms import *


def index(request):
    """
    Returns index view

    :param request: request from the user
    """

    return render(request, 'operators/index.html')


def my_account(request):
    """
    Returns my_account view

    :param request: request from the user
    """

    return render(request, 'operators/my_account.html')


def query(request):
    """
    Returns query view form for user to select the query they wish to perform

    :param request: request from the user
    """

    form = operatorQueryForm()

    if request.method == 'POST':

        form = operatorQueryForm(request.POST)

        if form.is_valid():
            query_type = form.cleaned_data.get('query_type')

            if query_type == 'mode':
                return redirect(reverse('operators:query_modes'))
            elif query_type == 'operator':
                return redirect(reverse('operators:query_operators'))

    context = {'form': form}

    return render(request, 'operators/query.html', context=context)


def change_data(request):
    """
    Returns change data view

    :param request: request from the user
    """

    return render(request, 'operators/change_data.html')


def query_modes(request):
    """
    Returns query_modes view to show the user the modes of transport available

    :param request: request from the user
    """

    token_url = 'https://cs21operatorapi.pythonanywhere.com/api-token-auth/'
    data = {'username':'cs21operatorapi', 'password':'123'}
    token = requests.post(url=token_url, data=data).json()['token']
    
    auth_header = {'Authorization': 'Token ' + token}
    URL = 'https://cs21operatorapi.pythonanywhere.com/mode/'

    context = {}

    try:
        response = requests.get(url=URL, headers=auth_header)
        data = response.json()

        context['mode_list'] = []

        for item in data:
            details = {}
            details['id'] = item['id']
            details['short_desc'] = item['short_desc']
            details['long_desc'] = item['long_desc']

            context['mode_list'].append(details)

        page_num = request.GET.get('page')
        if page_num is None:
            context['modes'] = Paginator(context['mode_list'], 3).page(1)
        else:
            context['modes'] = Paginator(context['mode_list'], 3).page(page_num)

    except:
        context['modes'] = False

    return render(request, 'operators/query_modes.html', context=context)


def query_operators(request):
    """
    Returns query operators view giving the user a form to enter any parameters they wish

    :param request: request from the user
    """

    context = {}

    form = requestDetailsForm()

    if request.method == 'POST':

        form = requestDetailsForm(request.POST)

        if form.is_valid():
            href = form.cleaned_data.get('href')
            description = form.cleaned_data.get('description')
            operator_id = form.cleaned_data.get('operator_id')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            homepage = form.cleaned_data.get('homepage')
            language = form.cleaned_data.get('language')
            modes = form.cleaned_data.get('modes')
            mode = form.cleaned_data.get('mode')
            url = form.cleaned_data.get('url')

            url_params = {'href': href, 'description': description, 'operator_id': operator_id, 'phone': phone,
                          'email': email, 'homepage': homepage, 'language': language, 'modes': modes, 'mode': mode,
                          'url': url}

            return redirect('{}?{}'.format(reverse('operators:view_operators'), urlencode(url_params)))

    context['form'] = form

    return render(request, 'operators/query_operators.html', context=context)


def view_operators(request):
    """
    Returns view_operators view to display the operators

    :param request: request from the user
    """

    href = request.GET.get('href')
    description = request.GET.get('description')
    operator_id = request.GET.get('operator_id')
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    homepage = request.GET.get('homepage')
    language = request.GET.get('language')
    modes = request.GET.get('modes')
    mode = request.GET.get('mode')
    url = request.GET.get('url')

    context = {'href': href, 'description': description, 'operator_id': operator_id, 'phone': phone,
               'email': email, 'homepage': homepage, 'language': language, 'modes': modes, 'mode': mode, 'url': url}

    params = {}
    if href != '':
        params['href'] = href

    if description != '':
        params['rel'] = 'description'
        params['val'] = description

    if operator_id != '':
        params['rel'] = 'id'
        params['val'] = operator_id

    if phone != '':
        params['rel'] = 'phone'
        params['val'] = phone

    if email != '':
        params['rel'] = 'email'
        params['val'] = email

    if homepage != '':
        params['rel'] = 'homepage'
        params['val'] = homepage

    if language != '':
        params['rel'] = 'language'
        params['val'] = language

    if mode != '':
        params['rel'] = 'mode'
        params['val'] = mode

    if url != '':
        params['rel'] = 'url'
        params['val'] = url

    try:
        token_url = 'https://cs21operatorapi.pythonanywhere.com/api-token-auth/'
        data = {'username':'cs21operatorapi', 'password':'123'}
        token = requests.post(url=token_url, data=data).json()['token']

        auth_header = {'Authorization': 'Token ' + token}
        URL = 'https://cs21operatorapi.pythonanywhere.com/operator/'

        response = requests.get(url=URL, params=params, headers=auth_header)
        data = response.json()

        context['operators_list'] = []

        for item in data:

            details = {}
            details['href'] = item['href']

            for pair in item['item_metadata']:

                if pair['rel'] == 'urn:X-hypercat:rels:hasDescription:en':
                    details['description'] = pair['val']

                elif pair['rel'] == 'urn:X-hypercat:rels:hasHomepage':
                    details['homepage'] = pair['val']

                elif pair['rel'] == 'urn:X-opentransport:rels:hasId':
                    details['id'] = pair['val']

                elif pair['rel'] == 'urn:X-opentransport:rels:hasEmail':
                    details['email'] = pair['val']

                elif pair['rel'] == 'urn:X-opentransport:rels:hasPhone':
                    details['phone'] = pair['val']

                elif pair['rel'] == 'urn:X-opentransport:rels:hasDefaultLanguage':
                    details['language'] = pair['val']

            context['operators_list'].append(details)

        page_num = request.GET.get('page')
        pages = Paginator(context['operators_list'], 1)
        if page_num is None:
            context['operators'] = pages.page(1)
        else:
            context['operators'] = pages.page(page_num)
    except:
        context['operators'] = False

    return render(request, 'operators/view_operators.html', context=context)


@login_required
def deactivate_user_view(request):
    return render(request, 'account/delete_user_account.html')


@login_required
def deactivate_user(request):
    pk = request.user.id
    user = request.user

    if request.user.is_authenticated and request.user.id == user.id:
        user.is_active = False
        user.delete()
        return redirect('operators:index')
    else:
        return HttpResponse('Cannot delete account')
