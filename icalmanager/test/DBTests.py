import sys

sys.path.append('../')

from src import dbmanager

class DBTests(object):

    def insert_test_data(self, db_filename, events):
        db = dbmanager.DBManager(db_filename)

        db.update_data(events)