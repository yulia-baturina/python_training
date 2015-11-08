# -*- coding: utf-8 -*-
from model.contact import Contact
import random

# test fails because editing/deleting contacts on UI adds new rows to DB instead of updating/deleting them
def test_edit_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="first", lastname="last", nickname="nick",
       company="company", homePhone="+11111111111", email="mail@mail.com"))
    old_contacts = db.get_contact_list()
    contact=Contact(firstname="first_updated", middlename="middle", lastname="last_updated", nickname="nickname",
    company="new company", title="title", address="ad", homePhone="+21111111111", mobilePhone="+12222222222",
    email="mail@mail.com", email2="a@aa.com", secondaryPhone="+3(333)33")
    random_contact = random.choice(old_contacts)
    contact_index = old_contacts.index(random_contact)
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(contact, random_contact.id)
    new_contacts = db.get_contact_list()
    old_contacts[contact_index] = contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

# test fails because editing/deleting contacts on UI adds new rows to DB instead of updating/deleting them
def test_modify_contact_initials(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="first", lastname="last", nickname="nick",
    company="company", homePhone="+22222222", email="mail@updated"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="updated firstname", lastname="updated lastname")
    random_contact = random.choice(old_contacts)
    contact_index = old_contacts.index(random_contact)
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(contact, random_contact.id)
    new_contacts = db.get_contact_list()
    old_contacts[contact_index] = contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)