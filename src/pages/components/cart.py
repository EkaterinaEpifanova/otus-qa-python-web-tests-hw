"""Cart dropdown"""
import allure
from selenium.webdriver.common.by import By


class CartDropdown:
    """Cart dropdown element of the page"""
    BUTTON = (By.XPATH, "//*[@id='cart']/div/button")
    DROPDOWN = (By.CSS_SELECTOR, ".dropdown-menu.show")

    def __init__(self, page):
        self.page = page

    @allure.step("Open cart dropdown")
    def open(self):
        """Open cart dropdown"""
        self.page.click(self.BUTTON)
        self.page.get_element(self.DROPDOWN)
        return self

    @allure.step("Get product in the cart dropdown")
    def get_product_text(self) -> str:
        """Find product in the cart dropdown"""
        return self.page.get_element(self.DROPDOWN).text
