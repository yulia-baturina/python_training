from pytest_bdd import scenario
from .contact_steps import *

@scenario("contacts.feature","add new contact")
def test_add_new_contact():
    pass

@scenario("contacts.feature","delete a contact")
def test_delete_contact():
    pass

@scenario("contacts.feature","update a contact")
def test_update_contact():
    pass