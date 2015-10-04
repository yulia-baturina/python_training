# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new", header="header", footer="footer"))
    app.group.edit_first_group(Group(name="updated_name", header="new header", footer="new footer"))
