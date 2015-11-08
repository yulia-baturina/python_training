# -*- coding: utf-8 -*-
from model.group import Group
import random

# def test_edit_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="new", header="header", footer="footer"))
#     old_groups = app.group.get_group_list()
#     group = Group(name="updated_name", header="new header", footer="new footer")
#     group.id = old_groups[0].id
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[0] = group
#     assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new", header="header", footer="footer"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group_index = old_groups.index(random_group)
    group = Group(name="updated group", header="updated header", footer="updated footer")
    group.id = random_group.id
    app.group.modify_group_by_id(group, random_group.id)
    new_groups = db.get_group_list()
    old_groups[group_index] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
