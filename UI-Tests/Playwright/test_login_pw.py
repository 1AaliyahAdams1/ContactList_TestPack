import pytest
import globals_ui

#XPATHS
Email_input = "//input[@id='email']"
Password_input = "//input[@id='password']"
login_button = "//button[@id='submit']"
Validation_text = "//p[text()='Click on any contact to view the Contact Details']"

@pytest.mark.regressiontest_pw
def test_login_pw(browser):
    page = browser.new_page()
    page.goto(globals_ui.website_url)

    page.wait_for_selector(Email_input)
    page.fill(Email_input, globals_ui.login_email)

    page.wait_for_selector(Password_input)
    page.fill(Password_input, globals_ui.password)

    page.click(login_button)

    page.wait_for_selector(Validation_text)
    assert page.is_visible(Validation_text), "Login was not successful"

