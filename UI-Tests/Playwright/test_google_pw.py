import pytest
from playwright.sync_api import expect

@pytest.mark.smoketest_pw
def test_google_pw(browser):
    page = browser.new_page()
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")
