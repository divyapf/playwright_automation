import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page):
    page.goto("https://www.saucedemo.com")
    return page

@pytest.fixture
def todo_page(page: Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.wait_for_selector(".new-todo")
    return page