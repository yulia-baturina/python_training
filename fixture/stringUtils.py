__author__ = 'IEUser'
import re
import random
import string


class StringsHelper:
    def clearPhone(s):
        return re.sub("[() -]", "", s)

    def randomstring(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def randomPhone(prefix, maxlen):
        return prefix + "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])