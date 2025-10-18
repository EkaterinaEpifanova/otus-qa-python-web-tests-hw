"""Home page"""
import allure
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.pages.components.cart import CartDropdown
from src.pages.components.header import HeaderComponent


class HomePage(BasePage):
    """Home page"""
    PRODUCT_CARD = (By.CLASS_NAME, "product-thumb")
    CART = (By.ID, "header-cart")
    ADD_PRODUCT_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[title='Add to Cart']")

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.header = HeaderComponent(self)
        self.cart = CartDropdown(self)

    def open_page(self):
        """Open registration page"""
        return super().open_page("")

    @allure.step("Add product {product_name} to cart")
    def add_product_to_cart(self, product_name: str):
        """Add product to cart"""
        # ensure products are visible
        self.get_element(self.PRODUCT_CARD)
        # TODO: Is it possible to move the XPath to the parameters somehow?
        self.get_element(
            (By.XPATH,
             f"//a[text()='{product_name}']/ancestor::div[contains(@class, 'product-thumb')]")
        )
        add_to_cart_button = self.get_element(self.ADD_PRODUCT_TO_CART_BUTTON)
        self.wait_for(condition=lambda driver: add_to_cart_button.is_enabled() and add_to_cart_button.is_displayed())
        # click via js, cause the regular selenium click doesn't work
        self.js("arguments[0].click();", add_to_cart_button)
        return self

    @allure.step("Alert is displayed")
    def success_alert_text(self):
        """Alert"""
        return self.get_element((By.CSS_SELECTOR, ".alert-success")).text

    @allure.step("Get cart counter")
    def cart_count(self) -> int:
        """Cart counter"""
        return int(self.get_element(self.CART).text.split()[0])

    @allure.step("Wait updated counter")
    def wait_cart_count_has_value(self, counter):
        """Wait updated counter"""
        self.wait_for(condition=lambda driver: self.cart_count() == counter)
