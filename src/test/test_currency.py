"""Main page E2E tests"""
import pytest

from src.pages.home_page import HomePage


@pytest.mark.parametrize("currency_code, expected_symbol", [
    ("EUR", "€"),
    ("GBP", "£"),
])
def test_currency_change_on_main(browser, base_url, currency_code, expected_symbol):
    """Switch currency test"""
    home = HomePage(browser, base_url).open_page()
    before = home.header.current_currency_text()
    home.header.change_currency(currency_code)
    after = home.header.current_currency_text()

    assert before != after
    assert expected_symbol in after


def test_default_currency(browser, base_url):
    """Default currency test"""
    home = HomePage(browser, base_url).open_page()
    assert home.header.current_currency_text() == "$ Currency"
