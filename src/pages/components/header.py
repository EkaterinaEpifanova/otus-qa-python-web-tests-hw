"""Header of the OpenCart"""
from selenium.webdriver.common.by import By


class HeaderComponent:
    """Header of the page"""
    CURRENCY_TOGGLE = (By.XPATH, "//*[@id='form-currency']/div/a")

    def __init__(self, page):
        self.page = page

    def current_currency_text(self) -> str:
        """Return currency"""
        return self.page.get_element(self.CURRENCY_TOGGLE).text

    def change_currency(self, currency_code: str):
        """Change currency"""
        before = self.current_currency_text()
        self.page.click(self.CURRENCY_TOGGLE)
        self.page.click((By.XPATH, f"//a[@href='{currency_code}']"))

        self.page.wait_for(condition=lambda driver: self.current_currency_text() != before)
        return self
