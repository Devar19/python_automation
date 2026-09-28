from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverFactory:
    
    @staticmethod
    def create_driver(browser):
        browser = browser.lower()
        
        if browser == "chrome":
            options = Options()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)
            
        elif browser == "firefox":
            driver = webdriver.Firefox()
            
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        return driver