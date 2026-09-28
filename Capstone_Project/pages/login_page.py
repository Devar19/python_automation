from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    MY_ACCOUNT = (
        By.CSS_SELECTOR,
        "a.dropdown-toggle"
    )

    LOGIN_LINK = (
        By.XPATH,
        "//a[contains(@href,'route=account/login')]"
    )

    EMAIL = (
        By.ID,
        "input-email"
    )

    PASSWORD = (
        By.ID,
        "input-password"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "input[type='submit']"
    )

    LOGIN_ERROR = (
        By.CSS_SELECTOR,
        ".alert.alert-danger"
    )

    def click_my_account(self):
        self.click(self.MY_ACCOUNT)

    def click_login_link(self):
        self.click(self.LOGIN_LINK)

    def open_login_page(self):
        self.click_my_account()
        self.click_login_link()

    def enter_email(self, email):
        self.enter_text(
            self.EMAIL,
            email
        )

    def enter_password(self, password):
        self.enter_text(
            self.PASSWORD,
            password
        )

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_login_error(self):
        if self.driver.find_elements(*self.LOGIN_ERROR):
            return self.driver.find_element(*self.LOGIN_ERROR).text

        return None