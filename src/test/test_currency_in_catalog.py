"""Product page E2E tests"""
import pytest
from selenium.webdriver.common.by import By

from src.conftest import wait_for


@pytest.mark.parametrize("currency_code, expected_symbol", [
    ("EUR", "€"),
    ("GBP", "£"),
])
def test_currency_change_in_catalog(browser, base_url, currency_code, expected_symbol):
    """Switch currency test"""
    browser.get(f"{base_url}/index.php?route=product/category&path=20")

    currency_before = wait_for(browser, by=By.XPATH, value="//*[@id='form-currency']/div/a").text

    # Переключаем валюту
    wait_for(browser, by=By.XPATH, value="//*[@id='form-currency']/div/a").click()
    wait_for(browser, by=By.XPATH, value=f"//a[@href='{currency_code}']").click()

    wait_for(browser, condition=lambda driver:
    driver.find_element(By.XPATH, "//*[@id='form-currency']/div/a").text != currency_before)

    currency_after = browser.find_element(By.XPATH, "//*[@id='form-currency']/div/a").text

    assert currency_before != currency_after, f"Currency did not change after switching to {currency_code}"
    assert expected_symbol in currency_after, f"Expected symbol '{expected_symbol}' not found in currency after switching to {currency_code}"


def test_default_currency_in_catalog(browser, base_url):
    """Default currency test"""
    browser.get(f"{base_url}/index.php?route=product/category&path=20")
    default_currency = wait_for(browser, by=By.XPATH, value="//*[@id='form-currency']/div/a")
    assert default_currency.text == "$ Currency", f"Wrong default currency {default_currency.text}"
