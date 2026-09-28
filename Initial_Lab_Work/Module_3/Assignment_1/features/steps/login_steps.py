from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given("I am on the SauceDemo login page")
def open_login_page(context):
    context.driver.get("https://saucedemo.com/")
    
@when("I enter the valid username")
def enter_username(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
@when("I enter the valid password")
def enter_password(context):
    context.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    
@when("I click the login button")
def click_login(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()
    
@then("I should be redirected to the inventory page")
def verify_inventory(context):
    assert "/inventory.html" in  context.driver.current_url