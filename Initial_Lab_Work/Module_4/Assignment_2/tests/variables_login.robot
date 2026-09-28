*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}          https://www.saucedemo.com/
${USERNAME}     standard_user
${PASSWORD}     secret_sauce
${BROWSER}      chrome

*** Test Cases ***
Login Using Variables

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

    Page Should Contain Element
    ...    id=inventory_container

    [Teardown]
    ...    Close All Browsers