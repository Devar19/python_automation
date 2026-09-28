from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

iframe = wait.until(
    EC.presence_of_element_located((By.ID, "courses-iframe"))
)

driver.switch_to.frame(iframe)

learning_paths = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='learning-path']")
    )
)
learning_paths.click()

python_tab = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@data-id='python']")
    )
)
python_tab.click()

driver.switch_to.default_content()


original_window = driver.current_window_handle

open_tab = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Open Tab']")
    )
)
open_tab.click()

wait.until(EC.number_of_windows_to_be(2))

windows = driver.window_handles

for window in windows:
    if window != original_window:
        driver.switch_to.window(window)
        break
    
print("New tab title: ", driver.title)

time.sleep(5)
driver.close()

driver.switch_to.window(original_window)


time.sleep(5)
driver.quit()