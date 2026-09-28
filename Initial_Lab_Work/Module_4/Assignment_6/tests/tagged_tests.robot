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
    [Tags]    smoke    login
    Page Should Contain Element    id=inventory_container
    Log    Inventory page verified.


Verify Products Section
    [Tags]    regression    products
    Page Should Contain    Products
    Log    Products section verified.


Verify Shopping Cart
    [Tags]    regression    cart
    Page Should Contain Element    id=shopping_cart_container
    Log    Shopping cart verified.


Verify Menu Button
    [Tags]    smoke    navigation
    Page Should Contain Element    id=react-burger-menu-btn
    Log    Menu button verified.


*** Keywords ***
Open Browser And Login

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


Close Test Browser

    Close All Browsers