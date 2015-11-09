# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_add_random_contact_to_random_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="new", header="header", footer="footer"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="first", lastname="last", nickname="nick",
    company="company", homePhone="+11111111111", email="mail@mail.com"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    group_index = groups.index(group)
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.assign_contact_by_id_to_group(contact.id, group.name)
    new_groups = orm.get_group_list()
    new_group = new_groups[group_index]
    new_contacts_in_group = orm.get_contacts_in_group(new_group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

def test_add_and_remove_random_contact_from_random_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="new", header="header", footer="footer"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="first", lastname="last", nickname="nick",
    company="company", homePhone="+11111111111", email="mail@mail.com"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    group_index = groups.index(group)
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    app.contact.assign_contact_by_id_to_group(contact.id, group.name)
    old_groups = orm.get_group_list()
    old_group = old_groups[group_index]
    old_contacts_in_group = orm.get_contacts_in_group(old_group)
    app.group.remove_contact_by_id_from_group(contact.id)
    new_groups = orm.get_group_list()
    new_group = new_groups[group_index]
    new_contacts_in_group = orm.get_contacts_in_group(new_group)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

