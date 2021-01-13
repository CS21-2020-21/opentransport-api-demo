import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'operator_api.settings')
django.setup()
from api.models import *


def populate():
    modes = [
        {
            "id": "001",
            "short-desc": "on foot",
            "long-desc": "for complete end-to-end journey mapping"
        },
        {
            "id": "002",
            "short-desc": "cycle",
            "long-desc": "includes both human-powered pedal cycle and ebike, typically rented or shared but also "
                         "possibly privately owned for complete end-to-end journey mapping "
        },
        {
            "id": "003",
            "short-desc": "moped & motorbike",
            "long-desc": "shared & privately-owned self-powered vehicles, for complete end-to-end journey mapping"
        },
        {
            "id": "004",
            "short-desc": "scooter",
            "long-desc": "includes human and electric/battery powered where passenger steps in/on"
        },
        {
            "id": "005",
            "short-desc": "segway",
            "long-desc": "includes any motorised self-balancing personal platform and also electric unicycles"
        },
        {
            "id": "006",
            "short-desc": "car",
            "long-desc": "includes any vehicle where the driver is also a passenger, such as: car / van vehicle "
                         "rental, car pool & car club "
        },
        {
            "id": "007",
            "short-desc": "bus",
            "long-desc": "includes any vehicle typically greater than 8 seats.. such as a mini bus"
        },
        {
            "id": "008",
            "short-desc": "tram",
            "long-desc": "includes any guided vehicle such as a streetcar and also trolleybuses that are limited by "
                         "overhead power lines "
        },
        {
            "id": "009",
            "short-desc": "metro & subway",
            "long-desc": "includes any light rail transit and their interconnecting systems"
        },
        {
            "id": "010",
            "short-desc": "train",
            "long-desc": "includes intercity, Eurostar / TGV, etc."
        },
        {
            "id": "011",
            "short-desc": "water bus",
            "long-desc": "includes river buses, typically just passenger service with multiple stops"
        },
        {
            "id": "012",
            "short-desc": "water ferry",
            "long-desc": "includes passenger only and also passenger & vehicle"
        },
        {
            "id": "013",
            "short-desc": "air",
            "long-desc": "aeroplane, helicopter, etc."
        },
        {
            "id": "014",
            "short-desc": "car parking",
            "long-desc": "includes on-street & off-street (e.g. dedicated building or airport short & long stay)"
        },
        {
            "id": "015",
            "short-desc": "taxi",
            "long-desc": "includes any vehicle where the driver is NOT a passenger"
        },
        {
            "id": "016",
            "short-desc": "suspended cable car",
            "long-desc": "includes any aerial cable cars, such as London 'Emirates Air Line', Barcelona Montjuïc & "
                         "Port Cable Cars and New York Roosevelt Island Tramway "
        },
    ]

    cat_metadata = [
        {
            "rel": "urn:X-hypercat:rels:isContentType",
            "val": "application/vnd.hypercat.catalogue+json"
        },
        {
            "rel": "urn:X-hypercat:rels:hasDescription:en",
            "val": "OpenTransport Operator Catalogue"
        },
        {
            "rel": "urn:X-hypercat:rels:supportsSearch",
            "val": "urn:X-hypercat:search:simple"
        },
    ]

    items = [
        {
            "href": "http://cs21operatorapi.pythonanywhere.com/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "CS21"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "http://cs21customerproject.pythonanywhere.com/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "000"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": "fakeemail@cs21customerproject.pythonanywhere.com"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "012345678910"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "2"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode2#Code",
                    "val": "008"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode2#Description",
                    "val": "tram"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.cs21customerproject.pythonanywhere.com/"
                }
            ]
        },
        {
            "href": "https://opentransport.avantiwestcoast.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Avanti West Coast"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.avantiwestcoast.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "001"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.avantiwestcoast.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.c2c-online.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "C2C"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.c2c-online.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "002"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03457444422"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.c2c-online.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.sleeper.scot/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Caledonian Sleeper"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.sleeper.scot/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "003"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.sleeper.scot/"
                }
            ]
        },
        {
            "href": "https://opentransport.chilternrailways.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Chiltern Railways"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.chilternrailways.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "004"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03456005165"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.chilternrailways.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.crosscountrytrains.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Crosscountry"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.crosscountrytrains.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "005"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.crosscountrytrains.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.eastmidlandsrailway.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "East Midlands Railway"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.eastmidlandsrailway.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "006"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.eastmidlandsrailway.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.gatwickexpress.com/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Gatwick Express"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.gatwickexpress.com/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "007"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03458501530"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.gatwickexpress.com/"
                }
            ]
        },
        {
            "href": "https://opentransport.grandcentralrail.com/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Grand Central Railway"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.grandcentralrail.com/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "008"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03456034852"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.grandcentralrail.com/"
                }
            ]
        },
        {
            "href": "https://opentransport.greatnorthernrail.com/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Great Northern"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.greatnorthernrail.com/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "009"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03450264700"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.greatnorthernrail.com/"
                }
            ]
        },
        {
            "href": "https://opentransport.gwr.com/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Great Western Railway"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.gwr.com/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03457000125"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.gwr.com/"
                }
            ]
        },
        {
            "href": "https://opentransport.greateranglia.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Greater Anglia"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.greateranglia.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "011"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": "contactcentre@greateranglia.co.uk"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.greateranglia.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.heathrowexpress.com/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Heathrow Express"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.heathrowexpress.com/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "012"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "0345 600 1515"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.heathrowexpress.com/"
                }
            ]
        },
        {
            "href": "https://opentransport.hulltrains.co.uk",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Hull Trains"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.hulltrains.co.uk"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "013"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": "customerservices.hull@firstgroup.com"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.hulltrains.co.uk"
                }
            ]
        },
        {
            "href": "https://opentransport.southwesternrailway.com/destinations-and-offers/island-line",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Island Line"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.southwesternrailway.com/destinations-and-offers/island-line"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "014"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03456000650"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.southwesternrailway.com/destinations-and-offers/island-line"
                }
            ]
        },
        {
            "href": "https://opentransport.lner.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "London North Eastern Railway"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.lner.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "015"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03457225333"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.lner.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.londonnorthwesternrailway.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "London Northwestern Railway"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.londonnorthwesternrailway.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "016"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03333110006"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.londonnorthwesternrailway.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.merseyrail.org/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Merseyrail"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.merseyrail.org/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "017"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "01515551111"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.merseyrail.org/"
                }
            ]
        },
        {
            "href": "https://opentransport.northernrailway.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Northern"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.northernrailway.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "018"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "08002006060"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.northernrailway.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.scotrail.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "ScotRail"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.scotrail.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "019"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": "customer.relations@scotrail.co.uk"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.scotrail.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.southwesternrailway.com",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "South Western Railway"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.southwesternrailway.com"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "020"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03456000650"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.southwesternrailway.com"
                }
            ]
        },
        {
            "href": "https://opentransport.southeasternrailway.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Southeastern"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.southeasternrailway.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "021"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03453227021"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.southwesternrailway.com"
                }
            ]
        },
        {
            "href": "https://opentransport.southernrailway.com/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Southern"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.southernrailway.com/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "022"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03451272920"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.southernrailway.com/"
                }
            ]
        },
        {
            "href": "https://opentransport.stanstedexpress.com/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Stansted Express"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.stanstedexpress.com/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "023"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.stanstedexpress.com/"
                }
            ]
        },
        {
            "href": "https://opentransport.thameslinkrailway.com/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Thameslink"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.thameslinkrailway.com/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "024"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03450264700"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.thameslinkrailway.com/"
                }
            ]
        },
        {
            "href": "https://opentransport.tpexpress.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Transpennine Express"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.tpexpress.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "025"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": "tpecustomer.relations@firstgroup.com"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.tpexpress.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.tfwrail.wales/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "Transport for Wales"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "tfwrail.wales/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "026"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03333211202"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.tfwrail.wales/"
                }
            ]
        },
        {
            "href": "https://opentransport.westmidlandsrailway.co.uk/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "West Midlands Railway"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "www.westmidlandsrailway.co.uk/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "027"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03333110039"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.westmidlandsrailway.co.uk/"
                }
            ]
        },
        {
            "href": "https://opentransport.tfl.gov.uk/modes/london-overground/",
            "item-metadata": [
                {
                    "rel": "urn:X-hypercat:rels:hasDescription:en",
                    "val": "London Overground"
                },
                {
                    "rel": "urn:X-hypercat:rels:hasHomepage",
                    "val": "tfl.gov.uk/modes/london-overground/"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasId",
                    "val": "028"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasEmail",
                    "val": ""
                },
                {
                    "rel": "urn:X-opentransport:rels:hasPhone",
                    "val": "03432221234"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasDefaultLanguage",
                    "val": "en"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberModes",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Code",
                    "val": "010"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMode1#Description",
                    "val": "train"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasNumberMIPTAURLs",
                    "val": "1"
                },
                {
                    "rel": "urn:X-opentransport:rels:hasMIPTAURL",
                    "val": "https://mipta.tfl.gov.uk/modes/london-overground/"
                }
            ]
        }
    ]

    catalogue = Catalogue.objects.get_or_create()[0]
    catalogue.save()

    for mode in modes:
        add_mode(mode)

    for metadata in cat_metadata:
        add_catalogue_metadata(metadata['rel'], metadata['val'], catalogue)

    for item in items:
        href = item['href']
        item_model = add_item(href, catalogue)
        for metadata in item['item-metadata']:
            add_item_metadata(metadata['rel'], metadata['val'], item_model)

    # Print out the categories we have added.
    print("")
    print("The following modes were added:")
    for m in Mode.objects.all():
        print(f'- {m}')

    print("")
    print("The following Catalogue Metadata was added:")
    for rv in CatalogueMetadata.objects.all():
        print(f'- {rv}')

    print("")
    print("The following Item Metadata was added:")
    for rv in ItemMetadata.objects.all():
        print(f'- {rv}')


def add_mode(mode_data):
    mode = Mode.objects.get_or_create(id=mode_data['id'], short_desc=mode_data['short-desc'],
                                      long_desc=mode_data['long-desc'])[0]
    mode.save()
    return mode


def add_catalogue_metadata(rel, val, catalogue):
    rel_val_pair = CatalogueMetadata.objects.get_or_create(rel=rel, val=val, catalogue=catalogue)[0]
    rel_val_pair.save()
    return rel_val_pair


def add_item(href, catalogue):
    item = Item.objects.get_or_create(href=href, catalogue=catalogue)[0]
    item.save()
    return item


def add_item_metadata(rel, val, item):
    item_metadata = ItemMetadata.objects.get_or_create(rel=rel, val=val, item=item)[0]
    item_metadata.save()
    return item_metadata


if __name__ == '__main__':
    print('Starting operator api population script...')
    populate()
