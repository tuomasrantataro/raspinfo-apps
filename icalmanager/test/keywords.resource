*** Settings ***
Library     ParseTests.py

*** Keywords ***
The text ${original} should become ${sanitized}
    ${result} =     Sanitize Text       ${original}
    Should Be Equal     ${result}       ${sanitized}


Ts ${orig_timestamp} should become ${ISO_8601_timestamp}
    ${timestamp_iso_result} =   Transform Timestamp     ${orig_timestamp}
    Should Be Equal     ${timestamp_iso_result}     ${ISO_8601_timestamp}


${timestamp} with offset ${timezone_offset} should become ${UTC_timestamp}
    ${timestamp_utc_result} =   Transform Timestamp       ${timestamp}   ${timezone_offset} 
    Should Be Equal     ${timestamp_utc_result}     ${UTC_timestamp}


Date ${orig_date} should become ${ISO_8601_date}
    ${date_result} =    Transform Timestamp     ${ISO_8601_date}
    Should Be Equal     ${date_result}      ${ISO_8601_date}


Events from ${ics_file} should match with ${event}
    @{event_list} =     Parse   ${ics_file}
    FOR     ${index}    ${event_item}   IN ENUMERATE    @{event_list}
        FOR     ${event_data_key}   ${event_data}   IN  &{event_item}
            Should Be Equal     ${event_list}[${index}][${event_data_key}]   ${event}[${index}][${event_data_key}]
        END
    END