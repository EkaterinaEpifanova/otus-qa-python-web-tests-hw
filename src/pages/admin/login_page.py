"""Login admin page"""
import allure
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class AdminLoginPage(BasePage):
    """Login admin page"""
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    TITLE = (By.CLASS_NAME, "card-header")

    @allure.step("Open page")
    def open_page(self):
        """Open page"""
        return super().open_page("admin")

    @allure.step("Verify that the login page contains all required elements")
    def is_loaded(self):
        """Method to verify that the login page contains all required elements"""
        self.get_element(self.USERNAME)
        self.get_element(self.PASSWORD)
        self.get_element(self.SUBMIT)
        return True

    @allure.step("Verify that the user on the admin login page")
    def title_text(self):
        """Method to verify that the user on the admin login page"""
        return self.get_element(self.TITLE).text

    @allure.step("Verify the user is successfully login")
    def login(self, username: str, password: str):
        """Login method"""
        self.input_value(self.USERNAME, username)
        self.input_value(self.PASSWORD, password)
        self.click(self.SUBMIT)
        return self
