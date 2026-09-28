import pytest

from utils.csv_reader import CSVReader
from utils.credentials import CredentialReader

from pages.login_page import LoginPage
from pages.account_page import AccountPage


test_data = CSVReader.read_test_data("login_data.csv")


@pytest.mark.parametrize("data", test_data)
def test_login(data, driver, config):

    driver.get(config.get_application_url())

    login_page = LoginPage(
        driver,
        timeout=config.get_timeout()
    )

    login_page.open_login_page()

    if data["password_type"] == "valid":
        password = CredentialReader.get_valid_password()

    elif data["password_type"] == "invalid":
        password = CredentialReader.get_invalid_password()

    else:
        raise ValueError(
            f"Unknown password_type: "
            f"{data['password_type']}"
        )

    login_page.login(
        data["email"],
        password
    )

    account_page = AccountPage(
        driver,
        timeout=config.get_timeout()
    )

    account_page_displayed = (
        account_page.is_account_page_displayed()
    )

    print("\n--- Login Diagnostics ---")
    print("Email:", data["email"])
    print("Expected result:", data["expected_result"])
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)
    print(
        "Account page displayed:",
        account_page_displayed
    )

    if data["expected_result"] == "success":

        assert account_page_displayed, (
            "Expected successful login, "
            "but Account page was not displayed."
        )

    elif data["expected_result"] == "failure":

        assert not account_page_displayed, (
            "Expected login failure, "
            "but Account page was displayed."
        )

    else:
        raise ValueError(
            f"Unknown expected_result: "
            f"{data['expected_result']}"
        )