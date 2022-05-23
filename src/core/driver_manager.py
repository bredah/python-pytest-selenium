"""
TBD
Since 2022
"""

from src.core.driver_factory import DriverFactory
from selenium import webdriver


class DriverManager():
    """
    Manager the driver used during the test
    """

    def __init__(self) -> None:
        self.driver: webdriver = None

    def start(self, browser):
        """
        Start the browser

        Args:
            browser (str): brownser name
        """
        return DriverFactory().get(browser)

    def quit(self):
        """
        Close the browser and terminate the driver
        """
        self.driver.quit()

    @property
    def driver(self):
        """
        Return the driver object

        Returns:
            webdriver: driver used during test
        """
        return self.driver


# browsers = ["chrome", "edge", "firefox", "safari"]

# for browser in browsers:
#   print("check browser: ", browser)
#   DriverManager.start(browser)
#   DriverManager.driver().get("http://www.python.org")
#   DriverManager.quit()
