*** Settings ***
Documentation   Tests for iCal parser
Resource        keywords.resource

*** Test Cases ***
Remove extra whitespace from text
    [Template]      The text ${original} should become ${sanitized}
    "Remove many newlines \n\n\n\n\n removed?"      "Remove many newlines \n\n removed?"
    "Remove many newlines \n removed?"              "Remove many newlines \n removed?"
    "Remove \ \ \ \ extra \ \ \ spaces"             "Remove extra spaces"
    "Don\'t remove \n\t different whitespaces"      "Don\'t remove \n\t different whitespaces"


Transform timestamps to standard format
    [Template]      Ts ${orig_timestamp} with offset ${timezone_offset} should become ${ISO_8601_timestamp}
    "20020113"                      "00:00"         "20020113T00:00:00.000Z"
    "20101016T13:45:05.001"         "-03:00"        "20101016T10:45:05.001Z"
    "20200105"                      "+02:00"        "20200106T02:00:00.000Z"
    "VALUE=DATE:20221010"           "00:00"         "20221010T00:00:00.000Z"