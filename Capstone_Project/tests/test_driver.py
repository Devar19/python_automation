from utils.driver_factory import DriverFactory

def test_driver_creation():
    driver = DriverFactory.create_driver("chrome")
    
    try:
        driver.get("https://tutorialsninja.com/demo/")
        assert "Your Store" in driver.title
    
    finally:
        driver.quit()