*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
SauceDemo Login Page Basic Automation

    Open Browser
    ...    https://www.saucedemo.com/
    ...    chrome

    Maximize Browser Window

    Page Should Contain Element
    ...    id=user-name

    Page Should Contain Element
    ...    id=password

    Page Should Contain Element
    ...    id=login-button

    Input Text
    ...    id=user-name
    ...    standard_user

    Input Text
    ...    id=password
    ...    secret_sauce

    [Teardown]
    ...    Close All Browsers