
#loading modules to be utilized
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    #Adding web elements/locators to be interacted within this functionality
    email_locator_id = "Email"
    password_locator_id = "Password"
    login_button_xpath = "//button[text()='Log in']"
    logout_button_xpath = "//a[text()='logout']"

    # browser driver interaction
    def __init__(self, driver):
        self.driver = driver

    # Add action methods
    def setuseremail(self, email):

        WebElement1 = self.driver.find_element(By.ID, self.email_locator_id)
        WebElement1.clear()
        WebElement1.send_keys(email)
    def setpasswordname(self, password):
        WebElement2 = self.driver.find_element(By.ID, self.password_locator_id)
        WebElement2.clear()
        WebElement2.send_keys(password)

    def clicklogin(self):
        WebElement3 = self.driver.find_element(By.XPATH, self.login_button_xpath)
        WebElement3.click()

    def clicklogout(self):
        WebElement4 = self.driver.find_element(By.XPATH, self.logout_button_xpath)
        WebElement4.click()