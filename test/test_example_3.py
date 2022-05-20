from test_base import TestBase


class TestExample3(TestBase):

    def test_example_1_pass(self):
        #   DriverManager.start(browser)
        #   DriverManager.driver().get("http://www.python.org")
        print("test_example_1_pass")
        assert 10 == 10

    def test_example_2_pass(self):
        print("test_example_2_pass")
        assert 10 == 10

    def test_example_1_fail(self):
        print("test_example_1_fail")
        assert 10 == 11

    def test_example_2_fail(self):
        print("test_example_2_fail")
        assert 10 == 11
