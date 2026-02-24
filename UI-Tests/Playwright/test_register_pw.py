import pytest
import globals_ui

#XPATHS
SignUp_URL = "//button[@id='signup']"
FirstName_URL = "//input[@id='firstName']"
LastName_URL = "//input[@id='lastName']"
Email_URL = "//input[@id='email']"
Password_URL = "//input[@id='password']"
Submit_URL = "//button[@id='submit']"
Validation_text = "//p[text()='Click on any contact to view the Contact Details']"

@pytest.mark.regressiontest_pw
def test_register_pw(browser):
    page = browser.new_page()
    page.goto(globals_ui.website_url)

    page.click(SignUp_URL)

    page.wait_for_selector(FirstName_URL)
    page.fill(FirstName_URL, globals_ui.first_name)

    page.wait_for_selector(LastName_URL)
    page.fill(LastName_URL, globals_ui.last_name)

    page.wait_for_selector(Email_URL)
    page.fill(Email_URL, globals_ui.email)

    page.wait_for_selector(Password_URL)
    page.fill(Password_URL, globals_ui.password)

    page.click(Submit_URL)

    page.wait_for_selector(Validation_text)
    assert page.is_visible(Validation_text), "Login was not successful"

