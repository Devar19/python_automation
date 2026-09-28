*** Settings ***
Library    SeleniumLibrary

Test Setup       Open Browser And Login
Test Teardown    Logout And Close Browser


*** Variables ***
${URL}          https://www.saucedemo.com/
${BROWSER}      chrome
${USERNAME}     standard_user
${PASSWORD}     secret_sauce


*** Test Cases ***
Verify Inventory Page

    Page Should Contain Element
    ...    id=inventory_container

    Log    Inventory page is displayed successfully.


Verify Products Page

    Page Should Contain
    ...    Products

    Log    Products text is displayed successfully.


Verify Shopping Cart

    Page Should Contain Element
    ...    id=shopping_cart_container

    Log    Shopping cart is displayed successfully.


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


Logout And Close Browser

    Click Button
    ...    id=react-burger-menu-btn

    Wait Until Element Is Visible
    ...    id=logout_sidebar_link
    ...    timeout=10s

    Click Link
    ...    id=logout_sidebar_link

    Close All Browsers