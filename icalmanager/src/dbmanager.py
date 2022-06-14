'''Manages iCal data in a SQLite database.

Calendar events are saved to a database for other software to consume.
This module adds, updates and removes events from calendars.

Calendar data:
    "uid":          Unique identifier for the event
    "summary":      One-line title for the event
    "dtstart":      Event start timestamp
    "dtend":        Event end timestamp
    "location":     Event location as a text string
    "description":  Longer description about the event
    "calendar":     Calendar name which contains the event'''

import sqlite3

class DBManager():

    def __init__(self, db_file):
        '''
        Inputs:
            db_file:    Location of the SQLite database file'''
            
        self.con = sqlite3.connect(db_file)
        cur = self.con.cursor()
        try:
            cur.execute("CREATE TABLE events (UID TEXT, SUMMARY TEXT, DTSTART DATE, DTEND DATE, LOCATION TEXT, DESCRIPTION TEXT, CALENDAR TEXT);")
        except sqlite3.OperationalError as err:
            if str(err) == "table events already exists":
                pass
            else:
                raise

    def __del__(self):
        self.con.close()

    def update_data(self, event_data):
        '''Add or update events in the database.

        #TODO: Create less naive system for updating already existing events than dropping the whole table every time
        
        Inputs:
            event_data: list of dicts containing an event each'''
        
        cur = self.con.cursor()
        try:
            cur = cur.execute("DROP TABLE events")
            cur = cur.execute("CREATE TABLE events (UID TEXT, SUMMARY TEXT, DTSTART DATE, DTEND DATE, LOCATION TEXT, DESCRIPTION TEXT, CALENDAR TEXT);")
        except:
            raise
        
        event_list = []
        for item in event_data:
            tup = (item['UID'],
                   item['SUMMARY'],
                   item['DTSTART'],
                   item['DTEND'],
                   item['LOCATION'],
                   item['DESCRIPTION'],
                   item['CALENDAR']
            )
            event_list.append(tup)

        cur = self.con.cursor()
        try:
            cur.executemany("INSERT INTO events(UID, SUMMARY, DTSTART, DTEND, LOCATION, DESCRIPTION, CALENDAR) VALUES(?, ?, ?, ?, ?, ?, ?)", event_list)
        except:
            raise
        
        self.con.commit()

    def clear_past_events(self):
        '''Remove events which have passed.'''
        raise NotImplementedError