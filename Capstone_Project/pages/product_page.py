from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "div.product-thumb h4 a")

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_product_names(self):
        elements = self.wait.until(
            lambda driver: driver.find_elements(*self.PRODUCT_NAMES)
        )

        return [element.text.strip() for element in elements]

    def is_product_displayed(self, product_name):
        products = self.get_product_names()

        return any(
            product.lower() == product_name.lower()
            for product in products
        )