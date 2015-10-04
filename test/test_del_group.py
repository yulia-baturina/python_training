# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new", header="header", footer="footer"))
    app.group.delete_first_group()
