#!/usr/bin/env python3

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException, StaleElementReferenceException)

from selenium.webdriver.chrome.options import Options
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
