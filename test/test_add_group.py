# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


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


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="new", header="header", footer="footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
