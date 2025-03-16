from playwright.sync_api import sync_playwright
import pytest

BASE_URL = "https://endorphina.com/"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()

def test_homepage_loads(page):
    page.goto(BASE_URL)
    assert page.title() == "ENDORPHINA | Company Providing Slot Games to Online Casinos"

def test_navigation_menu(page):
    page.goto(BASE_URL)
    menu = page.locator("nav").nth(0)
    assert menu.is_visible() == True

def test_accept_cookies(page):
    page.goto(BASE_URL)
    cookie_banner = page.locator("body > div.cookie-wrapper.displayed")
    if cookie_banner.is_visible():
        page.locator("body > div.cookie-wrapper.displayed > div > button.btn.btn-primary.btn-accept").click()
    assert cookie_banner.is_visible() == False

def test_accept_age_modal(page):
    page.goto(BASE_URL)
    age_modal = page.locator("body > div.modal-wrapper.displayed")
    if age_modal.is_visible():
        page.locator("body > div.modal-wrapper.displayed > div.modal.modal-age.displayed > div > div > button.btn.btn-primary.btn-yes").click()
    assert age_modal.is_visible() == False

def test_about_section(page):
    page.goto(BASE_URL)
    about_section = page.locator("section:has-text('About')")
    assert about_section.is_visible() == True
