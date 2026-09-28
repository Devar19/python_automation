from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# Find child/descendant input elements
elements = driver.find_elements(By.CSS_SELECTOR, "form input")

print("Total input elements inside form:", len(elements))


for element in elements:
    print(
        "Tag:",
        element.tag_name,
        "| ID:",
        element.get_attribute("id"),
        "| Type:",
        element.get_attribute("type")
    )


time.sleep(5)

driver.quit()