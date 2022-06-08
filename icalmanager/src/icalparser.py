from datetime import datetime, date, time, timedelta, timezone

'''Parser for iCal data

Parses the needed data from iCal file into form which is useful for other apps.
This means mostly discarding data not needed, but also converting timestamps to
a standard form and removing extra whitespace and escape characters.'''

__name__ = 'icalparser'

def _remove_past_events(events):
    '''Remove events which have ended from the list.
    
    Returns a list of dicts with only current and future events.'''
    ret = []
    for item in events:
        dt = datetime.fromisoformat(item['DTEND'])
        dt_ = datetime.combine(dt.date(), dt.time(), timezone.utc)

        if dt_ >= datetime.now(timezone.utc):
            ret.append(item)
            
    return ret

def _timestamp_to_datetime(timestamp):
    '''Create date/datetime object from string.
    
    Detect some common timestamp string types and convert
    them to a date or datetime object
    
    Returns a datetime or date object.'''

    date_ = None
    time_ = None

    try:
        parts = timestamp.split('T')
        try:
            date_ = datetime.strptime(parts[0], '%Y%m%d')
        except ValueError:
            raise
        try:
            time_ = datetime.strptime(parts[1], '%H%M%S')
        except ValueError:
            raise

    except IndexError:
        try:
            date_ = datetime.strptime(timestamp, '%Y%m%d')
        except ValueError:
            raise

    if time_ == None:
        return date(date_.year, date_.month, date_.day)
    else:
        return datetime(date_.year, date_.month, date_.day, time_.hour, time_.minute, time_.second)

def _transform_timestamp(timestamp, offset="+00:00"):
    '''Transforms timestamps to standard form and UTC time.
    
    The iCal format accepts many different time representations. Change them
    all to a single standard for easier future use. The format used is
    "2012-04-23T18:25:43+00:00", which is commonly in use and follows ISO 8601.
    Offset (from timezone and DST) should be in format "±HH:MM". In case of
    all-day events, the timestamp format is "2012-04-23"
    
    Returns timestamp as a string.'''
    
    timestamp = timestamp.removeprefix("VALUE=DATE:")
    timestamp = timestamp.removesuffix("Z")

    try:
        t = date.fromisoformat(timestamp)
    except ValueError:
        try:
            t_ = datetime.fromisoformat(timestamp)

            # convert to utc
            os_ = t_.utcoffset()
            if os_ == None:
                os = timedelta()
            else:
                os = t_.utcoffset()
            t_ = t_ - os
            t = datetime(t_.year, t_.month, t_.day, t_.hour, t_.minute, t_.second)
        except ValueError:
            t = _timestamp_to_datetime(timestamp)

    if isinstance(t, datetime):
        offset_ = time.fromisoformat('00'+offset)
        t = t - offset_.utcoffset()

        return t.isoformat() + "+00:00"
    else:
        return t.isoformat()

def _fix_escapes(input):
    '''Change escaped characters in text to real escaped characters'''
    ret = ''
    prev = ''

    for char in input:
        if char == '\\' and prev == '\\':
            ret = ret + '\\'
        elif char == 'n' and prev == '\\':
            ret = ret + '\n'
        elif char == 't' and prev == '\\':
            ret = ret + '\t'
        elif char == 'r' and prev == '\\':
            ret = ret
        elif char == '\\':
            # Escaped some character which python handles fine, remove escape backslash
            ret = ret
        else:
            ret = ret + char
        prev = char

    return ret

def _remove_extra_whitespace(input):
    ret = ""
    prev = ''
    prev2 = ''

    for char in input:
        if not char.isspace():
            ret = ret + char
            prev2 = prev
            prev = char
        elif char != prev:
            # not the same (whitespace) character after each other
            ret = ret + char
            prev2 = prev
            prev = char
        elif char == '\n' and char == prev:
            # Allow two whitespaces after each other
            if prev2 != '\n':
                # Don't allow more than two
                ret = ret + char
            prev2 = prev
            prev = char
        else:
            # Two (or more) of any other same whitespace after each other
            prev2 = prev
            prev = char

    return ret
    

def _sanitize_text(input):
    '''Sanitizes text fields.

    Removes extra whitespace and escape characters from the text given.

    When a whitespace character appears multiple times in row, leave only one,
    except in case of newline, leave two.
    
    When an escaped character (e.g. \') is found, leave only escapes which are
    needed in Python
    
    Returns the sanitized text as a string.'''

    input = _fix_escapes(input)

    input = _remove_extra_whitespace(input)

    return input

def _lines_to_list(input_file) -> list[str]:
    lines = []
    partial = ''
    for line in input_file.readline():
        if line != '\n':
            partial = partial + line
        else:
            lines.append(partial)
            partial = ''

    combined = []
    for item in lines:
        if item.startswith(' '):
            combined[-1] = combined[-1] + item.lstrip()
        else:
            combined.append(item)
    
    return combined

def _parse_event(event_data : list([str, str])) -> dict[str : str]:
    ret = {}
    keys = ['UID', 'DTSTART', 'DTEND', 'SUMMARY', 'DESCRIPTION', 'LOCATION']

    for item in event_data:
        if item[0] in keys:
            if item[0] in ['DTSTART', 'DTEND']:
                item[1] = _transform_timestamp(item[1])
            if item[0] in ['SUMMARY', 'DESCRIPTION', 'LOCATION']:
                item[1] = _sanitize_text(item[1])
            ret[item[0]] = item[1]

    return ret

def parse(input_file):
    '''Top level function. Put the iCal file here.

    input_file:
    Opened iCal (.ics) file 
    
    Returns a list of dicts, where each dict is info about one event.'''
    ret = []

    event_data = []
    reading_event = False

    lines = _lines_to_list(input_file)
    for item in lines:

        parts = item.split(';', maxsplit=1)
        if len(parts) == 1:
            parts = item.split(':', maxsplit=1)
        
        if item == 'BEGIN:VEVENT':
            reading_event = True
            event_data = []
        elif item == 'END:VEVENT':
            reading_event = False
            parsed = _parse_event(event_data)
            ret.append(parsed)
        elif reading_event == True:
            event_data.append([parts[0], parts[1]])
    
    return ret