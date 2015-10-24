__author__ = 'IEUser'


class NavigationHelper:

    def __init__(self, app):
        self.app = app
        self.baseUrl = app.baseUrl

    def is_home_page_opened(self):
        wd = self.app.wd
        return wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("//*[@onClick='MailSelection()']")) > 0

    def open_home_page(self):
        wd = self.app.wd
        if not self.is_home_page_opened():
            wd.get(self.baseUrl)

    def return_to_home_page(self):
        wd = self.app.wd
        if not self.is_home_page_opened():
            wd.find_element_by_link_text("home").click()