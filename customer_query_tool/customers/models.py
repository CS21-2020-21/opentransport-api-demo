from django.db import models
from django.contrib.auth.models import User



class Mode(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    short_desc = models.CharField(max_length=50)
    long_desc = models.TextField()

    def __str__(self):
        return self.short_desc



class Operator(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    modes = models.ManyToManyField(Mode, blank=True)
    homepage = models.URLField()
    api_url = models.URLField()
    default_language = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Monetary_Value(models.Model):
    money_id = models.IntegerField(unique=True, primary_key=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3)


class Transaction(models.Model):
    date_time = models.DateTimeField()
    reference = models.CharField(max_length=4, primary_key=True, unique=True)
    payment_type = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50)
    price = models.ForeignKey(Monetary_Value, related_name="transaction", on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.CharField(primary_key=True, unique=True, max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    


class LinkedAccount(models.Model):
    operator = models.CharField(max_length=50)
    email = models.EmailField()
    customer = models.ForeignKey(Customer, related_name="LinkedAccount", on_delete=models.CASCADE)
    username = models.CharField(max_length=50)


class AccountBalance(models.Model):
    account_id = models.IntegerField(primary_key=True, unique=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3)


class Vehicle(models.Model):
    included = models.CharField(max_length=3)
    reference = models.CharField(max_length=50, primary_key=True, unique=True)
    vehicle_type = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)



class Ticket(models.Model):
    number_usages = models.IntegerField()
    reference = models.CharField(max_length=50, primary_key=True, unique=True)
    reference_type = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)



class LatLong(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    latitude=models.DecimalField(max_digits=8, decimal_places=6)
    longitude=models.DecimalField(max_digits=8, decimal_places=6)


class LocationFrom(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    lat_long = models.ForeignKey(LatLong, related_name="location_from", on_delete=models.CASCADE)
    NaPTAN = models.CharField(max_length=50)
    other = models.CharField(max_length=50)
    other_type = models.CharField(max_length=50)
    accuracy = models.IntegerField()



class LocationTo(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    lat_long = models.ForeignKey(LatLong, related_name="location_to", on_delete=models.CASCADE)
    NaPTAN = models.CharField(max_length=50)
    other = models.CharField(max_length=50)
    other_type = models.CharField(max_length=50)
    accuracy = models.IntegerField()


class Discount(models.Model):
    discount_type = models.CharField(max_length=50)
    discount_value = models.IntegerField()
    discount_description = models.CharField(max_length=50)



class Reference(models.Model):
    reference = models.CharField(max_length=50)
    reference_type = models.CharField(max_length=50)


class Location(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    lat_long = models.ForeignKey(LatLong, related_name="location", on_delete=models.CASCADE)
    NaPTAN = models.CharField(max_length=50)
    other = models.CharField(max_length=50)
    other_type = models.CharField(max_length=50)
    accuracy = models.IntegerField()


class TravelLocation(models.Model):
    location = models.ForeignKey(Location, related_name="travel_location", on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reference = models.CharField(max_length=100)



class Service(models.Model):
    service_type = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    amount =models.DecimalField(max_digits=6, decimal_places=2)
    price = models.ForeignKey(Monetary_Value, related_name="service", on_delete=models.CASCADE)


class Usage(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=100)
    customer = models.ForeignKey(Customer, related_name="usage", on_delete=models.CASCADE)
    mode = models.ForeignKey(Mode, related_name="usage", on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, related_name="usage",on_delete=models.CASCADE)
    reference = models.ForeignKey(Reference, related_name="usage", on_delete=models.CASCADE)
    travel_class = models.CharField(max_length=50)
    travel_from = models.ForeignKey(TravelLocation, related_name="usage_from", on_delete=models.CASCADE)
    travel_to = models.ForeignKey(TravelLocation, related_name="usage_to", on_delete=models.CASCADE)
    purchase_id = models.CharField(max_length=50)
    usage_date_time = models.DateTimeField()
    route_via_avoid = models.CharField(max_length=50)
    ticket = models.ForeignKey(Ticket, related_name="usage", on_delete=models.CASCADE)
    pre_paid = models.BooleanField()
    price = models.ForeignKey(Monetary_Value, related_name="usage", on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, related_name="usage")


class Concession(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=100)
    customer = models.ForeignKey(Customer, related_name="concession", on_delete=models.CASCADE)
    mode = models.ForeignKey(Mode, related_name="concession", on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, related_name="concession",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.ForeignKey(Monetary_Value, related_name="concession", on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, related_name="concession", on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, related_name="concession",on_delete=models.CASCADE)
    valid_from_date_time = models.DateTimeField()
    valid_to_date_time = models.DateTimeField()
    conditions = models.CharField(max_length=100)
    

class Purchase(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=100)
    customer = models.ForeignKey(Customer, related_name="purchase", on_delete=models.CASCADE)
    mode = models.ForeignKey(Mode, related_name="purchase", on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, related_name="purchase",on_delete=models.CASCADE)
    travel_class = models.CharField(max_length=50)
    booking_date_time = models.DateTimeField()
    transaction = models.ForeignKey(Transaction, related_name="purchase",on_delete=models.CASCADE)
    account_balance = models.ForeignKey(AccountBalance, related_name="purchase",on_delete=models.CASCADE)
    agent = models.CharField(max_length=50)
    passenger_number = models.IntegerField()
    passenger_type = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Vehicle, related_name="purchase",on_delete=models.CASCADE)
    route = models.CharField(max_length=100)
    travel_from_date_time = models.DateTimeField()
    travel_to_date_time = models.DateTimeField()
    conditions = models.CharField(max_length=50)
    concession = models.CharField(max_length=50)
    restrictions = models.CharField(max_length=50)
    ticket = models.ForeignKey(Ticket, related_name="purchase",on_delete=models.CASCADE)
    location_from = models.ForeignKey(LocationFrom, related_name="purchase",on_delete=models.CASCADE)
    location_to = models.ForeignKey(LocationTo, related_name="purchase",on_delete=models.CASCADE)
    reserved_position = models.CharField(max_length=50)
    service_request = models.CharField(max_length=100)