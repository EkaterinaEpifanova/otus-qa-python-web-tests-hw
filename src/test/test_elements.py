"""Component tests for UI elements"""

from src.pages.admin.login_page import AdminLoginPage
from src.pages.category_page import CategoryPage
from src.pages.create_account_page import RegisterPage
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage


def test_homepage_elements(browser, base_url):
    """Verification of elements on the main page"""
    home = HomePage(browser, base_url).open_page()
    assert home.get_element(("id", "logo"))
    assert home.get_element(("name", "search"))
    assert home.get_element(("link text", "My Account"))
    assert home.get_element(("link text", "Shopping Cart"))
    assert home.get_element(("link text", "Checkout"))


def test_catalog_page(browser, base_url):
    """Verification of elements on the catalog page"""
    category = CategoryPage(browser, base_url).open_page()
    assert category.is_loaded()


def test_product_page(browser, base_url):
    """Verification of elements on the product page"""
    expected_price = "$122.00"

    page = ProductPage(browser, base_url).open_apple_cinema()
    assert page.is_loaded()
    assert page.price_text() == expected_price


def test_admin_login(browser, base_url):
    """Verification of login elements on the admin page"""
    login = AdminLoginPage(browser, base_url).open_page()
    login.is_loaded()
    assert login.title_text() == "Please enter your login details."


def test_register_page(browser, base_url):
    """Verification of registration elements on the user page"""
    RegisterPage(browser, base_url).open_page().is_loaded()
