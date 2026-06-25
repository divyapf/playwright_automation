# tests/test_login.py
# These tests check the login page of SauceDemo

from pages.login_page import LoginPage

class TestLogin:

    def test_successful_login(self, login_page):
        """
        TEST: Logging in with correct credentials should go to products page.
        """
        login = LoginPage(login_page)
        login.login("standard_user", "secret_sauce")

        # Check we are now on the inventory/products page
        assert "inventory" in login_page.url

    def test_wrong_password_shows_error(self, login_page):
        """
        TEST: Wrong password should show an error message.
        """
        login = LoginPage(login_page)
        login.login("standard_user", "wrong_password")

        assert login.is_error_visible()