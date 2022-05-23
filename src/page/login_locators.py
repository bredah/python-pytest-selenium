from selenium.webdriver.common.by import By


class LoginLocators:

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.XPATH, "//button")
    message_label = (By.ID, "flash")
