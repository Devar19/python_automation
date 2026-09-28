from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

element1 = driver.find_element(By.ID, "name")
element1.send_keys("Devarshi")

element2 = driver.find_element(By.NAME, "Cross-Column")
print("Element found using NAME:", element2)

inputs = driver.find_elements(By.TAG_NAME, "input")
print("Total number of input elements:", len(inputs))

home_link = driver.find_element(By.LINK_TEXT, "Home")
print("Home link text:", home_link.text)

element3 = driver.find_element(By.CLASS_NAME, "form-control")
print("Element found using CLASS_NAME:", element3)

home_link.click()

time.sleep(10)

driver.quit()