from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


links = driver.find_elements(By.TAG_NAME, "a")


print("Total links:", len(links))


for link in links:
    print(link.text)


time.sleep(5)

driver.quit()