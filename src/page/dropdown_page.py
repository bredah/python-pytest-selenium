from src.page.base_page import BasePage
from page.dropdown_locators import DropdownLocators


class DropdownPage(BasePage):

    def open(self):
        """TBD
        """
        super().get("/dropdown")

    def select(self, value) -> None:
        if type(value) is int:
            self.select_by_index(DropdownLocators.dropdown, value)
        if type(value) is str:
            self.select_by_text(DropdownLocators.dropdown, value)

    def get_value(self) -> str:
        return self.select_get_value(DropdownLocators.dropdown)
