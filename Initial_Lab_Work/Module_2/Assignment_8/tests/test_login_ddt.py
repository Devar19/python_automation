import pandas as pd
import pytest
from selenium import webdriver
from pages.login_page import LoginPage


data = pd.read_csv("data/login_data.csv")

test_data = [
    (
        row["username"],
        row["password"],
        row["expected_result"],
        row["expected_message"]
    )
    for _, row in data.iterrows()
]


@pytest.mark.parametrize(
    "username,password,expected_result,expected_message",
    test_data
)
def test_login_ddt(
    username,
    password,
    expected_result,
    expected_message
):

    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        login_page = LoginPage(driver)

        login_page.login(username, password)

        if expected_result == "success":

            assert "/inventory.html" in driver.current_url

        elif expected_result == "error":

            error_message = login_page.get_error_message()

            assert expected_message in error_message

    finally:
        driver.quit()