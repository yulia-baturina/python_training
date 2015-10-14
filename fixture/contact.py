__author__ = 'IEUser'

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_in_fields(self, contact):
        wd = self.app.wd
        if contact.firstname:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.lastname:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.company:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company)
        if contact.title:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)
        if contact.address:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.home:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.home)

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill in contact fields
        self.fill_in_fields(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.navigation.return_to_home_page()
        self.contact_cache=None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # init contact update
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        # fill in contact fields
        self.fill_in_fields(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_home_page()
        self.contact_cache=None

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        self.app.accept_alert()
        self.app.navigation.return_to_home_page()
        self.contact_cache=None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache=None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_elements_by_tag_name("td")[1].text
                firstname = element.find_elements_by_tag_name("td")[2].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)
