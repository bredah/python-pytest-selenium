from selenium.webdriver.common.by import By


class UploadLocators:

    upload_input = (By.ID, "file-upload")
    upload_button = (By.ID, "file-submit")
    validation_message_label = (By.CSS_SELECTOR, "h3")
    validation_file_label = (By.ID, "uploaded-files")
