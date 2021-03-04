from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework.test import APIClient, APIRequestFactory

from api import views


class TestPoll(APITestCase):
    def setUpa(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.ModeViewSet.as_view({'post': 'list'})


    def setUpb(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.CatalogueViewSet.as_view({'post': 'list'})


    def setUpc(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = self.setup_user()
        self.view =views.ItemViewSet.as_view({'post': 'list'})
