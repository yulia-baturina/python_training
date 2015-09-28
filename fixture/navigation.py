__author__ = 'IEUser'


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost:8080/addressbook/")

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()