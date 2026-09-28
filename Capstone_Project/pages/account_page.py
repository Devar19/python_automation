from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):

    ACCOUNT_HEADING = (
        By.CSS_SELECTOR,
        "#content h2"
    )

    HOME_BUTTON = (
        By.XPATH,
        "//ul[contains(@class,'breadcrumb')]/li[1]/a"
    )

    def is_account_page_displayed(self):
        try:
            heading = self.wait.until(
                lambda driver: driver.find_element(
                    *self.ACCOUNT_HEADING
                )
            )

            return heading.text.strip().lower() == "my account"

        except Exception:
            return False

    def click_home(self):
        self.click_with_javascript(self.HOME_BUTTON)