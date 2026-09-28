from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

dynamic_element_1 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//button[normalize-space()='START']")
))

print("Dynamic element text:", dynamic_element_1.text)
dynamic_element_1.click()

time.sleep(3)

dynamic_element_2 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//button[normalize-space()='STOP']")
))

print("Dynamic element text:", dynamic_element_2.text)

time.sleep(3)

dynamic_element_2.click()

time.sleep(1)
driver.quit()