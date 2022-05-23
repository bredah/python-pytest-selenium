from test_base import TestBase
from src.page.login_page import LoginPage
import pytest


class TestLogin(TestBase):

    def setup_class(self):
        super().setup_class(self)
        self.login_page = LoginPage(self.driver)

    def test_should_login_successfully(self):
        self.login_page.open()
        self.login_page.access_account("tomsmith", "SuperSecretPassword!")
        assert self.login_page.get_message() == "You logged into a secure area!"

    @pytest.mark.parametrize("username,password,expected_message", [
        ("tomsmit", "SuperSecretPassword!", "Your username is invalid!"),
        ("", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "SuperSecretPassword", "Your password is invalid!"),
        ("tomsmith", "", "Your password is invalid!"),
        ("", "", "Your username is invalid!"),
    ])
    def test_should_login_successfully(self, username, password, expected_message):
        self.login_page.open()
        self.login_page.access_account(username, password)
        assert self.login_page.get_message() == expected_message
