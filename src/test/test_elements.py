"""Component tests for UI elements"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from src.conftest import wait_for


def test_homepage_elements(browser, base_url):
    """Verification of elements on the main page"""
    browser.get(base_url)
    wait_for(browser, by=By.ID, value="logo")
    wait_for(browser, by=By.NAME, value="search")
    wait_for(browser, by=By.LINK_TEXT, value="My Account")
    wait_for(browser, by=By.LINK_TEXT, value="Shopping Cart")
    wait_for(browser, by=By.LINK_TEXT, value="Checkout")


def test_catalog_page(browser, base_url):
    """Verification of elements on the catalog page"""
    browser.get(f"{base_url}/index.php?route=product/category&path=20")
    wait_for(browser, by=By.XPATH, value="//h1[text()='Desktops']")  # Category title
    wait_for(browser, by=By.CLASS_NAME, value="product-thumb")
    wait_for(browser, by=By.ID, value="input-sort")
    sort_dropdown = wait_for(browser, by=By.ID, value="input-sort")
    select = Select(sort_dropdown)
    actual_options = [option.text for option in select.options]
    # TODO: Move to the list when it is used in other verifications
    expected_options = [
        "Default",
        "Name (A - Z)",
        "Name (Z - A)",
        "Price (Low > High)",
        "Price (High > Low)",
        "Rating (Highest)",
        "Rating (Lowest)",
        "Model (A - Z)",
        "Model (Z - A)"
    ]
    assert actual_options == expected_options, \
        f"Expected {expected_options}, but got {actual_options}"


def test_product_page(browser, base_url):
    """Verification of elements on the product page"""
    expected_price = "$122.00"

    browser.get(f"{base_url}/index.php?route=product/product&language=en-gb&product_id=42&path=20")
    wait_for(browser, by=By.XPATH, value="//h1[text()=concat('Apple Cinema 30', '\"')]")

    price_element = wait_for(browser, by=By.CLASS_NAME, value="price-new")
    price_text = price_element.text
    assert price_text == expected_price, f"Expected price {expected_price}, but got {price_text}"

    wait_for(browser, by=By.CLASS_NAME, value="rating")
    wait_for(browser, by=By.ID, value="button-cart")


def test_admin_login(browser, base_url):
    """Verification of login elements on the admin page"""
    browser.get(f"{base_url}/admin/")
    expected_title = "Please enter your login details."

    wait_for(browser, by=By.ID, value="input-username")
    wait_for(browser, by=By.ID, value="input-password")
    wait_for(browser, by=By.XPATH, value="//button[@type='submit']")

    title_element = wait_for(browser, by=By.CLASS_NAME, value="card-header")
    title = title_element.text
    assert title == expected_title, f"Expected title {expected_title}, but got {title}"
    wait_for(browser, by=By.TAG_NAME, value="footer")


def test_register_page(browser, base_url):
    """Verification of registration elements on the user page"""
    browser.get(f"{base_url}/index.php?route=account/register")
    wait_for(browser, by=By.ID, value="input-firstname")
    wait_for(browser, by=By.ID, value="input-lastname")
    wait_for(browser, by=By.ID, value="input-email")
    wait_for(browser, by=By.ID, value="input-password")
    wait_for(browser, by=By.XPATH, value="//button[@type='submit']")
