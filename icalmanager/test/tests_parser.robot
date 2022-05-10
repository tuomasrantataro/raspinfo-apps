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
