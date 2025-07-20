import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    """Custom command line parameters for running test, by default Chrome driver"""
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--base_url", action="store", default="http://localhost:8080", help="Base URL of OpenCart")


@pytest.fixture
def browser(request):
    """Select browser"""
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_url(request):
    """Base URL"""
    return request.config.getoption("--base_url")


def wait_for_element(driver, by, value, timeout=10):
    """Explicit waiter"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )


def wait_for(driver, *, by=None, value=None, url_contains=None, condition=None, timeout=10):
    """Waiter by + value, by URL, by condition"""
    if by and value:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
    elif url_contains:
        return WebDriverWait(driver, timeout).until(EC.url_contains(url_contains))
    elif condition:
        return WebDriverWait(driver, timeout).until(condition)
    else:
        raise ValueError("wait_for: you must provide by + value, url_contains, or condition")


@pytest.fixture
def admin_credentials():
    return {
        "username": "admin",
        "password": "Qwerty123"
    }
