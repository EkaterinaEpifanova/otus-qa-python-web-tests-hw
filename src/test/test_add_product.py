"""Product page E2E tests"""
from selenium.webdriver.common.by import By

from src.conftest import wait_for, browser


def test_add_macbook_to_cart(browser, base_url):
    """Test add MacBook to cart and validate count and cart content."""
    browser.get(base_url)

    wait_for(browser, by=By.CLASS_NAME, value="product-thumb")

    macbook = browser.find_element(By.XPATH, "//a[text()='MacBook']/ancestor::div[contains(@class, 'product-thumb')]")
    add_to_cart_button = macbook.find_element(By.CSS_SELECTOR, "button[title='Add to Cart']")

    wait_for(browser, condition=lambda driver: add_to_cart_button.is_enabled() and add_to_cart_button.is_displayed())
    browser.execute_script("arguments[0].click();", add_to_cart_button)

    success_alert = wait_for(browser, by=By.CSS_SELECTOR, value=".alert-success")
    assert success_alert.is_displayed()
    assert "MacBook" in success_alert.text

    wait_for(browser, condition=lambda driver: int(driver.find_element(By.ID, "cart").text.split()[0]) == 1)

    cart_text_after = browser.find_element(By.ID, "cart").text
    count_after = int(cart_text_after.split()[0])
    assert count_after == 1, f"Cart count did not increase correctly, got {count_after}"

    cart_button = wait_for(browser, by=By.XPATH, value="//*[@id='cart']/div/button")
    browser.execute_script("arguments[0].click();", cart_button)

    cart_dropdown = wait_for(browser, by=By.CSS_SELECTOR, value=".dropdown-menu.show")
    assert "MacBook" in cart_dropdown.text
