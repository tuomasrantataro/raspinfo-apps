'''Fill database with event data'''

import json
import requests

import icalparser
import dbmanager

if __name__ == "__main__":
    '''
    1. Get database location and iCalendar(.ics) file url(s) from config.JSON
    2. Download an .ics file
    3. Transform the .ics file into a list of dicts containing event data
    4. Add events to list to be inserted into database
    5. Go back to step 2 with next calendar url
    6. Add the events to database'''

    with open('../config.JSON', 'r') as f:
        data = json.load(f)

    db_path = data['settings']['dblocation']
    print('db path:', db_path)

    cals = []
    for item in data['calendars']:
        name = item['name']
        url = item['url']
        cals.append((name, url))

    db_events = []
    for item in cals:
        response = requests.get(item[1])

        events = icalparser.parse(response.content.decode('utf-8'))

        for event in events:
            event['CALENDAR'] = item[0]
            db_events.append(event)

    db = dbmanager.DBManager(db_path)
    db.update_data(db_events)
