from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicPage:
    START = (By.XPATH, "//button[normalize-space()='START']")
    STOP = (By.XPATH, "//button[normalize-space()='STOP']")
    
    def __init__(self, driver):
        self.driver = driver
        
    def click_start(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.START)
        ).click()
        
    def click_stop(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.STOP)
        ).click()
        
    def dynamic(self):
        self.click_start()
        self.click_stop()