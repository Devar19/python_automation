*** Settings ***
Library    RequestsLibrary


*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com


*** Test Cases ***
Verify Users API Response

    ${response}=    GET
    ...    ${BASE_URL}/users/1

    Log    Status Code: ${response.status_code}
    Log    Response: ${response.text}

    Should Be Equal As Strings
    ...    ${response.status_code}
    ...    200

    Should Contain
    ...    ${response.text}
    ...    "id"

    Should Contain
    ...    ${response.text}
    ...    "username"