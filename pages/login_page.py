# pages/login_page.py
# This file represents the Login page of SauceDemo

class LoginPage:
    
    def __init__(self, page):
        # Save the page so all methods below can use it
        self.page = page
        
        # Locators — these find elements on the page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button   = page.locator("#login-button")
        self.error_message  = page.locator("[data-test='error']")

    def login(self, username, password):
        """Types username and password, then clicks Login."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """Returns the error message text after a failed login."""
        return self.error_message.text_content()

    def is_error_visible(self):
        """Returns True if an error message is shown."""
        return self.error_message.is_visible()