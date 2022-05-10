*** Settings ***
Library     ParseTests.py

*** Keywords ***
The text ${original} should become ${sanitized}
    ${result} =     Sanitize Text       ${original}
    Should Be Equal     ${result}       ${sanitized}