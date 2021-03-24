from customers.models import *
from django.contrib import admin


class LinkedAccountAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('id',)}


admin.site.register(Mode)
admin.site.register(Operator)
admin.site.register(Monetary_Value)
admin.site.register(Transaction)
admin.site.register(AccountBalance)
admin.site.register(Vehicle)
admin.site.register(Ticket)
admin.site.register(LatLong)
admin.site.register(LocationFrom)
admin.site.register(LocationTo)
admin.site.register(Purchase)
admin.site.register(Customer)
admin.site.register(Discount)
admin.site.register(Concession)
admin.site.register(Reference)
admin.site.register(Location)
admin.site.register(TravelLocation)
admin.site.register(Usage)
admin.site.register(Service)
admin.site.register(LinkedAccount, LinkedAccountAdmin)
