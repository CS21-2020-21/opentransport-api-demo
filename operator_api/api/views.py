from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *


class ModeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Mode.objects.all().order_by('id')
    serializer_class = ModeSerializer


class CatalogueViewSet(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all().order_by('id')
    serializer_class = CatalogueSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

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
        return queryset
