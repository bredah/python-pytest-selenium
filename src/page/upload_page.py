from src.page.base_page import BasePage
from src.page.upload_locators import UploadLocators


class UploadPage(BasePage):

    def open(self):
        """TBD
        """
        super().get("/upload")

    def upload(self, file: str) -> None:
        self.driver.find_element(*UploadLocators.upload_input).send_keys(file)
        self.driver.find_element(*UploadLocators.upload_button).click()

    def get_info(self) -> tuple:
        message = self.driver.find_element(
            *UploadLocators.validation_message_label).text
        file = self.driver.find_element(
            *UploadLocators.validation_file_label).text
        return (message, file)
