class WebGeneric:
    def __init__(self,driver):
        self.driver = driver
    def Enter(self,locator,input_val):
        self.driver.find_element_by_name(locator).send_keys(input_val)
    def Click(self,locator):
        self.driver.find_element_by_xpath(locator).click()