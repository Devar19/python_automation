import unittest

from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader
from utils.driver_factory import DriverFactory
from utils.credentials import CredentialReader
from pages.login_page import LoginPage
from pages.account_page import AccountPage


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = ConfigReader()
        cls.test_data = CSVReader.read_test_data(
            "login_data.csv"
        )

    def setUp(self):
        self.driver = DriverFactory.create_driver(
            self.config.get_browser()
        )

        self.driver.get(
            self.config.get_application_url()
        )

    def test_valid_login(self):

        data = self.test_data[0]

        login_page = LoginPage(
            self.driver,
            timeout=self.config.get_timeout()
        )

        login_page.open_login_page()

        password = CredentialReader.get_valid_password()
        login_page.login(
            data["email"],
            password
        )

        account_page = AccountPage(
            self.driver,
            timeout=self.config.get_timeout()
        )

        account_page_displayed = (
            account_page.is_account_page_displayed()
        )

        print("\n--- Unittest Login Diagnostics ---")
        print("Current URL:", self.driver.current_url)
        print("Page title:", self.driver.title)
        print(
            "Account page displayed:",
            account_page_displayed
        )

        self.assertTrue(
            account_page_displayed,
            "Expected successful login, but Account page was not displayed."
        )

        account_page.click_home()

        self.assertIn(
            self.config.get_application_url(),
            self.driver.current_url
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()