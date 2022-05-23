"""
TBD
Since 2022-05
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from src.core.environment import Environment as env


class BasePage():

    def __init__(self, driver):
        self.driver: webdriver = driver

    def get(self, path):
        """
        Args:
            path (string, optional): URL path to the focus page. Defaults to None.
        """
        self.driver.get(env.base_url + path)

    def wait_presence_of_element(self, element: tuple) -> None:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((element)))

    def select_by_text(self, element: tuple, text: str) -> None:
        dropdown = Select(self.driver.find_element(*element))
        dropdown.select_by_visible_text(text)

    def select_by_index(self, element: tuple, index: int) -> None:
        dropdown = Select(self.driver.find_element(*element))
        dropdown.select_by_index(index)

    def select_get_value(self, element: tuple) -> str:
        dropdown = Select(self.driver.find_element(*element))
        return dropdown.first_selected_option.text
