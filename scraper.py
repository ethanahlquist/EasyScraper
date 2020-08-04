#!/usr/bin/env python3

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException, StaleElementReferenceException)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumDriver(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        super().__init__(
            executable_path='/snap/bin/chromium.chromedriver',
            options=options
        )
        self.wait = WebDriverWait(self, 30, poll_frequency=10, ignored_exceptions=(
            NoSuchElementException, StaleElementReferenceException))


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
