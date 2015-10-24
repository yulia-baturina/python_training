__author__ = 'IEUser'
from model.group import Group
from fixture.stringUtils import StringsHelper
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o=="-n":
        n = int(a)
    elif o=="-f":
        f = a

testdata = [Group(name="", header="", footer="")] + [
    Group(name=StringsHelper.randomstring("name", 10), header=StringsHelper.randomstring("header", 20),
          footer=StringsHelper.randomstring("footer", 20))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
