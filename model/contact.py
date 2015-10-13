__author__ = 'IEUser'

from sys import maxsize


class Contact:
    def __init__(self, firstname = None, middlename = None, lastname = None, nickname = None, company = None, title = None,
                 address = None, homePhone = None, mobilePhone = None, workPhone = None,
                 fax = None, email = None, email2 = None, email3 = None, homePage = None, birthDay = None, birthMonth = None,
                 birthYear = None, annDay = None, annMonth = None, annYear = None, group = None,
                 secondaryAddress = None, home = None, notes = None, id = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname=nickname
        self.company = company
        self.title = title
        self.address = address
        self.homePhone = homePhone
        self.mobilePhone = mobilePhone
        self.workPhone = workPhone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homePage = homePage
        self.birthDay = birthDay
        self.birthMonth = birthMonth
        self.birthYear = birthYear
        self.annDay = annDay
        self.annMonth = annMonth
        self.annYear = annYear
        self.group = group
        self.secondaryAddress = secondaryAddress
        self.home = home
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize