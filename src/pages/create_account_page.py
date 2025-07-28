"""Create user account page"""

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class RegisterPage(BasePage):
    """Create the user account page"""
    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    PRIVACY_CHECKBOX = (By.NAME, "agree")
    SUBMIT = (By.XPATH, "//*[@id='form-register']/div/button")
    SUCCESS_TITLE = (By.XPATH, "//h1[contains(text(), 'Your Account Has Been Created')]")

    def open_page(self):
        """Open registration page"""
        return super().open_page("index.php?route=account/register")

    def is_loaded(self):
        """Method to verify that the registration page contains all required elements"""
        self.get_element(self.FIRSTNAME)
        self.get_element(self.LASTNAME)
        self.get_element(self.EMAIL)
        self.get_element(self.PASSWORD)
        self.get_element(self.SUBMIT)
        return True

    def register(self, firstname, lastname, email, password):
        self.input_value(self.FIRSTNAME, firstname)
        self.input_value(self.LASTNAME, lastname)
        self.input_value(self.EMAIL, email)
        self.input_value(self.PASSWORD, password)
        self.click(self.PRIVACY_CHECKBOX)
        self.click(self.SUBMIT)
        return self

    def is_success(self) -> bool:
        self.get_element(self.SUCCESS_TITLE)
        return True
