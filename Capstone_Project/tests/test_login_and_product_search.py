import pytest

from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.product_page import ProductPage

from utils.csv_reader import CSVReader
from utils.credentials import CredentialReader


login_data = CSVReader.read_test_data(
    "login_data.csv"
)[0]

product_data = CSVReader.read_test_data(
    "product_data.csv"
)


@pytest.mark.integration
@pytest.mark.parametrize(
    "product",
    product_data,
    ids=lambda data: data["product"]
)
def test_login_then_search_product(
    product,
    driver,
    config
):

    # 1. Open application
    driver.get(
        config.get_application_url()
    )

    # 2. Login
    login_page = LoginPage(
        driver,
        timeout=config.get_timeout()
    )

    login_page.open_login_page()

    # 3. Retrieve password securely
    password = CredentialReader.get_valid_password()

    login_page.login(
        login_data["email"],
        password
    )

    # 4. Verify successful login
    account_page = AccountPage(
        driver,
        timeout=config.get_timeout()
    )

    account_page_displayed = (
        account_page.is_account_page_displayed()
    )

    print("\n--- Integration Login Diagnostics ---")
    print("Product:", product["product"])
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)
    print(
        "Account page displayed:",
        account_page_displayed
    )

    assert account_page_displayed, (
        "Login failed: Account page was not displayed."
    )

    # 5. Return to home page
    account_page.click_home()

    assert (
        config.get_application_url()
        in driver.current_url
    )

    # 6. Search product
    product_page = ProductPage(
        driver,
        timeout=config.get_timeout()
    )

    product_page.search_product(
        product["product"]
    )

    # 7. Verify product
    assert product_page.is_product_displayed(
        product["product"]
    ), (
        f"Product '{product['product']}' "
        "was not displayed."
    )