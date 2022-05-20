from src.core.driver_manager import DriverManager


class BasePage():

    def open(self, path):
        DriverManager.driver().get("http://automationpractice.com" + path)
