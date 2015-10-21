__author__ = 'IEUser'

from random import randint


def test_random_contacts_on_edit_page(app):
    contact_list = app.contact.get_contact_list()
    random_index = randint(0, len(contact_list)-1)
    contact_from_home_page = contact_list[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_home_page == contact_from_edit_page


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homePhone == contact_from_edit_page.homePhone
    assert contact_from_view_page.mobilePhone == contact_from_edit_page.mobilePhone
    assert contact_from_view_page.workPhone == contact_from_edit_page.workPhone