from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.automation_page import AutomationPage

def test_automation():
    browsername = "chrome"
    
    if browsername.lower() == "chrome":
        driver = webdriver.Chrome(
            service = ChromeService(
                ChromeDriverManager().install()
            )
        )
    
    elif browsername.lower() == "firefox":
        driver = webdriver.Firefox(
            service = FirefoxService(
                GeckoDriverManager().install()
            )
        )
        
    else:
        raise Exception("Invalid browser name")
    
    try:
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        
        automation_page = AutomationPage(driver)
        
        # Checkboxes
        
        automation_page.select_option1()
        automation_page.select_option3()
        
        print("Option 1 is selected: ", automation_page.is_option1_selected())
        print("Option 3 is selected: ", automation_page.is_option3_selected())
        
        # Assertions
        assert automation_page.is_option1_selected()
        assert automation_page.is_option3_selected()
        
        # Dropdown
        
        automation_page.select_dropdown_option("option1")
        automation_page.select_dropdown_option("option2")
        automation_page.select_dropdown_option("option3")
        
        # Autocomplete
        
        automation_page.enter_autocomplete("Ind")
        automation_page.select_autocomplete_option("India")
        
    finally:
        driver.quit()