
from src.core.driver_factory import DriverFactory


class DriverManager():

    __driver = None

    @staticmethod
    def start(browser):
        DriverManager.__driver = DriverFactory.get(browser)

    @staticmethod
    def driver():
        return DriverManager.__driver

    @staticmethod
    def quit():
        DriverManager.__driver.quit()

# browsers = ["chrome", "edge", "firefox", "safari"]

# for browser in browsers:
#   print("check browser: ", browser)
#   DriverManager.start(browser)
#   DriverManager.driver().get("http://www.python.org")
#   DriverManager.quit()


