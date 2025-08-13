"""Cart page"""
import allure
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class CartPage(BasePage):
    """Cart page"""
    SHOPPING_CART = By.XPATH, "//*[@id='shopping-cart']"
    CHECKOUT_LINK = By.LINK_TEXT, "Checkout"

    def _product_name(self, product_name):
        """Inner method that return product name"""
        return By.XPATH, self.SHOPPING_CART[1] + self._text_xpath(product_name)

    @allure.step("Click to checkout link")
    def click_checkout(self):
        """Click to the checkout link"""
        self.click(self.CHECKOUT_LINK)

    @allure.step("Verify product in the cart")
    def wait_for_product_in_cart(self, product_name):
        """Verify product in the cart"""
        self.get_element(self._product_name(product_name))
        return self
