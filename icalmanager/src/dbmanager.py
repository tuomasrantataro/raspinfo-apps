'''Manages iCal data in a SQLite database.

Calendar events are saved to a database for other software to consume.
This module adds, updates and removes events from calendars.

Calendar data:
    "calendar":     Calendar name which contains the event
    "uid":          Unique identifier for the event
    "dtstart":      Event start timestamp
    "dtend":        Event end timestamp
    "summary":      One-line title for the event
    "description":  Longer description about the event
    "location":     Event location as a text string
    "rrule":        Repeat rule for repeating events'''

class DBManager():

    def __init__(self, db_file):
        '''
        Inputs:
            db_file:    Location of the SQLite database file'''
        raise NotImplementedError

    def update_data(self, event_data):
        '''Add or update events in the database.
        
        Inputs:
            event_data: list of dicts containing an event each'''
        raise NotImplementedError

    def clear_past_events(self):
        '''Remove events which have passed.'''
        raise NotImplementedError