from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

class TestViews(TestCase):
    
    def test_index_view(self):
        response = self.client.get(reverse('customers:index'))
        self.assertEqual(response.status_code, 200)

    def test_account_view(self):
        response = self.client.get(reverse('customers:my_account'))
        self.assertEqual(response.status_code, 200)

    def test_query_view(self):
        response = self.client.get(reverse('customers:query'))
        self.assertEqual(response.status_code, 200)

    def test_query_purchases_view(self):
        response = self.client.get(reverse('customers:query_purchases'))
        self.assertEqual(response.status_code, 200)

    def test_query_concessions_view(self):
        response = self.client.get(reverse('customers:query_concessions'))
        self.assertEqual(response.status_code, 200)

    def test_query_usages_view(self):
        response = self.client.get(reverse('customers:query_usages'))
        self.assertEqual(response.status_code, 200)

class TestForms(TestCase):
    def test_purchase_from_date_incorrect_format(self):
        response = self.client.post(reverse('customers:query_purchases'), data={'from_date':'vbw'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Enter a valid date/time.')

    def test_purchase_to_date_incorrect_format(self):
        response = self.client.post(reverse('customers:query_purchases'), data={'to_date':'vbw'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Enter a valid date/time.')
    
    def test_concession_from_date_incorrect_format(self):
        response = self.client.post(reverse('customers:query_concessions'), data={'from_date':'vbw'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Enter a valid date/time.')

    def test_concession_to_date_incorrect_format(self):
        response = self.client.post(reverse('customers:query_concessions'), data={'to_date':'vbw'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Enter a valid date/time.')

    def test_usage_from_date_incorrect_format(self):
        response = self.client.post(reverse('customers:query_usages'), data={'from_date':'vbw'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Enter a valid date/time.')

    def test_usage_to_date_incorrect_format(self):
        response = self.client.post(reverse('customers:query_usages'), data={'to_date':'vbw'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Enter a valid date/time.')

    #no tests for the other formats because Django handles them itself


class TestProjectRequirements(TestCase):
    
