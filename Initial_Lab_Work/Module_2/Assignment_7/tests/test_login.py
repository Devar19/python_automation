from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://sauce-demo.myshopify.com/account/login")
    
    login_page = LoginPage(driver)
    login_page.enter_email("standard_user")
    login_page.enter_password("secret-sauce")
    login_page.click_login()
    
    assert "/account" in driver.current_url
    
    driver.quit()