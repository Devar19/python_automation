from utils.config_reader import ConfigReader

def test_config_reader():
    config = ConfigReader()

    print("URL:", config.get_application_url())
    print("Browser:", config.get_browser())
    print("Timeout:", config.get_timeout())

    assert config.get_application_url() == "https://tutorialsninja.com/demo/"
    assert config.get_browser() == "chrome"
    assert config.get_timeout() == 10