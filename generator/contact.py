__author__ = 'IEUser'
from model.contact import Contact
from fixture.stringUtils import StringsHelper
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o=="-n":
        n = int(a)
    elif o=="-f":
        f = a

testdata = [Contact()] + [
Contact(firstname=StringsHelper.randomstring("firstname", 10), lastname=StringsHelper.randomstring("lastname", 20),
          nickname=StringsHelper.randomstring("nickname", 20), company=StringsHelper.randomstring("company", 5),
        homePhone=StringsHelper.randomPhone("+",7), email=StringsHelper.randomstring("email", 10).join("mail.com"))
    for i in range(5)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
