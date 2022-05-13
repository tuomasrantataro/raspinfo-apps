import sys

sys.path.append('../')

from src import icalparser

class ParseTests(object):

    def transform_timestamp(self, offset, timestamp):
        return icalparser._transform_timestamp(offset, timestamp)

    def sanitize_text(self, text):
        return icalparser._sanitize_text(text)