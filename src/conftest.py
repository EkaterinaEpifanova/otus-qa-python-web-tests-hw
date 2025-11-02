import logging
import platform
import random
import string
import uuid
from email.policy import default

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    """Custom command line parameters for running test, by default Chrome driver"""
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--browser_version", action="store", default="latest", help="Choose browser version")
    parser.addoption("--base_url", action="store", default="http://localhost:8080", help="Base URL of OpenCart")
    # For selenoid:
    parser.addoption("--executor", action="store", default="local",
                     help="local or remote (selenoid/grid)")
    parser.addoption("--executor_url", action="store", default="http://localhost:4444/wd/hub",
                     help="Remote executor URL, e.g. http://selenoid:4444/wd/hub")

@pytest.fixture
def browser(request):
    """Select browser"""
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    executor = request.config.getoption("--executor").lower()
    executor_url = request.config.getoption("--executor_url")

    if executor == "local":
        if browser_name == "chrome":
            options = ChromeOptions()
            if platform.system() == "Windows":
                chrome_type = ChromeType.GOOGLE
            else:
                chrome_type = ChromeType.CHROMIUM
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=chrome_type).install()),
                                      options=options)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")

    else:
        # Selenoid
        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=\"1920x1080\"")
        else:
            options = FirefoxOptions()

        selenoid_opts = {
            "version": browser_version,
            "sessionTimeout": "2m",
            "timeZone": "Europe/Belgrade",
            "enableVNC": True
        }

        options.set_capability("selenoid:options", selenoid_opts)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    driver.test_name = request.node.name
    driver.log_level = logging.INFO
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"Screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture
def base_url(request):
    """Base URL"""
    return request.config.getoption("--base_url")


@pytest.fixture
def admin_credentials():
    return {
        "username": "user",
        "password": "bitnami"
    }


@pytest.fixture
def unique_email():
    return f"qa_{uuid.uuid4().hex[:8]}@example.com"


@pytest.fixture
def unique_product_name():
    return f"{uuid.uuid4().hex[:6]}"


@pytest.fixture
def random_string(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))


@pytest.fixture
def random_password(length=10):
    chars = string.ascii_letters + string.digits + "!@#"
    return ''.join(random.choices(chars, k=length))


@pytest.fixture
def unique_seo():
    return uuid.uuid4().hex[:6]
