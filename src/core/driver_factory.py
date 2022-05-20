import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory():

    @staticmethod
    def get(browser: str) -> webdriver:
        # turn off webdriver-manager logs
        os.environ['WDM_LOG'] = '0'
        match browser:
            case "chrome":
                driver = webdriver.Chrome(service=Service(
                    ChromeDriverManager().install()))
            case "firefox":
                driver = webdriver.Firefox(
                    executable_path=GeckoDriverManager().install())
            case "edge":
                driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            case "safari":
                driver = webdriver.Safari()
        return driver
