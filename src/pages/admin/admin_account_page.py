"""Admin page"""
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class AdminDashboardPage(BasePage):
    """Admin page"""
    LOGOUT = (By.ID, "nav-logout")

    def assert_opened(self):
        """Method that verify the admin is successfully login"""
        self.wait_for_url_contains("dashboard")
        return self

    def logout(self):
        """Logout method"""
        self.click(self.LOGOUT)
        self.wait_for_url_contains("login")
        return self
