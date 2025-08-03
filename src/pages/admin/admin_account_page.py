"""Admin page"""
import allure
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class AdminDashboardPage(BasePage):
    """Admin page"""
    LOGOUT = (By.ID, "nav-logout")

    @allure.step("Verify the admin is successfully login")
    def assert_opened(self):
        """Method that verify the admin is successfully login"""
        self.wait_for_url_contains("dashboard")
        return self

    @allure.step("Logout method")
    def logout(self):
        """Logout method"""
        self.click(self.LOGOUT)
        self.wait_for_url_contains("login")
        return self
