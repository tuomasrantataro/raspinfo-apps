*** Settings ***
Library     ParseTests.py

*** Keywords ***
The text ${original} should become ${sanitized}
    ${result} =     Sanitize Text       ${original}
    Should Be Equal     ${result}       ${sanitized}


Ts ${orig_timestamp} with offset ${timezone_offset} should become ${ISO_8601_timestamp}
    ${timestamp_result} =     Transform Timestamp       ${orig_timestamp}   ${timezone_offset} 
    Should Be Equal     ${timestamp_result}     ${ISO_8601_timestamp}