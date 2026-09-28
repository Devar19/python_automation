from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Click Simple Alert button
driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Simple Alert']"
).click()

# Switch to alert
alert = driver.switch_to.alert

# Print alert message
print("Alert message:", alert.text)
time.sleep(2)

# Accept the alert
alert.accept()

# Click Confirmation Alert button
driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Confirmation Alert']"
).click()

# Switch to confirmation box
confirm = driver.switch_to.alert

# Print confirmation message
print("Confirm message:", confirm.text)
time.sleep(2)

# Dismiss confirmation box
confirm.dismiss()

# Click Prompt Alert button
driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Prompt Alert']"
).click()

# Switch to prompt
prompt = driver.switch_to.alert

# Print prompt message
print("Prompt message:", prompt.text)

# Enter text into prompt
prompt.send_keys("Devarshi")
time.sleep(2)

# Accept/submit prompt
prompt.accept()

# Keep browser open for demonstration
time.sleep(5)

driver.quit()