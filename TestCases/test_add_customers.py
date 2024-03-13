import pytest
import time
import logging
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.AddCustomerPage import AddCustomer
from Utilities.customLogger import Loggen
from PageObjects.LoginPage import Login
from Utilities.readproperties import ReadConfig


class TestAddCustomer_002:
    # setting up login details
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = Loggen.loggen()

    #Calling methods
    def test003_addcustomer(self, setup):
        self.logger.info("**Test003 : Verifying Add Customer functionality")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setuseremail(self.username)
        self.lp.setpasswordname(self.password)
        self.lp.clicklogin()
        self.logger.info("**Login successful**")
        time.sleep(1)
        self.logger.info("__Add Customer Test started__")
        self.addcust = AddCustomer(self.driver)
        self.logger.info("__Menu to be Clicked__")
        self.addcust.ClickOnAddCustomerMenu()
        self.logger.info("__Menu Clicked__")
        time.sleep(1)
        self.addcust.ClickOnAddCustomerMenuItem()
        self.logger.info("__Menu Item Clicked__")
        self.addcust.ClickOnAddNewCustomer()
        self.logger.info("__add new Clicked__")
        time.sleep(1)
        self.logger.info("__Adding customer info__")

        def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))

        self.email = random_generator() + "@gmail.com"

        self.addcust.add_email(self.email)
        self.logger.info("__Added email__")
        self.addcust.add_password("test133")
        self.logger.info("__Added pwrd")
        self.addcust.add_first_name("Harsh")
        self.logger.info("__Added name")
        self.addcust.add_last_name("tal")
        self.logger.info("__Added surname")
        self.addcust.set_gender("Male")
        self.logger.info("__Added gender__")
        self.addcust.set_DOB("7/05/1985")
        self.logger.info("__Added date__")
        self.addcust.add_company_name("Personal Bank")
        self.logger.info("__Added company__")
        self.addcust.set_customer_role("Vendors")
        self.logger.info("__Added role__")
        self.addcust.set_vendor("Vendor 2")
        self.logger.info("__Added vendor__")
        self.addcust.set_status("Active")
        self.logger.info("__Added status__")
        self.addcust.add_comment("Test user")
        self.logger.info('__Added comment__')
        self.addcust.save_customer()
        self.logger.info("Saving customer info")
        time.sleep(1)
        self.msg = self.driver.find_element(By.TAG_NAME, "body")
        save_text = self.msg.text

        if "The new customer has been added successfully." in save_text:
            assert True == True
            self.logger.info("New Customer added")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "AddCustomer.png")
            self.logger.error("The new Customer addition Failed")
            assert True == False

        #self.driver.close()
