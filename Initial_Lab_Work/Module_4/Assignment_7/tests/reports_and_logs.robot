*** Settings ***
Library    SeleniumLibrary

Test Setup       Open Browser And Login
Test Teardown    Close Test Browser


*** Variables ***
${URL}          https://www.saucedemo.com/
${BROWSER}      chrome
${USERNAME}     standard_user
${PASSWORD}     secret_sauce


*** Test Cases ***
Verify Inventory Page

    Log    Starting inventory page verification.
    Log    Username used: ${USERNAME}

    Page Should Contain Element
    ...    id=inventory_container

    Log    Inventory page was successfully verified.


Verify Products Section

    Log    Starting products section verification.

    Page Should Contain
    ...    Products

    Log    Products section was successfully verified.


Verify Shopping Cart

    Log    Starting shopping cart verification.

    Page Should Contain Element
    ...    id=shopping_cart_container

    Log    Shopping cart was successfully verified.


*** Keywords ***
Open Browser And Login

    Log    Opening SauceDemo browser.

    Open Browser
    ...    ${URL}
    ...    ${BROWSER}

    Maximize Browser Window

    Log    Entering username.

    Input Text
    ...    id=user-name
    ...    ${USERNAME}

    Log    Entering password.

    Input Text
    ...    id=password
    ...    ${PASSWORD}

    Log    Clicking login button.

    Click Button
    ...    id=login-button

    Page Should Contain Element
    ...    id=inventory_container

    Log    Login completed successfully.


Close Test Browser

    Log    Closing browser and cleaning up.

    Close All Browsers