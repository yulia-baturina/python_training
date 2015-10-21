# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="first", lastname="last", nickname="nick",
       company="company", homePhone="+11111111111", email="mail@mail.com"))
    old_contacts = app.contact.get_contact_list()
    contact=Contact(firstname="first_updated", middlename="middle", lastname="last_updated", nickname="nickname",
    company="new company", title="title", address="ad", homePhone="+21111111111", mobilePhone="+12222222222",
    email="mail@mail.com", email2="a@aa.com", secondaryPhone="+3(333)33")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

def test_modify_contact_initials(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="first", lastname="last", nickname="nick",
    company="company", homePhone="+22222222", email="mail@updated"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="updated firstname", lastname="updated lastname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)