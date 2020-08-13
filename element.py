#!/usr/bin/env python3

#from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ScrapElement:
    def __init__(self, by, token, driver):
        self.location = EC.visibility_of_element_located((by, token))
        self.by = by
        self.token = token
        self.element = None
        self.value = None
        self.driver = driver

    '''
    This changes the value of an input field. 
    If given (value) it will input that. Otherwise, it will input (self.value) 
    '''

    def change_data(self, value=None):
        if value != None:
            self.value = value
        # Wait untill element exists
        element = self.driver.wait.until(self.location)
        # Clear text in field
        element.clear()
        # Add new value
        element.send_keys(str(self.value))
        self.element = element
        return self.element

    '''
    This will return the wanted element safely
    '''

    def get_data(self):
        self.element = self.driver.wait.until(self.location)
        return self.element
