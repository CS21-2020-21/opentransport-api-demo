from django.shortcuts import render
#from .models import Mode, Operator, Monetary_Value, Transaction, Customer, AccountBalance, Vehicle, Ticket, LatLong, LocationFrom, LocationTo, Purchase, Discount, Concession
from rest_framework import routers, serializers, viewsets
#from .serializers import ModeSerializer, OperatorSerializer, Monetary_ValueSerializer, TransactionSerializer, AccountBalanceSerializer, VehicleSerializer, TicketSerializer, LatLongSerializer, LocationFromSerializer, LocationToSerializer, PurchaseSerializer, CustomerSerializer, DiscountSerializer, ConcessionSerializer
# from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TravelFromViewSet(viewsets.ModelViewSet):
    queryset = TravelLocation.objects.all()
    serializer_class = TravelLocationSerializer

class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class Monetary_ValueViewSet(viewsets.ModelViewSet):
    queryset = Monetary_Value.objects.all()
    serializer_class = Monetary_ValueSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



class AccountBalanceViewSet(viewsets.ModelViewSet):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class LatLongViewSet(viewsets.ModelViewSet):
    queryset = LatLong.objects.all()
    serializer_class = LatLongSerializer

class LocationFromViewSet(viewsets.ModelViewSet):
    queryset = LocationFrom.objects.all()
    serializer_class = LocationFromSerializer

class LocationToViewSet(viewsets.ModelViewSet):
    queryset = LocationTo.objects.all()
    serializer_class = LocationToSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    
    # permission_classes = (IsAuthenticated,)
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


        #sort out travel dates
        

        return queryset

class ConcessionViewSet(viewsets.ModelViewSet):
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

class UsageViewSet(viewsets.ModelViewSet):
    
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
        
