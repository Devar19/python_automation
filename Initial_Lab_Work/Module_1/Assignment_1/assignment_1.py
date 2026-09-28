from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

button = driver.find_element(By.XPATH, "//input[@value='Login']")
button.click()

WebDriverWait(driver, 10).until(
    EC.url_contains("/inventory.html")
)

assert "/inventory.html" in driver.current_url, "Sign In failed or did not redirect to the expected page."

print("Sign In Successful!")
print("Current URL:", driver.current_url)

driver.quit()