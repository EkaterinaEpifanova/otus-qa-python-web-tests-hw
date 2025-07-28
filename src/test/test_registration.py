"""Account registration E2E tests"""
from src.pages.create_account_page import RegisterPage


def test_user_registration(browser, base_url, unique_email, random_string, random_password):
    page = RegisterPage(browser, base_url).open_page()
    page.register(
        firstname=random_string,
        lastname=random_string,
        email=unique_email,
        password=random_password
    )
    assert page.is_success()
