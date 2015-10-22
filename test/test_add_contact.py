# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.stringUtils import StringsHelper
import pytest

testdata = [Contact()] + [
Contact(firstname=StringsHelper.randomstring("firstname", 10), lastname=StringsHelper.randomstring("lastname", 20),
          nickname=StringsHelper.randomstring("nickname", 20), company=StringsHelper.randomstring("company", 5),
        homePhone=StringsHelper.randomPhone("+",7), email=StringsHelper.randomstring("email", 10).join("mail.com"))
    for i in range(5)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)