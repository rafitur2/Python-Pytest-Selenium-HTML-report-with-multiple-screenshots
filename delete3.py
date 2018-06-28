import unittest
import sys
import traceback
from selenium import webdriver
import time
# import unittest
from selenium.webdriver.support.select import Select
import pytest

wd = webdriver.Chrome()
class Test_Browser(unittest.TestCase):



    def test_google(self):
        wd.get("http://www.google.com/")
        # browser.save_screenshot("Test2.png")
        assert True
        wd.

        # browser.execute_script("alert('Good')")

