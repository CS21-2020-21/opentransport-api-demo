import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customer_query_tool.settings')

import django
django.setup()
from customers.models import *

import datetime

def populate():
    modes = [{"id": "007", "short_desc": "bus", "long_desc": "includes any vehicle typically greater than 8 seats.. such as a mini bus"},
            ]

    
    for mode in modes:
        add_mode(mode)

    operators = [{'id':'029', 'name':'PSD Buses','homepage':'www.psdbuses.com', 'api_url':'www.psdbuses.pythonanywhere.com', 
                'default_language':'en', 'phone':'0141523678', 'email':'psdbuses@gmail.com' },
                 ]

    for operator in operators:
        add_operator(operator)

    money = [{'id':1, 'amount':2.15, 'currency':'GBP'},
            {'id':2, 'amount':3.90, 'currency':'GBP'},
            {'id':3, 'amount':8.70, 'currency':'USD'},
            {'id':4, 'amount':4.20, 'currency':'GBP'},
            {'id':5, 'amount':1.99, 'currency':'HKD'},
            {'id':6, 'amount':0.50, 'currency':'GBP'},
            ]

    for value in money:
        add_money(value)

    
    customers = [{'user': User.objects.create_user('1', "palin@gmail.com", '12345678abc'), 'id':1, 'name':'Michael Palin', 'email':'palin@gmail.com'},
                {'user':User.objects.create_user('2', 'columbus@gmail.com', '12345678abc'), 'id':2, 'name':'Christopher Columbus', 'email':'columbus@gmail.com'},
                {'user':User.objects.create_user('3', 'da@hotmail.com', '12345678abc'), 'id':3, 'name':'David Attenborough', 'email':'da@hotmail.com'},
                {'user':User.objects.create_user('4', 'bear@yahoo.com', '12345678abc'), 'id':4, 'name':'Bear Grylls', 'email':'bear@yahoo.com'},
                {'user':User.objects.create_user('5', 'peake@gmail.com', '12345678abc'), 'id':5, 'name':'Tim Peake', 'email':'peake@gmail.com'},
                ]

    
    for customer in customers:
        add_customer(customer)


    accounts = [{'id':1, 'amount':0.15, 'currency':'GBP'},
            {'id':2, 'amount':4.87, 'currency':'GBP'},
            {'id':3, 'amount':9.10, 'currency':'USD'},
            {'id':4, 'amount':13.20, 'currency':'GBP'},
            {'id':5, 'amount':45.67, 'currency':'HKD'},
            {'id':6, 'amount':0.23, 'currency':'GBP'},
            ]

    for account in accounts:
        add_balance(account)

    vehicles = [{'included':'yes', 'reference':'BA20 FGD', 'vehicle_type':'bus', 'condition':'brand new' },
                {'included':'no', 'reference':'GH56 TCF', 'vehicle_type':'bus', 'condition':'old' },
                {'included':'yes', 'reference':'DR19 JKD', 'vehicle_type':'bus', 'condition':'nearly new' },
                {'included':'no', 'reference':'JL12 UTY', 'vehicle_type':'bus', 'condition':'rusty and needing repairs' },
                {'included':'yes', 'reference':'RD20 OIP', 'vehicle_type':'bus', 'condition':'brand new' },
            ]

    for vehicle in vehicles:
        add_vehicle(vehicle)


    transactions = [{'date_time':'2021-01-05T11:33:11Z', 'reference':'123', 'payment_type':'Card', 'payment_method':'visa', 'price':Monetary_Value.objects.get(money_id=2)},
                    {'date_time':'2020-04-02T11:33:11Z', 'reference':'432', 'payment_type':'Card', 'payment_method':'mastercard', 'price':Monetary_Value.objects.get(money_id=3)},
                    {'date_time':'2021-01-02T11:33:11Z', 'reference':'321', 'payment_type':'Card', 'payment_method':'visa', 'price':Monetary_Value.objects.get(money_id=4)},
                    {'date_time':'2021-01-01T11:33:11Z', 'reference':'745', 'payment_type':'Card', 'payment_method':'visa', 'price':Monetary_Value.objects.get(money_id=3)},
                    {'date_time':'2020-11-10T11:33:11Z', 'reference':'231', 'payment_type':'Card', 'payment_method':'visa', 'price':Monetary_Value.objects.get(money_id=2)},
                    {'date_time':'2020-12-20T11:33:11Z', 'reference':'986', 'payment_type':'Card', 'payment_method':'visa', 'price':Monetary_Value.objects.get(money_id=1)},
                   ]

    for transaction in transactions:
        add_transaction(transaction)


    tickets = [{'number_usages':3, 'reference':'1234D', 'reference_type':'ticket ref', 'medium':'paypal'},
                {'number_usages':2, 'reference':'1334D', 'reference_type':'ticket ref', 'medium':'card'},
                {'number_usages':6, 'reference':'1134D', 'reference_type':'ticket ref', 'medium':'card'},
                {'number_usages':1, 'reference':'1534D', 'reference_type':'ticket ref', 'medium':'cash'},
                {'number_usages':2, 'reference':'1834D', 'reference_type':'ticket ref', 'medium':'cash'},
            ]

    for ticket in tickets:
        add_ticket(ticket)


    latlongs = [{'id':1, 'latitude':'2.132435', 'longitude':'3.532897'},
                {'id':2, 'latitude':'4.132435', 'longitude':'72.532897'},
                {'id':3, 'latitude':'13.132435', 'longitude':'94.532897'},
                {'id':4, 'latitude':'1.132435', 'longitude':'2.532897'},
                {'id':5, 'latitude':'27.132435', 'longitude':'73.532897'},
                ]

    for latlong in latlongs:
        add_latlong(latlong)


    locfroms = [{'id':1, 'lat_long':LatLong.objects.get(id=2), 'NaPTAN':'9100GLGC', 'other':'lots of buses', 'other_type':'buses', 'accuracy':9},
                {'id':2, 'lat_long':LatLong.objects.get(id=1), 'NaPTAN':'9100GLGF', 'other':'lots of cars', 'other_type':'cars', 'accuracy':6},
                {'id':3, 'lat_long':LatLong.objects.get(id=3), 'NaPTAN':'9100GLGD', 'other':'lots of trains', 'other_type':'trains', 'accuracy':3},
                {'id':4, 'lat_long':LatLong.objects.get(id=5), 'NaPTAN':'9100GLGS', 'other':'lots of trucks', 'other_type':'trucks', 'accuracy':99},
                {'id':5, 'lat_long':LatLong.objects.get(id=4), 'NaPTAN':'9100GLGJ', 'other':'lots of lorries', 'other_type':'lorries', 'accuracy':2},
                ]
        
    for loc in locfroms:
        add_loc_from(loc)

    loctos = [{'id':1, 'lat_long':LatLong.objects.get(id=2), 'NaPTAN':'9100GLGC', 'other':'lots of buses', 'other_type':'buses', 'accuracy':9},
                {'id':2, 'lat_long':LatLong.objects.get(id=1), 'NaPTAN':'9100GLGF', 'other':'lots of cars', 'other_type':'cars', 'accuracy':6},
                {'id':3, 'lat_long':LatLong.objects.get(id=3), 'NaPTAN':'9100GLGD', 'other':'lots of trains', 'other_type':'trains', 'accuracy':3},
                {'id':4, 'lat_long':LatLong.objects.get(id=5), 'NaPTAN':'9100GLGS', 'other':'lots of trucks', 'other_type':'trucks', 'accuracy':99},
                {'id':5, 'lat_long':LatLong.objects.get(id=4), 'NaPTAN':'9100GLGJ', 'other':'lots of lorries', 'other_type':'lorries', 'accuracy':2},
                ]

    for loc in loctos:
        add_loc_to(loc)

    discounts = [{'discount_type':'%', 'discount_value':10, 'discount_description':'friends and family'},
                    {'discount_type':'%', 'discount_value':20, 'discount_description':'summer sale'},
                    {'discount_type':'%', 'discount_value':20, 'discount_description':'winter sale'},
                    {'discount_type':'%', 'discount_value':30, 'discount_description':'spring sale'},
                    {'discount_type':'%', 'discount_value':50, 'discount_description':'autumn sale'},
                ]

    for discount in discounts:
        add_discount(discount)

    references = [{'reference':'2b', 'reference_type':'seat'},
                {'reference':'3c', 'reference_type':'seat'},
                {'reference':'2d', 'reference_type':'seat'},
                {'reference':'1e', 'reference_type':'seat'},
                {'reference':'6d', 'reference_type':'seat'},
                ]

    for reference in references:
        add_reference(reference)


    locations= [{'id':1, 'lat_long':LatLong.objects.get(id=2), 'NaPTAN':'9100GLGC', 'other':'lots of buses', 'other_type':'buses', 'accuracy':9},
                {'id':2, 'lat_long':LatLong.objects.get(id=1), 'NaPTAN':'9100GLGF', 'other':'lots of cars', 'other_type':'cars', 'accuracy':6},
                {'id':3, 'lat_long':LatLong.objects.get(id=3), 'NaPTAN':'9100GLGD', 'other':'lots of trains', 'other_type':'trains', 'accuracy':3},
                {'id':4, 'lat_long':LatLong.objects.get(id=5), 'NaPTAN':'9100GLGS', 'other':'lots of trucks', 'other_type':'trucks', 'accuracy':99},
                {'id':5, 'lat_long':LatLong.objects.get(id=4), 'NaPTAN':'9100GLGJ', 'other':'lots of lorries', 'other_type':'lorries', 'accuracy':2},
                ]

    for location in locations:
        add_location(location)


    travel_locations = [{'location':Location.objects.get(id=1), 'date_time':'2020-01-07T11:33:11Z', 'reference':'123'},
                        {'location':Location.objects.get(id=2), 'date_time':'2021-01-07T11:33:11Z', 'reference':'124'},
                        {'location':Location.objects.get(id=3), 'date_time':'2021-01-03T11:33:11Z', 'reference':'125'},
                        {'location':Location.objects.get(id=4), 'date_time':'2020-12-14T11:33:11Z', 'reference':'126'},
                        {'location':Location.objects.get(id=5), 'date_time':'2020-11-07T11:33:11Z', 'reference':'127'},
                    ]

    for location in travel_locations:
        add_travel_location(location)

    
    services = [{'service_type':'charging', 'unit':'kwH', 'amount':20.0, 'price':Monetary_Value.objects.get(money_id=2)},
                {'service_type':'meal', 'unit':'calories', 'amount':300.0, 'price':Monetary_Value.objects.get(money_id=4)},
                ]

    for service in services:
        add_service(service)


    usages = [{'id':'123', 'customer':Customer.objects.get(customer_id=1), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=1),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='123'),
                'travel_to':TravelLocation.objects.get(reference=127), 'purchase_id':'C3112', 
                'usage_date_time':'2020-11-07T11:33:11Z', 'route_via_avoid':'avoid bridge',
                'ticket':Ticket.objects.get(reference='1134D'), 'pre_paid':True, 
                'price':Monetary_Value.objects.get(money_id=3)},


                {'id':'124', 'customer':Customer.objects.get(customer_id=1), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=2),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='127'),
                'travel_to':TravelLocation.objects.get(reference=123), 'purchase_id':'C3135', 
                'usage_date_time':'2020-12-16T11:33:11Z', 'route_via_avoid':'avoid one way road',
                'ticket':Ticket.objects.get(reference='1834D'), 'pre_paid':False, 
                'price':Monetary_Value.objects.get(money_id=1)},

                {'id':'125', 'customer':Customer.objects.get(customer_id=2), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=5),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='123'),
                'travel_to':TravelLocation.objects.get(reference=127), 'purchase_id':'C3112', 
                'usage_date_time':'2020-11-07T11:33:11Z', 'route_via_avoid':'avoid bridge',
                'ticket':Ticket.objects.get(reference='1134D'), 'pre_paid':True, 
                'price':Monetary_Value.objects.get(money_id=6)},


                {'id':'126', 'customer':Customer.objects.get(customer_id=2), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=4),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='127'),
                'travel_to':TravelLocation.objects.get(reference=123), 'purchase_id':'C3135', 
                'usage_date_time':'2020-12-16T11:33:11Z', 'route_via_avoid':'avoid one way road',
                'ticket':Ticket.objects.get(reference='1834D'), 'pre_paid':False, 
                'price':Monetary_Value.objects.get(money_id=2)},
    
                {'id':'127', 'customer':Customer.objects.get(customer_id=3), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=2),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='127'),
                'travel_to':TravelLocation.objects.get(reference=123), 'purchase_id':'C3135', 
                'usage_date_time':'2020-12-16T11:33:11Z', 'route_via_avoid':'avoid one way road',
                'ticket':Ticket.objects.get(reference='1834D'), 'pre_paid':False, 
                'price':Monetary_Value.objects.get(money_id=4)},

                {'id':'128', 'customer':Customer.objects.get(customer_id=4), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=2),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='127'),
                'travel_to':TravelLocation.objects.get(reference=123), 'purchase_id':'C3135', 
                'usage_date_time':'2020-12-16T11:33:11Z', 'route_via_avoid':'avoid one way road',
                'ticket':Ticket.objects.get(reference='1834D'), 'pre_paid':False, 
                'price':Monetary_Value.objects.get(money_id=1)},

                {'id':'129', 'customer':Customer.objects.get(customer_id=5), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=1),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='127'),
                'travel_to':TravelLocation.objects.get(reference=123), 'purchase_id':'C3135', 
                'usage_date_time':'2020-12-16T11:33:11Z', 'route_via_avoid':'avoid one way road',
                'ticket':Ticket.objects.get(reference='1834D'), 'pre_paid':False, 
                'price':Monetary_Value.objects.get(money_id=5)},

                {'id':'130', 'customer':Customer.objects.get(customer_id=5), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=2),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='127'),
                'travel_to':TravelLocation.objects.get(reference=123), 'purchase_id':'C3135', 
                'usage_date_time':'2020-12-16T11:33:11Z', 'route_via_avoid':'avoid one way road',
                'ticket':Ticket.objects.get(reference='1834D'), 'pre_paid':False, 
                'price':Monetary_Value.objects.get(money_id=4)},

                {'id':'131', 'customer':Customer.objects.get(customer_id=5), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=3),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='127'),
                'travel_to':TravelLocation.objects.get(reference=123), 'purchase_id':'C3135', 
                'usage_date_time':'2020-12-16T11:33:11Z', 'route_via_avoid':'avoid one way road',
                'ticket':Ticket.objects.get(reference='1834D'), 'pre_paid':False, 
                'price':Monetary_Value.objects.get(money_id=3)},

                {'id':'132', 'customer':Customer.objects.get(customer_id=5), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'reference':Reference.objects.get(id=1),
                'travel_class':'first', 'travel_from':TravelLocation.objects.get(reference='127'),
                'travel_to':TravelLocation.objects.get(reference=123), 'purchase_id':'C3135', 
                'usage_date_time':'2020-12-16T11:33:11Z', 'route_via_avoid':'avoid one way road',
                'ticket':Ticket.objects.get(reference='1834D'), 'pre_paid':False, 
                'price':Monetary_Value.objects.get(money_id=4)},
    
            ]


    for usage in usages:
        add_usage(usage)


    concessions = [{'id':'124', 'customer':Customer.objects.get(customer_id=1), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'name':'family concession', 'price':Monetary_Value.objects.get(money_id=1),
                'discount':Discount.objects.get(discount_description='spring sale'), 'transaction':Transaction.objects.get(reference='231'),
                'valid_from_date_time':'2021-01-16T11:33:11Z', 'valid_to_date_time':'2021-04-17T11:33:11Z',
                'conditions':'not valid weekends'
                },

                {'id':'156', 'customer':Customer.objects.get(customer_id=1), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'name':'winter sale card', 'price':Monetary_Value.objects.get(money_id=3),
                'discount':Discount.objects.get(discount_description='winter sale'), 'transaction':Transaction.objects.get(reference='745'),
                'valid_from_date_time':'2021-10-16T11:33:11Z', 'valid_to_date_time':'2022-02-17T11:33:11Z',
                'conditions':'valid all the time'
                },

                {'id':'194', 'customer':Customer.objects.get(customer_id=1), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'name':'summer sale card', 'price':Monetary_Value.objects.get(money_id=4),
                'discount':Discount.objects.get(discount_description='summer sale'), 'transaction':Transaction.objects.get(reference='123'),
                'valid_from_date_time':'2021-06-16T11:33:11Z', 'valid_to_date_time':'2021-08-17T11:33:11Z',
                'conditions':'not valid weekends'
                },

                {'id':'195', 'customer':Customer.objects.get(customer_id=2), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'name':'summer sale card', 'price':Monetary_Value.objects.get(money_id=4),
                'discount':Discount.objects.get(discount_description='summer sale'), 'transaction':Transaction.objects.get(reference='123'),
                'valid_from_date_time':'2021-06-19T11:33:11Z', 'valid_to_date_time':'2021-08-20T11:33:11Z',
                'conditions':'not valid weekends'
                },

                {'id':'196', 'customer':Customer.objects.get(customer_id=3), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'name':'winter sale card', 'price':Monetary_Value.objects.get(money_id=3),
                'discount':Discount.objects.get(discount_description='winter sale'), 'transaction':Transaction.objects.get(reference='745'),
                'valid_from_date_time':'2022-10-16T11:33:11Z', 'valid_to_date_time':'2023-02-17T11:33:11Z',
                'conditions':'valid all the time'
                },

                {'id':'197', 'customer':Customer.objects.get(customer_id=4), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'name':'winter sale card', 'price':Monetary_Value.objects.get(money_id=3),
                'discount':Discount.objects.get(discount_description='winter sale'), 'transaction':Transaction.objects.get(reference='745'),
                'valid_from_date_time':'2021-10-16T11:33:11Z', 'valid_to_date_time':'2022-02-17T11:33:11Z',
                'conditions':'valid all the time'
                },

                {'id':'198', 'customer':Customer.objects.get(customer_id=5), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'name':'winter sale card', 'price':Monetary_Value.objects.get(money_id=3),
                'discount':Discount.objects.get(discount_description='winter sale'), 'transaction':Transaction.objects.get(reference='745'),
                'valid_from_date_time':'2021-10-16T11:33:11Z', 'valid_to_date_time':'2022-02-17T11:33:11Z',
                'conditions':'valid all the time'
                },

                {'id':'199', 'customer':Customer.objects.get(customer_id=5), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 'name':'family concession', 'price':Monetary_Value.objects.get(money_id=1),
                'discount':Discount.objects.get(discount_description='spring sale'), 'transaction':Transaction.objects.get(reference='231'),
                'valid_from_date_time':'2021-01-16T11:33:11Z', 'valid_to_date_time':'2021-04-17T11:33:11Z',
                'conditions':'not valid weekends'
                },
                ]

    for concession in concessions:
        add_concession(concession)


    purchases = [{'id':'983', 'customer':Customer.objects.get(customer_id=1), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 
                'travel_class':'coach', 'booking_date_time':'2020-12-07T11:33:11Z', 'transaction':Transaction.objects.get(reference='432'),
                'account_balance':AccountBalance.objects.get(account_id=6), 'agent':'PSB Buses', 
                'passenger_number':2, 'passenger_type':'two adults', 'vehicle':Vehicle.objects.get(reference='BA20 FGD'),
                'route':'scenic route', 'travel_from_date_time':'2020-12-07T11:33:11Z', 'travel_to_date_time':'2020-12-08T11:33:11Z',
                'conditions':'peak time', 'concession':'family saving card', 'restrictions':'off peak only',
                'ticket':Ticket.objects.get(reference='1534D'), 'location_from':LocationFrom.objects.get(id=3),
                'location_to':LocationTo.objects.get(id=4), 'reserved_position':'3D', 'service_request':'nothing'},     

                {'id':'678', 'customer':Customer.objects.get(customer_id=1), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 
                'travel_class':'first', 'booking_date_time':'2021-01-07T11:33:11Z', 'transaction':Transaction.objects.get(reference='432'),
                'account_balance':AccountBalance.objects.get(account_id=2), 'agent':'PSD Buses', 
                'passenger_number':3, 'passenger_type':'two adults, one child', 'vehicle':Vehicle.objects.get(reference='GH56 TCF'),
                'route':'scenic route', 'travel_from_date_time':'2021-12-07T11:33:11Z', 'travel_to_date_time':'2021-12-08T11:33:11Z',
                'conditions':'peak time', 'concession':'family saving card', 'restrictions':'off peak only',
                'ticket':Ticket.objects.get(reference='1334D'), 'location_from':LocationFrom.objects.get(id=2),
                'location_to':LocationTo.objects.get(id=1), 'reserved_position':'3F', 'service_request':'food'},  

                {'id':'681', 'customer':Customer.objects.get(customer_id=1), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 
                'travel_class':'first', 'booking_date_time':'2020-01-07T11:33:11Z', 'transaction':Transaction.objects.get(reference='986'),
                'account_balance':AccountBalance.objects.get(account_id=5), 'agent':'PSD Buses', 
                'passenger_number':1, 'passenger_type':'one adult', 'vehicle':Vehicle.objects.get(reference='DR19 JKD'),
                'route':'fast route', 'travel_from_date_time':'2021-10-27T11:33:11Z', 'travel_to_date_time':'2021-11-08T11:33:11Z',
                'conditions':'peak time', 'concession':'none', 'restrictions':'off peak only',
                'ticket':Ticket.objects.get(reference='1234D'), 'location_from':LocationFrom.objects.get(id=1),
                'location_to':LocationTo.objects.get(id=3), 'reserved_position':'1A', 'service_request':'charging'},  

                 {'id':'534', 'customer':Customer.objects.get(customer_id=2), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 
                'travel_class':'first', 'booking_date_time':'2020-01-07T11:33:11Z', 'transaction':Transaction.objects.get(reference='986'),
                'account_balance':AccountBalance.objects.get(account_id=5), 'agent':'PSD Buses', 
                'passenger_number':1, 'passenger_type':'one adult', 'vehicle':Vehicle.objects.get(reference='JL12 UTY'),
                'route':'fast route', 'travel_from_date_time':'2021-10-27T11:33:11Z', 'travel_to_date_time':'2021-11-08T11:33:11Z',
                'conditions':'peak time', 'concession':'none', 'restrictions':'off peak only',
                'ticket':Ticket.objects.get(reference='1234D'), 'location_from':LocationFrom.objects.get(id=1),
                'location_to':LocationTo.objects.get(id=3), 'reserved_position':'1A', 'service_request':'charging'},   

                 {'id':'535', 'customer':Customer.objects.get(customer_id=2), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 
                'travel_class':'first', 'booking_date_time':'2020-01-07T11:33:11Z', 'transaction':Transaction.objects.get(reference='986'),
                'account_balance':AccountBalance.objects.get(account_id=5), 'agent':'PSD Buses', 
                'passenger_number':1, 'passenger_type':'one adult', 'vehicle':Vehicle.objects.get(reference='RD20 OIP'),
                'route':'fast route', 'travel_from_date_time':'2021-10-27T11:33:11Z', 'travel_to_date_time':'2021-11-08T11:33:11Z',
                'conditions':'peak time', 'concession':'none', 'restrictions':'off peak only',
                'ticket':Ticket.objects.get(reference='1234D'), 'location_from':LocationFrom.objects.get(id=1),
                'location_to':LocationTo.objects.get(id=3), 'reserved_position':'1A', 'service_request':'charging'},    

                 {'id':'536', 'customer':Customer.objects.get(customer_id=3), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 
                'travel_class':'first', 'booking_date_time':'2021-01-07T11:33:11Z', 'transaction':Transaction.objects.get(reference='432'),
                'account_balance':AccountBalance.objects.get(account_id=2), 'agent':'PSD Buses', 
                'passenger_number':3, 'passenger_type':'two adults, one child', 'vehicle':Vehicle.objects.get(reference='GH56 TCF'),
                'route':'scenic route', 'travel_from_date_time':'2021-12-07T11:33:11Z', 'travel_to_date_time':'2021-12-08T11:33:11Z',
                'conditions':'peak time', 'concession':'family saving card', 'restrictions':'off peak only',
                'ticket':Ticket.objects.get(reference='1334D'), 'location_from':LocationFrom.objects.get(id=2),
                'location_to':LocationTo.objects.get(id=1), 'reserved_position':'3F', 'service_request':'food'},  
                     
                {'id':'537', 'customer':Customer.objects.get(customer_id=4), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 
                'travel_class':'coach', 'booking_date_time':'2020-12-07T11:33:11Z', 'transaction':Transaction.objects.get(reference='432'),
                'account_balance':AccountBalance.objects.get(account_id=6), 'agent':'PSB Buses', 
                'passenger_number':2, 'passenger_type':'two adults', 'vehicle':Vehicle.objects.get(reference='BA20 FGD'),
                'route':'scenic route', 'travel_from_date_time':'2020-12-07T11:33:11Z', 'travel_to_date_time':'2020-12-08T11:33:11Z',
                'conditions':'peak time', 'concession':'family saving card', 'restrictions':'off peak only',
                'ticket':Ticket.objects.get(reference='1534D'), 'location_from':LocationFrom.objects.get(id=3),
                'location_to':LocationTo.objects.get(id=4), 'reserved_position':'3D', 'service_request':'food'},  

                {'id':'538', 'customer':Customer.objects.get(customer_id=5), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 
                'travel_class':'coach', 'booking_date_time':'2020-12-07T11:33:11Z', 'transaction':Transaction.objects.get(reference='432'),
                'account_balance':AccountBalance.objects.get(account_id=6), 'agent':'PSB Buses', 
                'passenger_number':2, 'passenger_type':'two adults', 'vehicle':Vehicle.objects.get(reference='BA20 FGD'),
                'route':'scenic route', 'travel_from_date_time':'2020-12-07T11:33:11Z', 'travel_to_date_time':'2020-12-08T11:33:11Z',
                'conditions':'peak time', 'concession':'family saving card', 'restrictions':'off peak only',
                'ticket':Ticket.objects.get(reference='1534D'), 'location_from':LocationFrom.objects.get(id=3),
                'location_to':LocationTo.objects.get(id=4), 'reserved_position':'3D', 'service_request':'nothing'},  

                {'id':'539', 'customer':Customer.objects.get(customer_id=5), 'mode':Mode.objects.get(id='007'), 
                'operator':Operator.objects.get(id='029'), 
                'travel_class':'first', 'booking_date_time':'2021-01-07T11:33:11Z', 'transaction':Transaction.objects.get(reference='432'),
                'account_balance':AccountBalance.objects.get(account_id=2), 'agent':'PSD Buses', 
                'passenger_number':3, 'passenger_type':'two adults, one child', 'vehicle':Vehicle.objects.get(reference='GH56 TCF'),
                'route':'scenic route', 'travel_from_date_time':'2021-12-07T11:33:11Z', 'travel_to_date_time':'2021-12-08T11:33:11Z',
                'conditions':'peak time', 'concession':'family saving card', 'restrictions':'off peak only',
                'ticket':Ticket.objects.get(reference='1334D'), 'location_from':LocationFrom.objects.get(id=2),
                'location_to':LocationTo.objects.get(id=1), 'reserved_position':'3F', 'service_request':'food'}, 
                
                ]

    for purchase in purchases:
        add_purchase(purchase)




def add_mode(mode_data):
    mode = Mode.objects.get_or_create(id=mode_data['id'], short_desc=mode_data['short_desc'], long_desc=mode_data['long_desc'])[0]
    mode.save()
    return mode

def add_operator(operator):
    op = Operator.objects.get_or_create(id=operator['id'], name=operator['name'], homepage=operator['homepage'], api_url=operator['api_url'], default_language=operator['default_language'], phone=operator['phone'], email=operator['email'])[0]
    op.save()
    return op

def add_money(value):
    money = Monetary_Value.objects.get_or_create(money_id=value['id'], amount=value['amount'], currency=value['currency'])[0]
    money.save()
    return money

def add_customer(customer):
    person = Customer.objects.get_or_create(user=customer['user'], customer_id=customer['id'], name=customer['name'], email=customer['email'])[0]
    person.save()
    return person


def add_balance(balance):
    account_balance = AccountBalance.objects.get_or_create(account_id=balance['id'], amount=balance['amount'], currency=balance['currency'])[0]
    account_balance.save()
    return account_balance


def add_vehicle(vehicle):
    transport_vehicle = Vehicle.objects.get_or_create(included=vehicle['included'], reference=vehicle['reference'], vehicle_type=vehicle['vehicle_type'], condition=vehicle['condition'])[0]

    transport_vehicle.save()
    return transport_vehicle

def add_transaction(transaction):
    transact = Transaction.objects.get_or_create(date_time=transaction['date_time'], reference=transaction['reference'], payment_type=transaction['payment_type'], payment_method=transaction['payment_method'], price=transaction['price'])[0]
    transact.save()
    return transact

def add_ticket(ticket):
    tick = Ticket.objects.get_or_create(number_usages=ticket['number_usages'], reference=ticket['reference'], reference_type=ticket['reference_type'], medium=ticket['medium'])[0]
    tick.save()
    return tick

def add_latlong(latlong):
    location = LatLong.objects.get_or_create(id=latlong['id'], latitude=latlong['latitude'], longitude=latlong['longitude'])[0]
    location.save()
    return location

def add_loc_from(loc):
    location = LocationFrom.objects.get_or_create(id=loc['id'], lat_long=loc['lat_long'], NaPTAN=loc['NaPTAN'], other=loc['other'], other_type=loc['other_type'], accuracy=loc['accuracy'])[0]
    location.save()
    return location

def add_loc_to(loc):
    location = LocationTo.objects.get_or_create(id=loc['id'], lat_long=loc['lat_long'], NaPTAN=loc['NaPTAN'], other=loc['other'], other_type=loc['other_type'], accuracy=loc['accuracy'])[0]
    location.save()
    return location

def add_discount(discount):
    discount_details = Discount.objects.get_or_create(discount_type=discount['discount_type'], discount_value=discount['discount_value'], discount_description=discount['discount_description'])[0]
    discount_details.save()
    return discount_details

def add_reference(ref):
    reference = Reference.objects.get_or_create(reference=ref['reference'], reference_type=ref['reference_type'])[0]
    reference.save()
    return reference

def add_location(loc):
    location = Location.objects.get_or_create(id=loc['id'], lat_long=loc['lat_long'], NaPTAN=loc['NaPTAN'], other=loc['other'], other_type=loc['other_type'], accuracy=loc['accuracy'])[0]
    location.save()
    return location

def add_travel_location(loc):
    location = TravelLocation.objects.get_or_create(location=loc['location'], date_time=loc['date_time'], reference=loc['reference'])[0]
    location.save()
    return location

def add_service(ser):
    service = Service.objects.get_or_create(service_type=ser['service_type'], unit=ser['unit'], amount=ser['amount'], price=ser['price'])[0]
    service.save()
    return service

def add_usage(usage):
    use = Usage.objects.get_or_create(id=usage['id'], customer=usage['customer'], 
    mode=usage['mode'], operator=usage['operator'], reference=usage['reference'],
    travel_class=usage['travel_class'], travel_from=usage['travel_from'],
    travel_to=usage['travel_to'], purchase_id=usage['purchase_id'], usage_date_time=usage['usage_date_time'],
    route_via_avoid=usage['route_via_avoid'], ticket=usage['ticket'], pre_paid=usage['pre_paid'],
    price=usage['price'], )[0]
    use.save()
    return use


def add_concession(conc):
    concession = Concession.objects.get_or_create(id=conc['id'], customer=conc['customer'],
    mode=conc['mode'], operator=conc['operator'], name=conc['name'], price=conc['price'], discount=conc['discount'],
    transaction=conc['transaction'], valid_from_date_time=conc['valid_from_date_time'], 
    valid_to_date_time=conc['valid_to_date_time'], conditions=conc['conditions'])[0]
    concession.save()
    return concession

def add_purchase(purch):
    purchase = Purchase.objects.get_or_create(id=purch['id'], customer=purch['customer'],
    mode=purch['mode'], operator=purch['operator'], travel_class=purch['travel_class'], booking_date_time=purch['booking_date_time'],
    transaction=purch['transaction'], account_balance=purch['account_balance'], agent=purch['agent'],
    passenger_number=purch['passenger_number'], passenger_type=purch['passenger_type'],
    vehicle=purch['vehicle'], route=purch['route'], travel_from_date_time=purch['travel_from_date_time'],
    travel_to_date_time=purch['travel_to_date_time'], conditions=purch['conditions'], concession=purch['concession'],
    restrictions=purch['restrictions'], ticket=purch['ticket'], location_from=purch['location_from'], 
    location_to=purch['location_to'], reserved_position=purch['reserved_position'], service_request=purch['service_request'] )[0]
    purchase.save()
    return purchase




if __name__ == '__main__':
    print('Starting api population script...')
    populate()


