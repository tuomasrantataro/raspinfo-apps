from datetime import datetime, date, time, timedelta

'''Parser for iCal data

Parses the needed data from iCal file into form which is useful for other apps.
This means mostly discarding data not needed, but also converting timestamps to
a standard form and removing extra whitespace and escape characters.'''

def _remove_past_events(events):
    '''Remove events which have ended from the list.
    
    Returns a list of dicts with only current and future events.'''
    raise NotImplementedError

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
    
    The iCal format accepts many different time representations.
    Change them all to a single standard for easier future use.
    The format used is "2012-04-23T18:25:43+00:00", which is commonly
    in use and follows ISO 8601. Offset (from timezone and DST) should
    be in format "±HH:MM"
    
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

def _sanitize_text(input):
    '''Sanitizes text fields.

    Removes extra whitespace and escape characters from the text given.

    When a whitespace character appears multiple times in row, leave only
    one, except in case of newline, leave two.
    
    When an escaped character (e.g. \') is found, transform to SQL-accepted
    form.
    
    Returns the sanitized text as a string.'''
    ret = ""
    prev = ''
    prev2 = ''
    for char in input:
        if not char.isspace():
            ret = ret + char
            prev2 = prev
            prev = char
        elif char != prev:
            ret = ret + char
            prev2 = prev
            prev = char
        elif char == '\n' and char == prev and prev != prev2:
            ret = ret + char
            prev2 = prev
            prev = char
    return ret

def parse(input):
    '''Top level function. Put the iCal file text here.
    
    Returns a list of dicts, where each dict is info about one event.'''
    raise NotImplementedError