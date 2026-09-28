from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

import time


browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
else:
    raise Exception("Invalid browser name.")


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

option1 = driver.find_element(By.XPATH, "//input[@value='option1']")
option3 = driver.find_element(By.XPATH, "//input[@value='option3']")

option1.click()
option3.click()

print("Option 1 is selected:", option1.is_selected())
print("Option 3 is selected:", option3.is_selected())

# Locating the dropdown
dropdown = driver.find_element(
    By.XPATH, "//select[@id='dropdown-class-example']"
)

# Selecting Options from dropdown
Select(dropdown).select_by_value("option1")
time.sleep(2)
Select(dropdown).select_by_value("option2")
time.sleep(2)
Select(dropdown).select_by_value("option3")

autocomplete = driver.find_element(By.ID, "autocomplete")
autocomplete.send_keys("Ind")

suggestions = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "li.ui-menu-item")
    )
)

for suggestion in suggestions:
    print("Suggestion:", suggestion.text)
    if suggestion.text == "India":
        suggestion.click()
        break

time.sleep(6)
driver.quit()