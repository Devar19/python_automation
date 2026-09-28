import pytest

from utils.config_reader import ConfigReader
from utils.driver_factory import DriverFactory
from utils.screenshot import ScreenshotUtility


@pytest.fixture
def config():
    return ConfigReader()


@pytest.fixture
def driver(config):

    driver = DriverFactory.create_driver(
        config.get_browser()
    )

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver is not None:

            screenshot_path = ScreenshotUtility.capture(
                driver,
                item.nodeid
            )

            print(
                f"\nScreenshot captured: {screenshot_path}"
            )

            # Attach screenshot to pytest-html report
            if hasattr(report, "extras"):

                from pytest_html import extras

                report.extras.append(
                    extras.image(
                        str(screenshot_path)
                    )
                )