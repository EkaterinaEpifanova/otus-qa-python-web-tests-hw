"""Admin product page"""
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.base_page import BasePage


class AdminProductsPage(BasePage):
    """Admin product page"""
    MENU_CATALOG = (By.ID, "menu-catalog")
    LINK_PRODUCTS = (By.XPATH, "//a[text()='Products']")
    ADD_BUTTON = (By.CLASS_NAME, "fa-plus")
    DELETE_BUTTON = (By.CLASS_NAME, "fa-trash-can")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    NO_RESULTS = (By.XPATH, "//*[@id='form-product']/div[1]/table/tbody/tr/td")

    FILTER_NAME = (By.ID, "input-name")
    FILTER_BUTTON = (By.XPATH, "//*[@id='button-filter']/i")

    TABLE = (By.CSS_SELECTOR, "table.table")
    TABLE_ROWS = (By.CSS_SELECTOR, "table.table tbody tr")
    ROW_NAME_CELL = (By.CSS_SELECTOR, "td:nth-child(3)")
    ROW_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    @allure.step("Open page and interact with dashboard page")
    def open_page(self):
        """Open page and interact with dashboard page"""
        self.click(self.MENU_CATALOG)
        self.click(self.LINK_PRODUCTS)
        self.get_element(self.TABLE)
        return self

    @allure.step("Add new product")
    def click_add(self):
        """Add new product"""
        self.click(self.ADD_BUTTON)
        return self

    # TODO: Get rid of time.sleep by verifying the presence or absence of the product in the DB, or by refreshing the page
    @allure.step("Delete product")
    def delete_by_name(self, name: str):
        """Delete product"""
        self.filter_by_name(name)
        # wait for the previous success message to disappear before proceeding, the user-like delay
        time.sleep(0.5)
        rows = self.get_elements(self.TABLE_ROWS)
        checkbox = rows[0].find_element(by=self.ROW_CHECKBOX[0], value=self.ROW_CHECKBOX[1])
        self.js("arguments[0].click()", checkbox)
        self.click(self.DELETE_BUTTON)
        # wait for the previous success message to disappear before proceeding, the user-like delay
        time.sleep(0.5)
        alert = self.browser.switch_to.alert
        alert.accept()
        self.get_elements(self.SUCCESS_ALERT)
        # wait for the previous success message to disappear before proceeding, the user-like delay
        time.sleep(0.5)
        return self

    @allure.step("Filter products by {name}")
    def filter_by_name(self, name: str):
        """Filter products"""
        try:
            WebDriverWait(self.browser, 0.5).until(
                EC.invisibility_of_element_located(self.SUCCESS_ALERT)
            )
        except TimeoutException:
            raise AssertionError("Unexpected SUCCESS alert is visible before filtering")
        self.input_value(self.FILTER_NAME, name)
        self.click(self.FILTER_BUTTON)
        self.get_element(self.TABLE)
        return self

    @allure.step("Verify the product {name} is shown")
    def is_product_present(self, name: str) -> bool:
        """Method that verify the product is shown"""
        rows = self.get_elements(self.TABLE_ROWS)
        for r in rows:
            if r.find_element(by=self.ROW_NAME_CELL[0], value=self.ROW_NAME_CELL[1]).text.strip() == name:
                return True
        return False

    @allure.step("Success message is displayed")
    def success_text(self) -> str:
        """Success message"""
        return self.get_element(self.SUCCESS_ALERT).text

    @allure.step("Get No results text")
    def no_results_text(self) -> str:
        """No results"""
        return self.get_element(self.NO_RESULTS).text
