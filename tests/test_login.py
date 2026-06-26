# tests/test_login.py
# These tests check the login page of SauceDemo
import pytest
from pages.login_page import LoginPage

class TestLogin:

    def test_successful_login(self, login_page):
        """
        TEST: Logging in with correct credentials should go to products page.
        """
        login = LoginPage(login_page)
        login.login("standard_user", "secret_sauce")

        # Checking if we are now on the inventory/products page
        assert "inventory" in login_page.url

    def test_wrong_password_shows_error(self, login_page):
        """
        TEST: Wrong password should show an error message.
        """
        login = LoginPage(login_page)
        login.login("standard_user", "wrong_password")
        assert login.is_error_visible()

        
    @pytest.mark.parametrize("username, password",
                              
       [ ("locked_out_user", "secret_sauce"),
        ("wrong_user",      "secret_sauce"),
        ("standard_user",   "wrong_pass"),])
    
    def test_invalid_credentials(self, login_page, username, password):
        login = LoginPage(login_page)
        login.login(username, password)
        assert login.is_error_visible()