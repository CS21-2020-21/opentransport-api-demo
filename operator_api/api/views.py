from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
# from rest_framework.permissions import IsAuthenticated
from .forms import *
from django.forms import Textarea
from .serializers import *
from .models import *

@login_required
def change_data(request):
    userprofile = request.user.userprofile
    operator_id = userprofile.operator_id
    item = Item.objects.get(operator_id=operator_id)

    ItemInlineFormSet = inlineformset_factory(Item, ItemMetadata, fields=('rel', 'val'), can_delete=False, widgets={
        'rel': Textarea(attrs={'cols': 60, 'rows': 1, 'readonly':'readonly'}), 'val': Textarea(attrs={'cols': 60, 'rows': 1})
    })
    if request.method == "POST":
        formset = ItemInlineFormSet(request.POST, request.FILES, instance=item)
        print("Formset is valid:", formset.is_valid())
        print(formset.non_form_errors())
        print(formset.errors)
        if formset.is_valid():
            # for form in formset:
            #     cleaned_data = form.cleaned_data
            #     rel = cleaned_data['rel']
            #     val = cleaned_data['val']
            #     print(rel, val)
            formset.save()
            return redirect('/change_data')
    else:
        formset = ItemInlineFormSet(instance=item)
    return render(request, 'api/change_data.html', {'formset': formset})


class ModeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Mode.objects.all().order_by('id')
    serializer_class = ModeSerializer


class CatalogueViewSet(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all().order_by('id')
    serializer_class = CatalogueSerializer


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    lookup_field = 'operator_id'

    def get_queryset(self):
        print("Getting query set")
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
        return queryset
