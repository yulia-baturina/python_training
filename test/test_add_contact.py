# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


@pytest.fixture
def app(request):
    fixture = Application()
    def cleanup():
            fixture.destroy()
    # using request.addfinalizer(fixture.destroy()) causes method destroy()
    # to be invoked right in the set up, so additional function cleanup() was added to avoid that
    request.addfinalizer(cleanup)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="first", middlename="", lastname="last", nickname="nick",
    company="company", title="", address="", homePhone="+11111111111", mobilePhone="", workPhone="",
    fax="", email="", email2="", email3="", homePage="", birthDay="", birthMonth="", birthYear="",
    annDay="", annMonth="", annYear="", group="", secondaryAddress="", home="", notes=""))
    app.session.logout();
