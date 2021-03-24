from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse

from selenium import webdriver
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

import time


class UnitTesting(TestCase):


    def setUp(self):
        #runs before every test
        self.client = Client()  


    def test_index_page(self):
        url = reverse('operators:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'operators/index.html')


    def test_my_account_page(self):
        url = reverse('operators:my_account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'operators/my_account.html')


    def test_query_page(self):
        url = reverse('operators:query')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'operators/query.html')
    

    def test_change_data_page(self):
        url = reverse('operators:change_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'operators/change_data.html')

    
    def test_query_modes_page(self):
        url = reverse('operators:query_modes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'operators/query_modes.html')


    def test_query_operators_page(self):
        url = reverse('operators:query_operators')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'operators/query_operators.html')


    def test_view_operators_page(self):
        url = reverse('operators:view_operators')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'operators/view_operators.html')

    
    def test_query_form_with_mode(self):
        url = reverse('operators:query')
        response = self.client.post(url, data={'query_type':'Modes'})
        self.assertEqual(response.status_code, 200)

    
    def test_query_form_with_operator(self):
        url = reverse('operators:query')
        response = self.client.post(url, data={'query_type':'Operators'})
        self.assertEqual(response.status_code, 200)


    def test_details_form(self):
        url = reverse('operators:query_operators')
        data = {'href':'www.scotrail.com', 'description':'trains', 'operator_id':'123', 
        'phone':'01234567890', 'email':'test@test.com', 'homepage':'www.scotrail.com', 
        'language':'en', 'modes':1, 'mode':'train', 'url':'www.scotrail.com'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        

class IntegrationTesting(TestCase):

    def setUp(self):
        #runs before every test
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        print('starting')


    def tearDown(self):
        #runs after every test
        self.driver.quit()


    def home_to_sign_in_page(self):
        #get the driver set to the homepage/chromedriver.exe
        self.driver.get('http://127.0.0.1:8000/')
        time.sleep(1)

        user = User.objects.get_or_create(username='1', password='12345678abc')[0]

        #click on the button to go to the login page
        self.driver.find_element_by_id('signin').click()
        time.sleep(1)


        #check we are on the login page
        self.assertEqual(self.driver.title, 'Operators - Login')


    def login_page(self):
       
        #type the username into the username field
        self.driver.find_element_by_id('id_login').send_keys('1')
        time.sleep(1)

        #type the password into the password field
        self.driver.find_element_by_id('id_password').send_keys('12345678abc')
        time.sleep(1)

        #if it doesn't already exist, create the user object and return it
        #user, created = User.objects.get_or_create(username='1', password='12345678abc')
        
        
        #submit the form
        self.driver.find_element_by_id('signinbutton').click()
        time.sleep(1)

        #check we have been redirected to the homepage and the user is logged in
        self.assertEqual(self.driver.title, 'Operators - Homepage')
        

    def home_page_to_query_page(self):
        #click the button to go the the query page and check this worked
        self.driver.find_element_by_id('query button').click()
        time.sleep(1)
        self.assertEqual(self.driver.title, 'Operators - Query Data')


    def perform_query(self, query_type):
        #select appropriate query from drop down menu
        select = Select(self.driver.find_element_by_id('id_query_type'))
        select.select_by_visible_text(query_type)
        time.sleep(1)
        self.driver.find_element_by_id('submit button').click()
        time.sleep(1)

        if query_type=='Modes':
            #if we performed the modes query, check the correct page and content is displayed
            self.assertEqual(self.driver.find_element_by_id('title').text, 'Here are the transport modes')
            self.assertEqual(self.driver.title, 'Operators - View Modes')
        else:
            #if we performed the operators query check the correct page is displayed
            self.assertEqual(self.driver.title, 'Operators - Query Operators')


    def add_operator_argument(self, element_id, argument_value):

        #fill in a field depending on the parameter passed in
        self.driver.find_element_by_id(element_id).send_keys(argument_value)
        time.sleep(1)

        #submit the request
        self.driver.find_element_by_name('submit').click()
        time.sleep(1)

        #check the query was performed correctly
        self.assertEqual(self.driver.title, 'Operators - View Operators')
        self.assertEqual(self.driver.find_element_by_id(element_id).text,argument_value)


    def test_homepage_to_login_to_query_modes(self):
        
        #testing project requirement #4
        #testing functional requirement of looking up modes of transport
        print('Testing Scenario #1 - Making mode query')
        self.home_to_sign_in_page()
        self.login_page()
        self.home_page_to_query_page()
        self.perform_query('Modes')
        print('Scenario #1 successfully completed')


    def test_homepage_to_login_to_query_operators(self):

        #testing project requirement #4
        #functional requirement of looking up operators
        print('Testing Scenario #2 - Making Operator Query')
        self.home_to_sign_in_page()
        self.login_page()
        self.home_page_to_query_page()
        self.perform_query('Operators')
        self.add_operator_argument('id_operator_id', '003')
        print('Scenario #2 successfully completed')
