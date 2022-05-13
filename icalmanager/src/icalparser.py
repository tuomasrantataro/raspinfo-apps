'''Parser for iCal data

Parses the needed data from iCal file into form which is useful for other apps.
This means mostly discarding data not needed, but also converting timestamps to
a standard form and removing extra whitespace and escape characters.'''

def _remove_past_events(events):
    '''Remove events which have ended from the list.
    
    Returns a list of dicts with only current and future events.'''
    raise NotImplementedError

def _transform_timestamp(timestamp, offset="00:00"):
    '''Transforms timestamps to standard form and UTC time.
    
    The iCal format accepts many different time representations.
    Change them all to a single standard for easier future use.
    The format used is "2012-04-23T18:25:43.511Z", which is commonly
    in use and follows ISO 8601. Offset (from timezone and DST) should
    be in format "±HH:MM"
    
    Returns timestamp as a string.'''
    raise NotImplementedError

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