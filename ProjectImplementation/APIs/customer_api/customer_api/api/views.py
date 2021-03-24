from rest_framework.viewsets import ModelViewSet
from django_auto_prefetching import AutoPrefetchViewSetMixin, prefetch
from .models import *
from .serializers import *


class ModeViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = ModeSerializer

    def get_queryset(self):
        queryset = Mode.objects.all()
        return prefetch(queryset, self.serializer_class)


class DiscountViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = DiscountSerializer

    def get_queryset(self):
        queryset = Discount.objects.all()
        return prefetch(queryset, self.serializer_class)


class ServiceViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()
        return prefetch(queryset, self.serializer_class)


class LocationViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = Location.objects.all()
        return prefetch(queryset, self.serializer_class)


class TravelFromViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = TravelLocationSerializer

    def get_queryset(self):
        queryset = TravelLocation.objects.all()
        return prefetch(queryset, self.serializer_class)


class OperatorViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = OperatorSerializer

    def get_queryset(self):
        queryset = Operator.objects.all()
        return prefetch(queryset, self.serializer_class)


class Monetary_ValueViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = Monetary_ValueSerializer

    def get_queryset(self):
        queryset = Monetary_Value.objects.all()
        return prefetch(queryset, self.serializer_class)


class TransactionViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        return prefetch(queryset, self.serializer_class)


class CustomerViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        return prefetch(queryset, self.serializer_class)


class AccountBalanceViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = AccountBalanceSerializer

    def get_queryset(self):
        queryset = AccountBalance.objects.all()
        return prefetch(queryset, self.serializer_class)


class VehicleViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        return prefetch(queryset, self.serializer_class)


class TicketViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        queryset = Ticket.objects.all()
        return prefetch(queryset, self.serializer_class)


class LatLongViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = LatLongSerializer

    def get_queryset(self):
        queryset = LatLong.objects.all()
        return prefetch(queryset, self.serializer_class)


class LocationFromViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = LocationFromSerializer

    def get_queryset(self):
        queryset = LocationFrom.objects.all()
        return prefetch(queryset, self.serializer_class)


class LocationToViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = LocationToSerializer

    def get_queryset(self):
        queryset = LocationTo.objects.all()
        return prefetch(queryset, self.serializer_class)


class PurchaseViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        queryset = Purchase.objects.all()
        customer_id = self.request.query_params.get('filterString', None)
        limit = self.request.query_params.get('limit', None)
        travel_valid_during_from = self.request.query_params.get('travel-valid-during-from', None)
        travel_valid_during_to = self.request.query_params.get('travel-valid-during-to', None)
        skip = self.request.query_params.get('skip', None)

        if customer_id is not None:
            customer = Customer.objects.get(customer_id=customer_id)
            queryset = queryset.filter(customer=customer)

        if travel_valid_during_from is not None and travel_valid_during_to is None:
            queryset = queryset.filter(travel_from_date_time__gte=travel_valid_during_from)

        elif travel_valid_during_to is not None and travel_valid_during_from is None:
            queryset = queryset.filter(travel_from_date_time__lte=travel_valid_during_to)

        elif travel_valid_during_to is not None and travel_valid_during_from is not None:
            queryset = queryset.filter(travel_from_date_time__range=(travel_valid_during_from, travel_valid_during_to))

        if limit is not None:
            queryset = queryset[:int(limit)]

        if skip is not None:
            queryset = queryset[::int(skip)]
            return queryset

        # sort out travel dates

        return prefetch(queryset, self.serializer_class)


class ConcessionViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = ConcessionSerializer

    def get_queryset(self):
        queryset = Concession.objects.all()
        customer_id = self.request.query_params.get('filterString', None)
        limit = self.request.query_params.get('limit', None)
        travel_valid_during_from = self.request.query_params.get('concession-valid-during-from', None)
        travel_valid_during_to = self.request.query_params.get('concession-valid-during-to', None)
        skip = self.request.query_params.get('skip', None)

        if customer_id is not None:
            customer = Customer.objects.get(customer_id=customer_id)
            queryset = queryset.filter(customer=customer)

        if travel_valid_during_from is not None and travel_valid_during_to is None:
            queryset = queryset.filter(valid_from_date_time__gte=travel_valid_during_from)

        elif travel_valid_during_to is not None and travel_valid_during_from is None:
            queryset = queryset.filter(valid_to_date_time__lte=travel_valid_during_to)

        elif travel_valid_during_to is not None and travel_valid_during_from is not None:
            queryset = queryset.filter(valid_from_date_time__range=(travel_valid_during_from, travel_valid_during_to))

        if limit is not None:
            queryset = queryset[:int(limit)]

        if skip is not None:
            queryset = queryset[::int(skip)]
            return queryset

        return prefetch(queryset, self.serializer_class)


class UsageViewSet(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = UsageSerializer

    def get_queryset(self):
        queryset = Usage.objects.all()
        customer_id = self.request.query_params.get('filterString', None)
        travel_valid_during_from = self.request.query_params.get('usage-occured-during-from', None)
        travel_valid_during_to = self.request.query_params.get('usage-occured-during-to', None)
        limit = self.request.query_params.get('limit', None)
        skip = self.request.query_params.get('skip', None)

        if customer_id is not None:
            customer = Customer.objects.get(customer_id=customer_id)
            queryset = queryset.filter(customer=customer)

        if travel_valid_during_from is not None and travel_valid_during_to is None:
            queryset = queryset.filter(usage_date_time__gte=travel_valid_during_from)

        elif travel_valid_during_to is not None and travel_valid_during_from is None:
            queryset = queryset.filter(usage_date_time__lte=travel_valid_during_to)

        elif travel_valid_during_to is not None and travel_valid_during_from is not None:
            queryset = queryset.filter(usage_date_time__range=(travel_valid_during_from, travel_valid_during_to))

        if limit is not None:
            queryset = queryset[:int(limit)]

        if skip is not None:
            queryset = queryset[::int(skip)]
            return queryset

        return prefetch(queryset, self.serializer_class)
