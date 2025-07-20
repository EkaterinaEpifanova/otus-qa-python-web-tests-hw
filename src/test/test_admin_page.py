"""Admin page E2E tests"""
from selenium.webdriver.common.by import By

from src.conftest import wait_for


def test_admin_login_logout(browser, base_url, admin_credentials):
    """Login to admin page test"""
    browser.get(f"{base_url}/admin")

    wait_for(browser, by=By.ID, value="input-username").send_keys(admin_credentials["username"])
    wait_for(browser, by=By.ID, value="input-password").send_keys(admin_credentials["password"])
    wait_for(browser, by=By.XPATH, value="//button[@type='submit']").click()

    wait_for(browser, url_contains="dashboard")
    assert "dashboard" in browser.current_url.lower()

    # Ожидаем и кликаем по меню с логином (nav-logout)
    wait_for(browser, by=By.ID, value="nav-logout").click()

    wait_for(browser, url_contains="login")
    assert "login" in browser.current_url.lower()
