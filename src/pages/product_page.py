"""Product card page"""
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class ProductPage(BasePage):
    """Product card page"""
    PRICE = (By.CLASS_NAME, "price-new")
    CART_BUTTON = (By.ID, "button-cart")
    APPLE_CINEMA_TITLE = (By.XPATH, "//h1[text()=concat('Apple Cinema 30', '\"')]")
    APPLE_CINEMA_PRODUCT_URL = "index.php?route=product/product&language=en-gb&product_id=42&path=20"

    def open_apple_cinema(self, path=APPLE_CINEMA_PRODUCT_URL):
        """Open apple cinema product page"""
        return super().open_page(path)

    def price_text(self):
        """Check the price"""
        return self.get_element(self.PRICE).text

    def is_loaded(self):
        """Check the product card is shown"""
        self.get_element(self.APPLE_CINEMA_TITLE)
        self.get_element(self.CART_BUTTON)
        return True
