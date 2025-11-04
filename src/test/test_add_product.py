"""Product page E2E tests"""

from src.pages.home_page import HomePage


def test_add_macbook_to_cart(browser, base_url):
    """Test add MacBook to cart and validate count and cart content."""
    home = HomePage(browser, base_url).open_page()
    home.add_product_to_cart("MacBook")

    assert "MacBook" in home.success_alert_text()
    home.close_success_alert_text()

    home.wait_cart_count_has_value(1)
    assert home.cart_count() == 1

    cart = home.cart.open()
    assert "MacBook" in cart.get_product_text()
