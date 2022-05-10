import sys

sys.path.append('../')

from src import icalparser

class ParseTests(object):

    def sanitize_text(self, text):
        return icalparser._sanitize_text(text)