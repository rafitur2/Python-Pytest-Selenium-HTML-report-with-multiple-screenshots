import sys
import traceback
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
import pytest

#Test22
class TestBrowser():

    def test_teach(self,browser):
        Value = "Under 20"
        browser.get("http://www.teachmeselenium.com/automation-practice/")
        dropdown = Select(browser.find_element_by_name("age"))
        dropdown.select_by_value(Value)
        selected_value=dropdown.first_selected_option
        browser.save_screenshot("Test1.png")
        assert selected_value.text == Value
        assert False

    def test_facebook(self,browser):
        Value = "Under 20"
        browser.get("http://www.facebook.com/")
        # browser.save_screenshot("Test2.png")
        assert "xyy" in browser.title

    def test_google(self,browser):
        Value = "Under 20"
        browser.get("http://www.google.com/")
        # browser.save_screenshot("Test2.png")
        assert "xyy" in browser.title
        assert True
