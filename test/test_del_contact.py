# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="first", middlename="", lastname="last", nickname="nick",
    company="company", title="", address="", homePhone="+11111111111", mobilePhone="", workPhone="",
    fax="", email="", email2="", email3="", homePage="", birthDay="", birthMonth="", birthYear="",
    annDay="", annMonth="", annYear="", group="", secondaryAddress="", home="", notes=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts)-1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
