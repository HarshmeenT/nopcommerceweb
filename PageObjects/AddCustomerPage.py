#loading modules to be utilized
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:

    #Add locators
    lnk_Customers_Menu_xpath = "//a[@href='#']//p[normalize-space()='Customers']"
    #lnk_Customers_Menu_xpath = "//a[@href='#']//span[contains(text(), 'Customers')]"
    lnk_Customers_Menu_item_xpath ="//a[@href='/Admin/Customer/List']//p[normalize-space()='Customers']"
    btn_Add_New_Customer_xpath = "//a[normalize-space()='Add new']"
    txt_box_Email_xpath = "//input[@id='Email']"
    txt_box_password_xpath = "//input[@id='Password']"
    txt_box_FName_xpath = "//input[@id='FirstName']"
    txt_box_LName_xpath = "//input[@id='LastName']"
    rad_Gender_male_xpath = "//input[@id='Gender_Male']"
    rad_Gender_female_xpath = "//input[@id='Gender_Female']"
    txt_box_Calendar_id = "//input[@id='DateOfBirth']"
    txt_box_Company_xpath= "//input[@id='Company']"
    drp_Vendor1_xpath= "//option[text()= 'Vendor 1']"
    drp_Vendor2_xpath = "//option[text()= 'Vendor 2']"
    li_Customer_Roles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    li_Registered_xpath = "//li[contains(text(),'Registered')]"
    li_Forum_Moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    li_Guest_xpath= "//li[contains(text(),'Guests')]"
    li_Vendor_xpath = "//li[contains(text(),'Vendors')]"
    li_Administrator_xpath = "//li[contains(text(),'Administrators']"
    chk_box_Active_xpath= "//input[@id='Active']"
    btn_Save_xpath = "//button[@name='save']"
    txt_box_Comment_xpath = "//textarea[@id='AdminComment']"

    #Add constructor
    def __init__(self, driver):
        self.driver = driver

    #Add Action methods
    def ClickOnAddCustomerMenu(self):
         self.driver.find_element(By.XPATH, self.lnk_Customers_Menu_xpath).click()

    def ClickOnAddCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnk_Customers_Menu_item_xpath).click()

    def ClickOnAddNewCustomer(self):
        self.driver.find_element(By.XPATH, self.btn_Add_New_Customer_xpath).click()

    def add_email(self, email):
       element_3 = self.driver.find_element(By.XPATH,self.txt_box_Email_xpath)
       element_3.send_keys(email)

    def add_password(self, password):
       element_4 = self.driver.find_element(By.XPATH, self.txt_box_password_xpath)
       element_4.send_keys(password)

    def add_first_name(self, FirstName):
       element_5 = self.driver.find_element(By.XPATH, self.txt_box_FName_xpath)
       element_5.send_keys(FirstName)

    def add_last_name(self, LastName):
        element_6 = self.driver.find_element(By.XPATH, self.txt_box_LName_xpath)
        element_6.send_keys(LastName)

    def set_gender(self, Gender):
        if Gender.lower() == 'male':
            self.driver.find_element(By.XPATH, self.rad_Gender_male_xpath).click()
        elif Gender.lower() == 'Female':
            self.driver.find_element(By.XPATH, self.rad_Gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rad_Gender_male_xpath).click()

    def set_DOB(self, date):
        element_9 = self.driver.find_element(By.XPATH, self.txt_box_Calendar_id)
        element_9.send_keys(date)

    def add_company_name(self, company_name):
         element_10 = self.driver.find_element(By.XPATH, self.txt_box_Company_xpath)
         element_10.send_keys(company_name)
         time.sleep(1)
    def set_customer_role(self, role):

        self.driver.find_element(By.XPATH, self.li_Customer_Roles_xpath).click()
        time.sleep(1)
        if role == 'Registered':
            current_value = self.driver.find_element(By.XPATH, self.li_Customer_Roles_xpath)
            if current_value != 'Registered':
                self.list_item = self.driver.find_element(By.XPATH, self.li_Registered_xpath)
        elif role == 'Administrators':
            self.list_item = self.driver.find_element(By.XPATH, self.li_Administrator_xpath)
        elif role == 'Vendors':
            self.list_item = self.driver.find_element(By.XPATH, self.li_Vendor_xpath)
        elif role == 'Guest':
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.list_item = self.driver.find_element(By.XPATH, self.li_Guest_xpath)
        else:
            self.list_item = self.driver.find_element(By.XPATH, self.li_Guest_xpath)

        self.list_item.click()

    def set_vendor(self, Vendor):
        if Vendor == "Vendor 1":
            self.driver.find_element(By.XPATH, self.drp_Vendor1_xpath).click()
        elif Vendor == "Vendor 2":
            self.driver.find_element(By.XPATH, self.drp_Vendor2_xpath).click()
    time.sleep(1)
    def set_status(self, status):
        if status != 'Active':
            self.driver.find_element(By.XPATH, self.chk_box_Active_xpath).click()
    def add_comment(self, admin_comment):
        element_13 = self.driver.find_element(By.XPATH, self.txt_box_Comment_xpath)
        element_13.send_keys(admin_comment)

    def save_customer(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()










