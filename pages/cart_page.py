#File represents the Products and Cart pages on SauceDemo

class CartPage:

    def __init__(self, page):
        # Save the page so all methods below can use it
        self.page = page

        #finding elements on the page
        self.cart_icon  = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_item_to_cart(self, item_name):
        """Finds a product by name and clicks its Add to cart button."""
        self.page.locator(".inventory_item").filter(
            has_text=item_name
        ).get_by_role("button", name="Add to cart").click()

    def open_cart(self):
        """Clicks the cart icon to go to the cart page."""
        self.cart_icon.click()

    def get_cart_count(self):
        """Returns the number shown on the cart badge. Returns 0 if empty."""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0

    def get_cart_item_names(self):
        """Returns a list of all product names currently in the cart."""
        return self.page.locator(".cart_item_label .inventory_item_name").all_text_contents()

    def remove_item_from_cart(self, item_name):
        """Finds a product in the cart by name and clicks Remove."""
        self.page.locator(".cart_item").filter(
            has_text=item_name
        ).get_by_role("button", name="Remove").click()

    def proceed_to_checkout(self):
        """Clicks the Checkout button."""
        self.page.get_by_role("button", name="Checkout").click()