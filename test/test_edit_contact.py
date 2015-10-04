# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_first_contact(Contact(firstname="first_updated", middlename="middle", lastname="last_updated", nickname="nickname",
    company="new company", title="title", address="ad", homePhone="+11111111111", mobilePhone="+12222222222", workPhone="",
    fax="", email="", email2="a@aa.com", email3="", homePage="", birthDay="", birthMonth="", birthYear="",
    annDay="", annMonth="", annYear="", group="", secondaryAddress="", home="", notes=""))
