from page.dropdown_page import DropdownPage
from test_base import TestBase


class TestDropdown(TestBase):

    def setup_class(self):
        super().setup_class(self)
        self.dropdown_page = DropdownPage(self.driver)

    def test_dropdown_by_text(self):
        self.dropdown_page.open()
        self.dropdown_page.select("Option 1")
        result = self.dropdown_page.get_value()
        assert result == "Option 1"

    def test_dropdown_by_index(self):
        self.dropdown_page.open()
        self.dropdown_page.select(1)
        result = self.dropdown_page.get_value()
        assert result == "Option 1"
