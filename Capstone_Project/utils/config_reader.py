import configparser
from pathlib import Path

class ConfigReader:

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "config" / "config.ini"

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_application_url(self):
        return self.config["application"]["url"]

    def get_browser(self):
        return self.config["browser"]["name"]

    def get_timeout(self):
        return int(self.config["test"]["timeout"])