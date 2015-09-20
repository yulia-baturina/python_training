# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        success = True
        wd = self.wd
        self.openHomePage(wd)
        self.login(wd, username="admin", password="secret")
        self.openGroupsPage(wd)
        self.createGroup(wd, Group(name="new", header="header", footer="footer"))
        self.returnToGroupsPage(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        success = True
        wd = self.wd
        self.openHomePage(wd)
        self.login(wd, username="admin", password="secret")
        self.openGroupsPage(wd)
        self.createGroup(wd, Group(name="", header="", footer=""))
        self.returnToGroupsPage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def returnToGroupsPage(self, wd):
        wd.find_element_by_link_text("group page").click()

    def createGroup(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group name
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def openGroupsPage(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def openHomePage(self, wd):
        wd.get("http://localhost:8080/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
