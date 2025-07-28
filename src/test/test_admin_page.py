"""Admin page E2E tests"""
from src.pages.admin.login_page import AdminLoginPage
from src.pages.admin.admin_account_page import AdminDashboardPage


def test_admin_login_logout(browser, base_url, admin_credentials):
    """Login to admin page test"""
    login = AdminLoginPage(browser, base_url).open_page()
    login.is_loaded()
    login.login(admin_credentials["username"], admin_credentials["password"])

    dashboard = AdminDashboardPage(browser, base_url).assert_opened()
    dashboard.logout()
