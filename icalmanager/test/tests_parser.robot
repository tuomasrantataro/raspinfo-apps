*** Settings ***
Documentation   Tests for iCal parser
Resource        keywords.resource
Variables       parser_variables.py

*** Variables ***
&{Event 1}  SUMMARY=Abraham Lincoln  DTSTART=2008-02-12  DTEND=2008-02-13  LOCATION=Hodgenville, Kentucky
...         DESCRIPTION=Born February 12, 1809\nSixteenth President (1861-1865)\n\nhttp://AmericanHistoryCalendar.com
...         UID=c7614cff-3549-4a00-9152-d25cc1fe077d

*** Test Cases ***
Remove extra whitespace from text
    [Template]      The text ${original} should become ${sanitized}
    Remove many newlines \n\n\n\n\n removed?      Remove many newlines \n\n removed?
    Remove many newlines \n removed?              Remove many newlines \n removed?
    Remove \ \ \ \ extra \ \ \ spaces             Remove extra spaces
    Don\'t remove \n\t different whitespaces      Don\'t remove \n\t different whitespaces

Transform timestamps to ISO 8601 format
    [Template]      Ts ${orig_timestamp} should become ${ISO_8601_timestamp}
    20101016T134505             2010-10-16T13:45:05+00:00
    20101016T134505Z            2010-10-16T13:45:05+00:00
    20220515T143000             2022-05-15T14:30:00+00:00
    20220515T143000Z            2022-05-15T14:30:00+00:00

Transform timestamps to UTC
    [Template]      ${timestamp} with offset ${timezone_offset} should become ${UTC_timestamp}
    2004-10-09T11:04:23+01:00     +00:00        2004-10-09T10:04:23+00:00  # iso with tz data
    2004-10-09T11:04:23-01:00     +00:00        2004-10-09T12:04:23+00:00  # iso with negative tz data
    1992-04-13T08:08:13Z          +00:00        1992-04-13T08:08:13+00:00  # iso with Z marking UTC
    2004-04-04T18:23:00Z          +01:00        2004-04-04T17:23:00+00:00  # iso with Z marking UTC, with separate tz
    2004-04-04T18:23:00Z          -02:00        2004-04-04T20:23:00+00:00  # iso with Z marking UTC, with separate negative tz

Transform dates to ISO 8601 format
    [Template]      Date ${orig_date} should become ${ISO_8601_date}
    20020113              2002-01-13
    20200105              2020-01-06
    VALUE=DATE:20221010   2022-10-10

#TODO: add tests for daylight saving time

Create events from iCal file
    [Template]      Events from ${ics_file} should match with ${event}
    calendar_data.ics       @{CAL_ITEMS}

Remove past events