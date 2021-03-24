from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model


from rest_framework.test import APITestCase
from rest_framework.test import APIClient, APIRequestFactory

from api import views


class TestPoll(APITestCase):
    def setUp1(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.ModeViewSet.as_view({'post': 'list'})

    def setUp2(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.DiscountViewSet.as_view({'post': 'list'})

    def setUp3(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.ServiceViewSet.as_view({'post': 'list'})

    def setUp4(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.LocationViewSet.as_view({'post': 'list'})

    def setUp5(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.TravelFromViewSet.as_view({'post': 'list'})

    def setUp6(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.OperatorViewSet.as_view({'post': 'list'})

    def setUp7(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.TransactionViewSet.as_view({'post': 'list'})

    def setUp8(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.Monetary_ValueViewSet.as_view({'post': 'list'})

    def setUp9(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.TransactionViewSet.as_view({'post': 'list'})

    def setUp10(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.CustomerViewSet.as_view({'post': 'list'})

    def setUp11(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

        self.user = self.setup_user()
        self.view =views.AccountBalanceViewSet.as_view({'post': 'list'})

    def setUp12(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.VehicleViewSet.as_view({'post': 'list'})

    def setUp13(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.TicketViewSet.as_view({'post': 'list'})

    def setUp14(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.LatLongViewSet.as_view({'post': 'list'})

    def setUp15(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.LocationFromViewSet.as_view({'post': 'list'})
    def setUp16(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.LocationToViewSet.as_view({'post': 'list'})
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            username='testing',
            password='test'
        )

    def purchaseviewlist(self):
        request = self.factory.get(self.uri)
        request.user = self.user
        response = self.view(request)
        if request is None:
            print("Enter all details")
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def concessionviewlist(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        if response is None:
            print("Enter all details")
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200,received {0} instead.'
                         .format(response.status_code))