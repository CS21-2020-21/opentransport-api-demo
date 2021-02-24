from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from http import HTTPStatus
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

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


#class TestProjectRequirements(TestCase):


class IntegrationTesting(TestCase):


    def setUp(self):
        # runs before every test
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=self.options, executable_path=r"C:\webdrivers/chromedriver.exe")
        self.driver.maximize_window()


    def tearDown(self):
        # runs after every test
        self.driver.quit()


    def home_page_to_sign_in_page(self):
        # get the driver set to the homepage
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(1)

        # click on the button to go to the login page
        self.driver.find_element_by_id('sign_in').click()
        time.sleep(1)

        # check if we are on the login page
        self.assertEqual(self.driver.title, "PSD Ferries - Login")


    def home_page_to_sign_up_page(self):
        # get the driver set to the homepage
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(1)

        # click on the button to go to the register page
        self.driver.find_element_by_id('sign_up').click()
        time.sleep(1)

        # check if we are on the register page
        self.assertEqual(self.driver.title, "PSD Ferries - Register")


    def sign_in_process(self):
        # type the username into the username field
        self.driver.find_element_by_id('id_login').send_keys("6")
        time.sleep(1)

        # type the password into the password field
        self.driver.find_element_by_id('id_password').send_keys("12345678abc")
        time.sleep(1)

        # if it doesn't already exist, create the user object and return it
        user = User.objects.get_or_create(username="6", password="12345678abc")[0]

        # submit the form
        self.driver.find_element_by_id('sign_in_button').click()
        time.sleep(1)

        # check if we have been redirected to the homepage and the user is logged in
        self.assertEqual(self.driver.title, "PSD Ferries - Homepage")
        assert user.is_authenticated


    def sign_up_process(self):
        # type the username into the username field
        self.driver.find_element_by_id('id_username').send_keys("7")
        time.sleep(1)

        # type the email into the email field
        self.driver.find_element_by_id('id_email').send_keys("7@gmail.com")
        time.sleep(1)

        # type the password into the password field
        self.driver.find_element_by_id('id_password1').send_keys("12345678abc")
        time.sleep(1)

        # type the password into the password field
        self.driver.find_element_by_id('id_password2').send_keys("12345678abc")
        time.sleep(1)

        # if it doesn't already exist, create the user object and return it
        user = User.objects.get_or_create(username="7", password="12345678abc")[0]

        # submit the form
        self.driver.find_element_by_id('sign_up_button').click()
        time.sleep(1)

        # check if we have been redirected to the homepage and the user is logged in
        self.assertEqual(self.driver.title, "PSD Ferries - Homepage")
        assert user.is_authenticated


    def home_page_to_my_account_page(self):
        # click the button to open the dropdown items list
        self.driver.find_element_by_id('dropdownMenuLink').click()
        time.sleep(1)

        # click the button to go to the my account page
        self.driver.find_element_by_id('my_account').click()
        time.sleep(1)

        # check if we are on the my account page
        self.assertEqual(self.driver.title, "PSD Ferries - My Account")


    def my_account_page_to_linked_accounts_page(self):
        # click the button to open the linked accounts page
        self.driver.find_element_by_id('linked_accounts').click()
        time.sleep(1)

        # check if we are on the linked accounts page
        self.assertEqual(self.driver.title, "PSD Ferries - Linked Accounts")


    def my_account_page_to_psd_ferries_account_page(self):
        # click the button to open the psd ferries account page
        self.driver.find_element_by_id('psd_ferries_account').click()
        time.sleep(1)

        # check if we are on the psd ferries account page
        self.assertEqual(self.driver.title, "PSD Ferries - PSD Ferries Account")


    def my_account_page_to_link_account_page(self):
        # click the button to open the link account page
        self.driver.find_element_by_id('link_account').click()
        time.sleep(1)

        # check if we are on the link account page
        self.assertEqual(self.driver.title, "PSD Ferries - Link Account")


    def perform_linking_query(self):
        # fill in the company name that we want to link our account to
        self.driver.find_element_by_id('id_operator_cbo_box').send_keys("CS21")
        time.sleep(1)

        # fill in the email of the account that we're linking to
        self.driver.find_element_by_id('id_email').send_keys("cs21@gmail.com")
        time.sleep(1)

        # fill in the username of the account that we're linking to
        self.driver.find_element_by_id('id_username').send_keys("1")
        time.sleep(1)

        # click the submit button to submit the query
        self.driver.find_element_by_id('submit_link_query').click()
        time.sleep(1)

        # check if we are on the check email page
        self.assertEqual(self.driver.title, "PSD Ferries - Check Email")


    def perform_email_verification(self):
        # fill in the email verification code
        self.driver.find_element_by_id('id_code').send_keys("123456")
        time.sleep(1)

        # click the submit button to submit the verification query
        self.driver.find_element_by_id('submit_email_confirmation').click()
        time.sleep(1)

        # check if we are on the account linked page
        self.assertEqual(self.driver.title, "PSD Ferries - Account Linked")


    def is_account_linked(self):
        # fill in the company name that we want to link our account to
        self.driver.find_element_by_id('id_operator_cbo_box').send_keys("CS21")
        time.sleep(1)

        # fill in the email of the account that we're linking to
        self.driver.find_element_by_id('id_email').send_keys("cs21@gmail.com")
        time.sleep(1)

        # fill in the username of the account that we're linking to
        self.driver.find_element_by_id('id_username').send_keys("1")
        time.sleep(1)

        # click the submit button to submit the query
        self.driver.find_element_by_id('submit_link_query').click()
        time.sleep(1)

        if self.driver.title == "PSD Ferries - Link Failed":
            return True
        elif self.driver.title == "PSD Ferries - Check Email":
            return False


    def any_page_to_home_page(self):
        # click the button to go to the home page
        self.driver.find_element_by_id('home_button').click()
        time.sleep(1)

        # check if we are on the home page
        self.assertEqual(self.driver.title, "PSD Ferries - Homepage")


    def perform_data_query(self, query_type, account_type):
        # decide which query to perform based on query_type
        if query_type == 'purchases':

            # click the purchases button to query customer purchases
            self.driver.find_element_by_id('purchases').click()
            time.sleep(1)

            # check if we are dealing with the linked account data or not
            if account_type == "not_linked":
                # check if we are on the psd ferries purchases page
                self.assertEqual(self.driver.title, "PSD Ferries - PSD Ferries Purchases")

            elif account_type == "linked":
                # check if we are on the show linked account page
                self.assertEqual(self.driver.title, "PSD Ferries - Show Linked Account")

        elif query_type == 'concessions':

            # click the concessions button to query customer concessions
            self.driver.find_element_by_id('concessions').click()
            time.sleep(1)

            # check if we are dealing with the linked account data or not
            if account_type == "not_linked":
                # check if we are on the psd ferries concessions page
                self.assertEqual(self.driver.title, "PSD Ferries - PSD Ferries Concessions")

            elif account_type == "linked":
                # check if we are on the show linked account page
                self.assertEqual(self.driver.title, "PSD Ferries - Show Linked Account")
            
        elif query_type == 'usages':

            # click the usages button to query customer usages
            self.driver.find_element_by_id('usages').click()
            time.sleep(1)

            # check if we are dealing with the linked account data or not
            if account_type == "not_linked":
                # check if we are on the psd ferries usages page
                self.assertEqual(self.driver.title, "PSD Ferries - PSD Ferries Usages")

            elif account_type == "linked":
                # check if we are on the show linked account page
                self.assertEqual(self.driver.title, "PSD Ferries - Show Linked Account")


    def test_homepage_to_login_to_query_purchases(self):
        
        # testing a requirement of looking up customer purchases
        print("Testing Scenario #1 - Making purchases query")
        self.home_page_to_sign_in_page()
        self.sign_in_process()
        self.home_page_to_my_account_page()
        self.my_account_page_to_psd_ferries_account_page()
        self.perform_data_query('purchases', 'not_linked')
        print("Scenario #1 successfully completed")


    def test_homepage_to_login_to_query_concessions(self):

        # testing a requirement of looking up customer concessions
        print("Testing Scenario #2 - Making concessions query")
        self.home_page_to_sign_in_page()
        self.sign_in_process()
        self.home_page_to_my_account_page()
        self.my_account_page_to_psd_ferries_account_page()
        self.perform_data_query('concessions', 'not_linked')
        print("Scenario #2 successfully completed")


    def test_homepage_to_login_to_query_usages(self):

        # testing a requirement of looking up customer usages
        print("Testing Scenario #3 - Making usages query")
        self.home_page_to_sign_in_page()
        self.sign_in_process()
        self.home_page_to_my_account_page()
        self.my_account_page_to_psd_ferries_account_page()
        self.perform_data_query('usages', 'not_linked')
        print("Scenario #3 successfully completed")


    def test_homepage_to_login_to_link_account_to_query_linked_account_purchases(self):
        # testing a requirement of linking an account and making the purchases query
        print("Testing Scenario #4 - Linking an account and making the purchases query")
        self.home_page_to_sign_in_page()
        self.sign_in_process()
        self.home_page_to_my_account_page()
        self.my_account_page_to_link_account_page()
        if self.is_account_linked():
            self.any_page_to_home_page()
            self.home_page_to_my_account_page()
            self.my_account_page_to_linked_accounts_page()
            self.perform_data_query('purchases', 'linked')
        else:
            self.perform_email_verification()
            self.any_page_to_home_page()
            self.home_page_to_my_account_page()
            self.my_account_page_to_linked_accounts_page()
            self.perform_data_query('purchases', 'linked')
        print("Scenario #4 successfully completed")


    def test_homepage_to_login_to_link_account_to_query_linked_account_concessions(self):
        # testing a requirement of linking and account and making the concessions query
        print("Testing Scenario #5 - Linking an account and making the concessions query")
        self.home_page_to_sign_in_page()
        self.sign_in_process()
        self.home_page_to_my_account_page()
        self.my_account_page_to_link_account_page()
        if self.is_account_linked():
            self.any_page_to_home_page()
            self.home_page_to_my_account_page()
            self.my_account_page_to_linked_accounts_page()
            self.perform_data_query('concessions', 'linked')
        else:
            self.perform_email_verification()
            self.any_page_to_home_page()
            self.home_page_to_my_account_page()
            self.my_account_page_to_linked_accounts_page()
            self.perform_data_query('concessions', 'linked')
        print("Scenario #5 successfully completed")


    def test_homepage_to_login_to_link_account_to_query_linked_account_usages(self):
        # testing a requirement of linking an account and making the usages query
        print("Testing Scenario #6 - Linking an account and making the usages query")
        self.home_page_to_sign_in_page()
        self.sign_in_process()
        self.home_page_to_my_account_page()
        self.my_account_page_to_link_account_page()
        if self.is_account_linked():
            self.any_page_to_home_page()
            self.home_page_to_my_account_page()
            self.my_account_page_to_linked_accounts_page()
            self.perform_data_query('usages', 'linked')
        else:
            self.perform_email_verification()
            self.any_page_to_home_page()
            self.home_page_to_my_account_page()
            self.my_account_page_to_linked_accounts_page()
            self.perform_data_query('usages', 'linked')
        print("Scenario #6 successfully completed")


    def test_homepage_to_signup_to_link_account(self):
        # testing a requirement of creating an account and linking it with the CS21 account
        print("Testing Scenario #7 - Creating and linking an account")
        self.home_page_to_sign_up_page()
        self.sign_up_process()
        self.home_page_to_my_account_page()
        self.my_account_page_to_link_account_page()
        self.perform_linking_query()
        self.perform_email_verification()
        print("Scenario #7 successfully completed")