from selenium import webdriver
from pages.dynamic_page import DynamicPage

def test_dynamic():
    driver = webdriver.Chrome()
    try:
        driver.get("https://testautomationpractice.blogspot.com/")
        
        dynamic_page = DynamicPage(driver)
        dynamic_page.dynamic()
    
    finally:
        driver.quit()