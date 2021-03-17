from customers.models import *
from rest_framework import serializers


class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = ('id', 'short_desc', 'long_desc')


class OperatorSerializer(serializers.ModelSerializer):
    modes = ModeSerializer(many=True, read_only=True)

    class Meta:
        model = Operator
        fields = ('id', 'name', 'modes', 'homepage', 'api_url', 'default_language', 'phone', 'email')


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('discount_type', 'discount_value', 'discount_description')


class Monetary_ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monetary_Value
        fields = ('amount', 'currency')


class TransactionSerializer(serializers.ModelSerializer):
    price = Monetary_ValueSerializer(many=False, read_only=True)

    class Meta:
        model = Transaction
        fields = ('date_time', 'reference', 'payment_type', 'payment_method', 'price')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('included', 'reference', 'vehicle_type', 'condition')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'name', 'email')


class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBalance
        fields = ('amount', 'currency')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('number_usages', 'reference', 'reference_type', 'medium')


class LatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLong
        fields = ('latitude', 'longitude')


class LocationSerializer(serializers.ModelSerializer):
    lat_long = LatLongSerializer(many=False, read_only=True)

    class Meta:
        model = Location
        fields = ('lat_long', 'NaPTAN', 'other', 'other_type', 'accuracy')


class TravelLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False, read_only=True)

    class Meta:
        model = TravelLocation
        fields = ('location', 'date_time', 'reference')


class LocationFromSerializer(serializers.ModelSerializer):
    lat_long = LatLongSerializer(many=False, read_only=True)

    class Meta:
        model = LocationFrom
        fields = ('lat_long', 'NaPTAN', 'other', 'other_type', 'accuracy')


class LocationToSerializer(serializers.ModelSerializer):
    lat_long = LatLongSerializer(many=False, read_only=True)

    class Meta:
        model = LocationTo
        fields = ('lat_long', 'NaPTAN', 'other', 'other_type', 'accuracy')


class ServiceSerializer(serializers.ModelSerializer):
    price = Monetary_ValueSerializer(many=False, read_only=True)

    class Meta:
        model = Service
        fields = ('service_type', 'unit', 'amount', 'price')


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ('reference', 'reference_type')


class UsageSerializer(serializers.ModelSerializer):
    mode = ModeSerializer(many=False, read_only=True)
    operator = OperatorSerializer(many=False, read_only=True)
    reference = ReferenceSerializer(many=False, read_only=True)
    travel_from = TravelLocationSerializer(many=False, read_only=True)
    travel_to = TravelLocationSerializer(many=False, read_only=True)
    ticket = TicketSerializer(many=False, read_only=True)
    price = Monetary_ValueSerializer(many=False, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Usage
        fields = ('id', 'mode', 'operator', 'reference', 'travel_class', 'travel_from', 'travel_to', 'purchase_id',
                  'route_via_avoid', 'ticket', 'pre_paid', 'price', 'services')


class PurchaseSerializer(serializers.ModelSerializer):
    mode = ModeSerializer(many=False, read_only=True)
    operator = OperatorSerializer(many=False, read_only=True)
    transaction = TransactionSerializer(many=False, read_only=True)
    account_balance = AccountBalanceSerializer(many=False, read_only=True)
    vehicle = VehicleSerializer(many=False, read_only=True)
    ticket = TicketSerializer(many=False, read_only=True)
    location_from = LocationFromSerializer(many=False, read_only=True)
    location_to = LocationToSerializer(many=False, read_only=True)
    
    class Meta:
        model = Purchase
        fields = ('id', 'mode', 'operator', 'travel_class',
                  'booking_date_time', 'transaction', 'account_balance',
                  'agent', 'passenger_number', 'passenger_type',
                  'vehicle', 'route', 'travel_from_date_time',
                  'travel_to_date_time', 'conditions', 'concession',
                  'restrictions', 'ticket', 'location_from',
                  'location_to', 'reserved_position', 'service_request')


class ConcessionSerializer(serializers.ModelSerializer):
    mode = ModeSerializer(many=False, read_only=True)
    operator = OperatorSerializer(many=False, read_only=True)
    transaction = TransactionSerializer(many=False, read_only=True)
    price = Monetary_ValueSerializer(many=False, read_only=True)
    discount = DiscountSerializer(many=False, read_only=True)

    class Meta:
        model = Concession
        fields = ('id', 'mode', 'operator', 'name', 'price', 'discount', 'transaction',
                  'valid_from_date_time', 'valid_to_date_time', 'conditions')
