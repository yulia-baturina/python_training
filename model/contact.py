__author__ = 'IEUser'

from sys import maxsize
from fixture.stringUtils import StringsHelper


class Contact:
    def __init__(self, firstname="", middlename="", lastname="", nickname="", company="", title="",
                 address="", homePhone="", mobilePhone="", workPhone="", secondaryPhone="",
                 fax="", email="", email2="", email3="", homePage="", birthDay="", birthMonth="",
                 birthYear="", annDay="", annMonth="", annYear="", group="",
                 secondaryAddress="", home="", notes="", id=None, all_phones_from_home_page="",
                 all_emails_from_home_page=""):
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
        self.secondaryPhone = secondaryPhone
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
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        self_phones = self.get_all_phones_like_on_home_page()
        other_phones = other.get_all_phones_like_on_home_page()
        self_emails = self.get_all_emails_like_on_home_page()
        other_emails = other.get_all_emails_like_on_home_page()

        if not ((self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
            and self.lastname == other.lastname and self.address == other.address \
            and self_emails == other_emails and self_phones == other_phones):
            j=1

        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
            and self.lastname == other.lastname and self.address == other.address \
            and self_emails == other_emails and self_phones == other_phones

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def merge_phones_like_on_home_page(self):
        return "\n".join(map(lambda x: StringsHelper.clearPhone(x), filter(lambda x: x != "",
                                                               [self.homePhone, self.mobilePhone, self.workPhone, self.secondaryPhone])))

    def merge_emails_like_on_home_page(self):
        return "\n".join(filter(lambda x: x != "",
                                          [self.email, self.email2, self.email3]))

    def get_all_phones_like_on_home_page(self):
        if self.all_phones_from_home_page == "":
            return self.merge_phones_like_on_home_page()
        else:
            return self.all_phones_from_home_page

    def get_all_emails_like_on_home_page(self):
        if self.all_emails_from_home_page == "":
            return self.merge_emails_like_on_home_page()
        else:
            return self.all_emails_from_home_page