import random

from src.core.driver_factory import DriverFactory


class TestBase():
    """
    Base test to set the behavion during the test execution
    """

    x = random.randint(0, 9)

    def setup_class(self):
        """
        Setup test class before execution
        """
        self.driver = DriverFactory().get("chrome")
        print("setup_class called once for the class - ", TestBase.x)

    def teardown_class(self):
        """
        Tear down test class after execution
        """
        self.driver.quit()
        print("teardown_class called once for the class - ", TestBase.x)

    def setup_method(self):
        """
        Perform an action(s) before a test execution
        """
        print("  setup_method called for every method - ", TestBase.x)

    def teardown_method(self):
        """
        Perform an action(s) after a test execution
        """
        print("  teardown_method called for every method - ", TestBase.x)
