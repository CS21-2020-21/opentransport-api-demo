from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

import time


class IntegrationTesting(TestCase):

    def setUp(self):
        #runs before every test
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()


    def tearDown(self):
        #runs after every test
        self.driver.quit()


    def home_to_sign_in_page(self):
        #get the driver set to the homepage/chromedriver.exe
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(1)

        #click on the button to go to the login page
        self.driver.find_element_by_id('signin').click()
        time.sleep(1)

        #check we are on the login page
        self.assertEqual(self.driver.title, "Operators - Login")


    def login_page(self):
        #type the username into the username field
        self.driver.find_element_by_id('id_login').send_keys("user1")
        time.sleep(1)

        #type the password into the password field
        self.driver.find_element_by_id('id_password').send_keys("12345678abc")
        time.sleep(1)

        #if it doesn't already exist, create the user object and return it
        user = User.objects.get_or_create(username="user1", password="12345678abc")[0]

        #submit the form
        self.driver.find_element_by_id('signinbutton').click()
        time.sleep(1)

        #check we have been redirected to the homepage and the user is logged in
        self.assertEqual(self.driver.title, "Operators - Homepage")
        assert user.is_authenticated


    def home_page_to_query_page(self):
        #click the button to go the the query page and check this worked
        self.driver.find_element_by_id('query button').click()
        time.sleep(1)
        self.assertEqual(self.driver.title, "Operators - Query Data")


    def perform_query(self, query_type):
        #select appropriate query from drop down menu
        select = Select(self.driver.find_element_by_id("id_query_type"))
        select.select_by_visible_text(query_type)
        time.sleep(1)
        self.driver.find_element_by_id("submit button").click()
        time.sleep(1)

        if query_type=="Modes":
            #if we performed the modes query, check the correct page and content is displayed
            self.assertEqual(self.driver.find_element_by_id("title").text, "Here are the transport modes")
            self.assertEqual(self.driver.title, "Operators - View Modes")
        else:
            #if we performed the operators query check the correct page is displayed
            self.assertEqual(self.driver.title, "Operators - Query Operators")


    def add_operator_argument(self, element_id, argument_value):

        #fill in a field depending on the parameter passed in
        self.driver.find_element_by_id(element_id).send_keys(argument_value)
        time.sleep(1)

        #submit the request
        self.driver.find_element_by_name("submit").click()
        time.sleep(1)

        #check the query was performed correctly
        self.assertEqual(self.driver.title, "Operators - View Operators")
        self.assertEqual(self.driver.find_element_by_id(element_id).text,argument_value)


    def test_homepage_to_login_to_query_modes(self):
        
        #testing project requirement #4
        #testing functional requirement of looking up modes of transport
        print("Testing Scenario #1 - Making mode query")
        self.home_to_sign_in_page()
        self.login_page()
        self.home_page_to_query_page()
        self.perform_query("Modes")
        print("Scenario #1 successfully completed")


    def test_homepage_to_login_to_query_operators(self):

        #testing project requirement #4
        #functional requirement of looking up operators
        print("Testing Scenario #2 - Making Operator Query")
        self.home_to_sign_in_page()
        self.login_page()
        self.home_page_to_query_page()
        self.perform_query("Operators")
        self.add_operator_argument("id_operator_id", "003")
        print("Scenario #2 successfully completed")

