from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutomationPage:
    
    # Locators
    
    OPTION1_CHECKBOX = (By.XPATH, "//input[@value='option1']")
    OPTION3_CHECKBOX = (By.XPATH, "//input[@value='option3']")
    
    DROPDOWN = (By.XPATH, "//select[@id='dropdown-class-example']")
    
    AUTOCOMPLETE = (By.ID, "autocomplete")
    
    SUGGESTIONS = (By.CSS_SELECTOR, "li.ui-menu-item")
    
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        
    # Checkbox methods
    
    def select_option1(self):
        self.driver.find_element(*self.OPTION1_CHECKBOX).click()
        
    def select_option3(self):
        self.driver.find_element(*self.OPTION3_CHECKBOX).click()
        
    def is_option1_selected(self):
        return self.driver.find_element(*self.OPTION1_CHECKBOX).is_selected()
    
    def is_option3_selected(self):
        return self.driver.find_element(*self.OPTION3_CHECKBOX).is_selected()
    
    
    # Dropdown method
    
    def select_dropdown_option(self, value):
        dropdown = self.driver.find_element(*self.DROPDOWN)
        Select(dropdown).select_by_value(value)
        
    
    # Autocomplete methods
    
    def enter_autocomplete(self, text):
        autocomplete = self.driver.find_element(*self.AUTOCOMPLETE)
        autocomplete.clear()
        autocomplete.send_keys(text)
        
    def get_suggestions(self):
        return self.wait.until(
            EC.visibility_of_all_elements_located(
                self.SUGGESTIONS
            )
        )
        
    def select_autocomplete_option(self, option):
        suggestions = self.get_suggestions()
        
        for suggestion in suggestions:
            print("Suggestion: ", suggestion.text)
            
            if suggestion.text == option:
                suggestion.click()
                return
            
        raise Exception(
            f"Autocomplete option '{option}' was not found"
        )