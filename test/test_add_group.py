# -*- coding: utf-8 -*-
from model.group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new", header="header", footer="footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
