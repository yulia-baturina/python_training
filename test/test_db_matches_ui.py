__author__ = 'IEUser'
from model.group import Group
from model.contact import Contact
from timeit import timeit

def test_groups_list(app, db):
    ui_list = app.group.get_group_list()
    # print(timeit(lambda: ui_list, number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    # print(timeit(lambda:map(clean, db.get_group_list()), number=1000))
    db_list = list(map(clean, db.get_group_list()))
    assert sorted(ui_list, key=Group.id_or_max)==sorted(db_list, key=Group.id_or_max)

def test_contacts_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = db.get_contact_list()
    assert sorted(ui_list, key=Contact.id_or_max)==sorted(db_list, key=Contact.id_or_max)