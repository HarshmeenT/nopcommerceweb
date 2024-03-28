import pytest
import logging
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import Loggen

class TestLogin_001:

    #hardcoded (common) data comes from config.ini file
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = Loggen.loggen()

    @pytest.mark.regression

    # 1. Verify home page title
    def test001_homePageTitle(self, setup):
        self.logger.info("#######TC#1########")
        self.logger.info("**Test001 : Verifying home page title**")
        self.driver = setup
        self.driver.get(self.baseURL)
        home_page_title = self.driver.title
        if home_page_title == 'Your store. Login':
            self.driver.close()
            self.logger.info("**Passed**")
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "_test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**Failed**")
            assert False

# 2. Verify user Login

    @pytest.mark.sanity
    @pytest.mark.regression
    def test002_login(self, setup):
        self.logger.info("**Test002 : Verify user is able to login successfully**")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setuseremail(self.username)
        self.lp.setpasswordname(self.password)
        self.lp.clicklogin()

        landing_page_title = self.driver.title
        if landing_page_title == 'Dashboard / nopCommerce administration':
            self.driver.close()
            self.logger.info("**Passed**")
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "_test_login.png")
            self.driver.close()
            self.logger.error("**Failed**")
            assert False


# Add customers
# Search customers by Name
# Search customers by Email