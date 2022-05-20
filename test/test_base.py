import random

from src.core.driver_manager import DriverManager


class TestBase():

    x = random.randint(0, 9)

    def setup_class(self):
        DriverManager.start("chrome")
        print("setup_class called once for the class - ", TestBase.x)

    def teardown_class(self):
        DriverManager.quit()
        print("teardown_class called once for the class - ", TestBase.x)

    def setup_method(self):
        print("  setup_method called for every method - ", TestBase.x)

    def teardown_method(self):
        print("  teardown_method called for every method - ", TestBase.x)
