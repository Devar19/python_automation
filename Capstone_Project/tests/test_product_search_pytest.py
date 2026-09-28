import pytest

from utils.csv_reader import CSVReader
from pages.product_page import ProductPage

test_data = CSVReader.read_test_data(
    "product_data.csv"
)

@pytest.mark.parametrize(
    "data",
    test_data,
    ids=lambda data: data["product"]
)
def test_product_search(data, driver, config):

    driver.get(
        config.get_application_url()
    )

    product_name = data["product"]

    product_page = ProductPage(driver,
                               timeout=config.get_timeout()
                               )

    product_page.search_product(
        product_name
    )

    assert product_page.is_product_displayed(
        product_name
    )