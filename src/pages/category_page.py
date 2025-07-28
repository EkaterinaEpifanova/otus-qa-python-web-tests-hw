"""Product category page"""
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.pages.components.header import HeaderComponent


class CategoryPage(BasePage):
    """Product category page"""
    TITLE = (By.XPATH, "//h1[text()='Desktops']")
    PRODUCT_CARD = (By.CLASS_NAME, "product-thumb")
    DESKTOP_URL = "index.php?route=product/category&path=20"

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.header = HeaderComponent(self)

    def open_page(self, path=DESKTOP_URL):
        """Open desktops page"""
        return super().open_page(path)

    def is_loaded(self):
        """Method that verify the product is shown"""
        self.get_element(self.TITLE)
        self.get_element(self.PRODUCT_CARD)
        return True
