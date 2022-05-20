
import pytest
from test_base import TestBase
from src.page.home_page import HomePage

class TestExample(TestBase):

    
    def setup_class(self):
        super().setup_class(self)
        self.home_page = HomePage()

    # def teardown_class(self):
    #     super().teardown_class(self)
    #     self.home_page = None

    def test_example_1_pass(self):        
        self.home_page.open()
        print("test_example_1_pass")
        assert 10 == 10

    def test_example_2_pass(self):
        self.home_page.open()
        print("test_example_2_pass")
        assert 10 == 10

    def test_example_1_fail(self):
        self.home_page.open()
        print("test_example_1_fail")
        assert 10 == 11

    def test_example_2_fail(self):
        self.home_page.open()
        print("test_example_2_fail")
        assert 10 == 11
