"""Product page E2E tests"""
import pytest

from src.pages.category_page import CategoryPage


@pytest.mark.parametrize("currency_code, expected_symbol", [
    ("EUR", "€"),
    ("GBP", "£"),
])
def test_currency_change_in_catalog(browser, base_url, currency_code, expected_symbol):
    """Switch currency test"""
    category = CategoryPage(browser, base_url).open_page()
    category.is_loaded()
    before = category.header.current_currency_text()
    category.header.change_currency(currency_code)
    after = category.header.current_currency_text()
    assert before != after
    assert expected_symbol in after


def test_default_currency_in_catalog(browser, base_url):
    """Default currency test"""
    category = CategoryPage(browser, base_url).open_page()
    assert category.header.current_currency_text() == "$ Currency"
