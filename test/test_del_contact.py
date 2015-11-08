# -*- coding: utf-8 -*-
from model.contact import Contact
import random

# test fails because editing/deleting contacts on UI adds new rows to DB instead of updating/deleting them
def test_delete_random_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="first", lastname="last", nickname="nick",
    company="company", homePhone="+11111111111", email="mail@mail.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_index = old_contacts.index(contact)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts[contact_index:contact_index+1] = []
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)