import time

from customers.models import *
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from selenium import webdriver


class ModelTesting(TestCase):

    def test_mode_model(self):
        mode = baker.make(Mode, short_desc="bus")

        self.assertTrue(isinstance(mode, Mode))
        self.assertEqual(str(mode), "bus")

    def test_operator_model(self):
        operator = baker.make(Operator, name="ScotRail")
        self.assertTrue(isinstance(operator, Operator))
        self.assertEqual(str(operator), "ScotRail")

    def test_linked_account_model(self):
        linked_account = baker.make(LinkedAccount, id=1)
        slug = slugify(1)
        linked_account.save()
        self.assertEqual(linked_account.slug, slug)


class UnitTesting(TestCase):

    def test_index_page(self):
        url = reverse('customers:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/index.html')

    def test_my_account_page(self):
        url = reverse('customers:my_account')
        self.client.force_login(User.objects.get_or_create(username="test")[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_ferry_query_selection_page(self):
        url = reverse('customers:ferry_query_selection')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/ferry_query_selection.html')

    def test_ferry_purchases_page(self):
        url = reverse('customers:ferry_purchases')
        user = User.objects.get_or_create(username="test")[0]
        self.client.force_login(user)
        Customer.objects.create(user=user, customer_id="test", name="test", email="test@test.com")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/ferry_purchases.html')

    def test_ferry_concessions_page(self):
        url = reverse('customers:ferry_concessions')
        user = User.objects.get_or_create(username="test")[0]
        self.client.force_login(user)
        Customer.objects.create(user=user, customer_id="test", name="test", email="test@test.com")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/ferry_concessions.html')

    def test_ferry_usages_page(self):
        url = reverse('customers:ferry_usages')
        user = User.objects.get_or_create(username="test")[0]
        self.client.force_login(user)
        Customer.objects.create(user=user, customer_id="test", name="test", email="test@test.com")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/ferry_usages.html')

    def test_link_account_page(self):
        url = reverse('customers:link_account')
        user = User.objects.get_or_create(username="test")[0]
        self.client.force_login(user)
        Customer.objects.create(user=user, customer_id="test", name="test", email="test@test.com")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/link_account.html')

    def test_check_email_page(self):
        url = reverse('customers:check_email')
        user = User.objects.get_or_create(username="test")[0]
        self.client.force_login(user)
        Customer.objects.create(user=user, customer_id="test", name="test", email="test@test.com")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/check_email.html')

    def test_account_linked_page(self):
        url = reverse('customers:account_linked')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/account_linked.html')

    def test_linked_failed_page(self):
        url = reverse('customers:link_failed')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/link_failed.html')

    def test_linked_accounts_page(self):
        url = reverse('customers:linked_accounts')
        user = User.objects.get_or_create(username="test")[0]
        self.client.force_login(user)
        Customer.objects.create(user=user, customer_id="test", name="test", email="test@test.com")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/linked_accounts.html')

    def test_show_linked_account_purchases_page(self):
        linked_account = baker.make(LinkedAccount, id=1)
        linked_account.save()
        url = reverse('customers:show_linked_account_purchases', kwargs={'id_slug': linked_account.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/show_linked_account_purchases.html')

    def test_show_linked_account_concessions_page(self):
        linked_account = baker.make(LinkedAccount, id=1)
        linked_account.save()
        url = reverse('customers:show_linked_account_concessions', kwargs={'id_slug': linked_account.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/show_linked_account_concessions.html')

    def test_show_linked_account_usages_page(self):
        linked_account = baker.make(LinkedAccount, id=1)
        linked_account.save()
        url = reverse('customers:show_linked_account_usages', kwargs={'id_slug': linked_account.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/show_linked_account_usages.html')

    def test_link_account_form(self):
        url = reverse('customers:link_account')
        response = self.client.post(url,
                                    data={'operator_cbo_box': 'PSDBuses', 'email': 'test@test.com', 'username': '1'})
        self.assertEqual(response.status_code, 302)

    def test_check_email_form(self):
        url = reverse('customers:check_email') + '?operator=PSDBuses&email=test@test.com&username=1'
        user = User.objects.get_or_create(username="test")[0]
        self.client.force_login(user)
        Customer.objects.create(user=user, customer_id="test", name="test", email="test@test.com")
        response = self.client.post(url, data={'code': '123456'})
        self.assertEqual(response.status_code, 302)


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
        self.driver.get("http://127.0.0.1:8000/index")
        time.sleep(1)

        # click on the button to go to the login page
        self.driver.find_element_by_id('sign_in').click()
        time.sleep(1)

        # check if we are on the login page
        self.assertEqual(self.driver.title, "PSD Ferries - Login")

    def home_page_to_sign_up_page(self):
        # get the driver set to the homepage
        self.driver.get("http://127.0.0.1:8000/index")
        time.sleep(1)

        # click on the button to go to the register page
        self.driver.find_element_by_id('sign_up').click()
        time.sleep(1)

        # check if we are on the register page
        self.assertEqual(self.driver.title, "PSD Ferries - Register")

    def sign_in_process(self):
        # type the username into the username field
        self.driver.find_element_by_id('id_login').send_keys("5")
        time.sleep(1)

        # type the password into the password field
        self.driver.find_element_by_id('id_password').send_keys("12345678abc")
        time.sleep(1)

        # if it doesn't already exist, create the user object and return it
        user = User.objects.get_or_create(username="5", password="12345678abc")[0]

        # submit the form
        self.driver.find_element_by_id('sign_in_button').click()
        time.sleep(1)

        # check if we have been redirected to the homepage and the user is logged in
        self.assertEqual(self.driver.title, "PSD Ferries - Homepage")
        assert user.is_authenticated

    def sign_up_process(self):
        # type the username into the username field
        self.driver.find_element_by_id('id_username').send_keys("8")
        time.sleep(1)

        # type the email into the email field
        self.driver.find_element_by_id('id_email').send_keys("8@gmail.com")
        time.sleep(1)

        # type the password into the password field
        self.driver.find_element_by_id('id_password1').send_keys("12345678abc")
        time.sleep(1)

        # type the password into the password field
        self.driver.find_element_by_id('id_password2').send_keys("12345678abc")
        time.sleep(1)

        # if it doesn't already exist, create the user object and return it
        user = User.objects.get_or_create(username="8", password="12345678abc")[0]

        # submit the form
        self.driver.find_element_by_id('sign_up_button').click()
        time.sleep(1)

        # check if we have been redirected to the homepage and the user is logged in
        self.assertEqual(self.driver.title, "PSD Ferries - Homepage")

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
        self.driver.find_element_by_id('id_operator_cbo_box').send_keys("PSD Buses")
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
        self.driver.find_element_by_id('id_operator_cbo_box').send_keys("PSD Buses")
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


'''
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
'''
