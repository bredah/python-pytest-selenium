"""_summary_
Factory used to start a webdriver
"""
import os

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium import webdriver


class DriverFactory():
    """
    Manages the initialization of the driver to be used
    """

    def get(self, browser: str) -> webdriver:
        """
        Start a new driver

        Args:
            browser (str): Browser name

        Returns:
            webdriver: new driver session
        """
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

        driver.implicitly_wait(5)  # seconds
        return driver
