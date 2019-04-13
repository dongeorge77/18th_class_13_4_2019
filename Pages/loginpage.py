from Pages.webgeneric import WebGeneric
from Testdata.data import *
class LoginPage(WebGeneric):
    def __init__(self,driver):
        self.driver = driver
        self.un = "username"
        self.pwd = "pwd"
        self.login = "//*[text()='Login ']"
        global wb
        wb = WebGeneric(driver)
    def enter_un(self):
        #self.driver.find_element_by_name(self.un).send_keys(UN)
        wb.Enter(self.un, UN)
    def enter_pwd(self):
        #self.driver.find_element_by_name(self.pwd).send_keys(PWD)
        wb.Enter(self.pwd, PWD)
    def click_login(self):
        #self.driver.find_element_by_xpath(self.login).click()
        wb.Click(self.login)