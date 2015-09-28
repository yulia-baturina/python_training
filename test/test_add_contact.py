# -*- coding: utf-8 -*-
from model.contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="first", middlename="", lastname="last", nickname="nick",
    company="company", title="", address="", homePhone="+11111111111", mobilePhone="", workPhone="",
    fax="", email="", email2="", email3="", homePage="", birthDay="", birthMonth="", birthYear="",
    annDay="", annMonth="", annYear="", group="", secondaryAddress="", home="", notes=""))
    app.session.logout();
