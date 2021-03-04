from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django_auto_prefetching import AutoPrefetchViewSetMixin, prefetch
from django.forms import Textarea
from rest_framework.viewsets import ModelViewSet

from .forms import *
from .serializers import *
from .models import *


@login_required
def change_data(request):
    """
    Returns form to change operator data

    :param request: request from the user
    """

    userprofile = request.user.userprofile
    operator_id = userprofile.operator_id
    item = Item.objects.get(operator_id=operator_id)

    ItemInlineFormSet = inlineformset_factory(Item, ItemMetadata, fields=('rel', 'val'), can_delete=False, widgets={
        'rel': Textarea(attrs={'cols': 60, 'rows': 1, 'readonly': 'readonly'}),
        'val': Textarea(attrs={'cols': 60, 'rows': 1})
    })
    if request.method == "POST":
        formset = ItemInlineFormSet(request.POST, request.FILES, instance=item)
        if formset.is_valid():
            formset.save()
            return redirect('/change_data')
    else:
        formset = ItemInlineFormSet(instance=item)
    return render(request, 'api/change_data.html', {'formset': formset})


class ModeViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = ModeSerializer

    def get_queryset(self):
        queryset = Mode.objects.all()
        return prefetch(queryset, self.serializer_class)


class CatalogueViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = CatalogueSerializer

    def get_queryset(self):
        queryset = Catalogue.objects.all()
        return prefetch(queryset, self.serializer_class)


class ItemViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = ItemSerializer
    lookup_field = 'operator_id'

    def get_queryset(self):
        queryset = Item.objects.all()
        rel = self.request.query_params.get('rel', None)
        val = self.request.query_params.get('val', None)
        href = self.request.query_params.get('href', None)

        if rel is not None and val is None:
            queryset = queryset.filter(item_metadata__rel__contains=rel)

        elif val is not None and rel is None:
            queryset = queryset.filter(item_metadata__val__contains=val)

        elif rel is not None and val is not None:
            queryset = queryset.filter(item_metadata__rel__contains=rel, item_metadata__val__contains=val)

        if href is not None:
            queryset = queryset.filter(href__contains=href)

        return prefetch(queryset, self.serializer_class)
