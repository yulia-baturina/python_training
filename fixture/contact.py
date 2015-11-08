__author__ = 'IEUser'

from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_in_fields(self, contact):
        wd = self.app.wd
        self.fill_in_field("firstname", contact.firstname)
        self.fill_in_field("lastname", contact.lastname)
        self.fill_in_field("nickname", contact.nickname)
        self.fill_in_field("company", contact.company)
        self.fill_in_field("title", contact.title)
        self.fill_in_field("address", contact.address)
        self.fill_in_field("home", contact.homePhone)
        self.fill_in_field("mobile", contact.mobilePhone)
        self.fill_in_field("work", contact.workPhone)
        self.fill_in_field("email", contact.email)
        self.fill_in_field("email2", contact.email2)
        self.fill_in_field("email3", contact.email3)
        self.fill_in_field("phone2", contact.secondaryPhone)

    def fill_in_field(self, fieldName, fieldValue):
        wd = self.app.wd
        if fieldValue is not None:
            wd.find_element_by_name(fieldName).click()
            wd.find_element_by_name(fieldName).clear()
            wd.find_element_by_name(fieldName).send_keys(fieldValue)

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
        self.modify_contact_by_index(contact, 0)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@title='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='%s']/../..//*[@title='Edit']" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//*[@title='Details']")[index].click()

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        # init contact update
        self.open_contact_to_edit_by_index(index)
        # fill in contact fields
        self.fill_in_fields(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_home_page()
        self.contact_cache=None

    def modify_contact_by_id(self, contact, id):
        wd = self.app.wd
        # init contact update
        self.open_contact_to_edit_by_id(id)
        # fill in contact fields
        self.fill_in_fields(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_home_page()
        self.contact_cache=None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select contact by index
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        self.app.accept_alert()
        self.app.navigation.return_to_home_page()
        self.contact_cache=None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # select contact by index
        wd.find_element_by_xpath("//input[@value='%s']" % id).click()
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
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                          all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails,
                                                  address = address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homePhone = wd.find_element_by_name("home").get_attribute("value")
        mobilePhone = wd.find_element_by_name("mobile").get_attribute("value")
        workPhone = wd.find_element_by_name("work").get_attribute("value")
        secondaryPhone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homePhone=homePhone, mobilePhone=mobilePhone, workPhone=workPhone, secondaryPhone=secondaryPhone,
                       address=address,
                       email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        if re.search("H: (.*)", text) is not None:
            homePhone = re.search("H: (.*)", text).group(1)
        else:
            homePhone = "";
        if re.search("M: (.*)", text) is not None:
            mobilePhone = re.search("M: (.*)", text).group(1)
        else:
            mobilePhone = ""
        if re.search("W: (.*)", text) is not None:
            workPhone = re.search("W: (.*)", text).group(1)
        else:
            workPhone = ""
        if re.search("P: (.*)", text) is not None:
            secondaryPhone = re.search("P: (.*)", text).group(1)
        else:
            secondaryPhone = ""
        return Contact(homePhone=homePhone, mobilePhone=mobilePhone, workPhone=workPhone, secondaryPhone=secondaryPhone)