"""Admin product E2E tests"""
import time

from src.pages.admin.admin_account_page import AdminDashboardPage
from src.pages.admin.login_page import AdminLoginPage
from src.pages.admin.product_form_page import AdminProductFormPage
from src.pages.admin.products_page import AdminProductsPage


def _login_and_open_products(browser, base_url, admin_credentials):
    login = AdminLoginPage(browser, base_url).open_page()
    login.is_loaded()
    login.login(admin_credentials["username"], admin_credentials["password"])
    AdminDashboardPage(browser, base_url).assert_opened()
    return AdminProductsPage(browser, base_url).open_page()


def test_admin_add_new_product(browser, base_url, admin_credentials, unique_product_name, unique_seo):
    products = _login_and_open_products(browser, base_url, admin_credentials)

    products.click_add()
    form = AdminProductFormPage(browser, base_url)
    form.fill_and_save(
        name=unique_product_name,
        meta_title=f"Meta {unique_product_name}",
        model="QA-TEST-MODEL",
        seo_keyword=unique_seo
    )

    assert "Success" in products.success_text()
    AdminProductsPage(browser, base_url).open_page()
    products.filter_by_name(unique_product_name)
    assert products.is_product_present(unique_product_name), "Product not found in the list after save"


def test_admin_delete_product(browser, base_url, admin_credentials, unique_product_name, unique_seo):
    # Create product
    products = _login_and_open_products(browser, base_url, admin_credentials)
    products.click_add()
    form = AdminProductFormPage(browser, base_url)
    form.fill_and_save(
        name=unique_product_name,
        meta_title=f"Meta {unique_product_name}",
        model="QA-TEST-MODEL",
        seo_keyword=unique_seo
    )
    assert "Success" in products.success_text()

    AdminProductsPage(browser, base_url).open_page()
    # Delete product
    products.delete_by_name(unique_product_name)
    assert "Success" in products.success_text()
    assert products.no_results_text() == "No results!", "Product still present after deletion"
