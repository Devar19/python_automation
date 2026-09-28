from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

element1 = driver.find_element(By.CSS_SELECTOR, "#name")

element1.send_keys("Devarshi")

print("Element found using ID CSS selector")

elements = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

print("Text input elements:", len(elements))

elements = driver.find_elements(By.CSS_SELECTOR, "[id^='date']")

print("IDs starting with 'date':", len(elements))


elements = driver.find_elements(By.CSS_SELECTOR, "[id*='date']")

print("IDs containing 'date':", len(elements))


time.sleep(5)

driver.quit()