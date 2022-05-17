import sys

sys.path.append('../')

from src import icalparser

class ParseTests(object):

    def transform_timestamp(self, timestamp, offset=None):
        if offset == None:
            return icalparser._transform_timestamp(timestamp)
        else:
            return icalparser._transform_timestamp(timestamp, offset)

    def sanitize_text(self, text):
        return icalparser._sanitize_text(text)