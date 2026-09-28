*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   chrome
${USERNAME}  standard_user
${PASSWORD}  secret_sauce


*** Test Cases ***
Verify Successful Login

    Open Browser
    ...    ${URL}
    ...    ${BROWSER}

    Maximize Browser Window

    Input Text
    ...    id=user-name
    ...    ${USERNAME}

    Input Text
    ...    id=password
    ...    ${PASSWORD}

    Click Button
    ...    id=login-button

    ${current_url}=    Get Location

    Log    Current URL: ${current_url}

    Should Contain
    ...    ${current_url}
    ...    inventory.html

    [Teardown]
    ...    Close All Browsers