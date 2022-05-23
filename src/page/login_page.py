from src.page.base_page import BasePage
from src.page.login_locators import LoginLocators


class LoginPage(BasePage):

    def open(self):
        """TBD
        """
        self.get("/login")

    def access_account(self, username: str, password: str) -> None:
        self.driver.find_element(
            *LoginLocators.username_input).send_keys(username)
        self.driver.find_element(
            *LoginLocators.password_input).send_keys(password)
        self.driver.find_element(
            *LoginLocators.login_button).click()

    def get_message(self) -> str:
        self.wait_presence_of_element(LoginLocators.message_label)
        message = self.driver.find_element(
            *LoginLocators.message_label).text
        return message.split('\n')[0]
