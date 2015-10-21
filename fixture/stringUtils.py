__author__ = 'IEUser'
import re

class StringsHelper:

    def clearPhone(s):
        return re.sub("[() -]","",s)