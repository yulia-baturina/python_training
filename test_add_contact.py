# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from dataObjects.contact import Contact
from commonFunctions import open_home_page
from commonFunctions import login
from commonFunctions import logout
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        success = True
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(firstname="first", middlename="", lastname="last", nickname="nick",
        company="company", title="", address="", homePhone="+11111111111", mobilePhone="", workPhone="",
        fax="", email="", email2="", email3="", homePage="", birthDay="", birthMonth="", birthYear="",
        annDay="", annMonth="", annYear="", group="", secondaryAddress="", home="", notes=""))
        self.return_to_home_page(wd);
        logout(wd);

    def create_new_contact(self, wd, contact):
        # init cintact creation
        wd.find_element_by_link_text("add new").click()
        # fill in contact fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
