"""Base page behavior"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_TIMEOUT = 10


class BasePage:
    """Base page behavior"""

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url.rstrip("/")

    @staticmethod
    def _text_xpath(text):
        return f"//*[text()='{text}']"

    def open_page(self, path: str = ""):
        """Open page"""
        self.browser.get(f"{self.base_url}/{path.lstrip('/')}")
        return self

    def get_element(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT):
        """Find element"""
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator, timeout: int = DEFAULT_TIMEOUT):
        """Find elements"""
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def click(self, locator):
        """Click on the element with the user-like delay"""
        (ActionChains(self.browser).move_to_element(self.get_element(locator))
         .pause(0.5).click().perform())

    def input_value(self, locator: tuple, text: str, timeout: int = DEFAULT_TIMEOUT):
        """Enter some text to the input"""
        self.get_element(locator, timeout).click()
        self.get_element(locator, timeout).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

    def wait_for_url_contains(self, part_of_url: str, timeout: int = DEFAULT_TIMEOUT):
        """Waiter for URL"""
        WebDriverWait(self.browser, timeout).until(EC.url_contains(part_of_url))

    def js(self, script: str, *args):
        """Execute JS method"""
        return self.browser.execute_script(script, *args)

    def wait_for_condition(self, condition, timeout=DEFAULT_TIMEOUT):
        """Waiter"""
        WebDriverWait(self.browser, timeout).until(condition)

    def wait_for(self, *, by=None, value=None, url_contains=None, condition=None, timeout=10):
        """Waiter by + value, by URL, by condition"""
        if by and value:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((by, value)))
        elif url_contains:
            return WebDriverWait(self.browser, timeout).until(EC.url_contains(url_contains))
        elif condition:
            return WebDriverWait(self.browser, timeout).until(condition)
        else:
            raise ValueError("wait_for: you must provide by + value, url_contains, or condition")
