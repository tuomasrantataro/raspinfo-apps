*** Settings ***
Documentation   Tests for submitting event data to SQLite database
Library         RPA.Database
Library         OperatingSystem
Library         DBTests.py
Variables       db_variables.py
Test Setup      Connect To Database    sqlite3    ${DB_FILE_NAME}
Test Teardown   Remove File    ${DB_FILE_NAME}

*** Test Cases ***
Verify Data Insertion
    Insert Test Data    ${DB_FILE_NAME}    ${CAL_ITEMS} 
    @{rows} =    Get Rows    events 
    Should Be Equal    ${rows}    ${CAL_ITEMS}
    

#No Past Events in Database