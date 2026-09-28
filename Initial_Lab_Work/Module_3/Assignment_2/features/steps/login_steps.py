from behave import given, when, then
from selenium.webdriver.common.by   import By

@given('I am on the SauceDemo login page')
def open_login_page(context):
    context.driver.get("https://www.saucedemo.com/")
    
@when('I enter username "{username}"')
def enter_username(context, username):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    
@when('I enter password "{password}"')
def enter_password(context, password):
    context.driver.find_element(By.NAME, "password").send_keys(password)
    
@when('I click the login button')
def click_login(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()
    
@then('the login result should be "{result}"')
def verify_login_result(context, result):
    if result == "success":
        assert "/inventory.html" in context.driver.current_url
    
    elif result == "error":
        error_message = context.driver.find_element(
            By.XPATH, "//h3[@data-test='error']"
        )
        assert error_message.is_displayed()
        
    else:
        raise ValueError(f"Unknown expected result: {result}")