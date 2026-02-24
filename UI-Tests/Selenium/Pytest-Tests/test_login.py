#IMPORTS
import pytest
from selenium.webdriver.common.by import By
import globals_ui

#XPATHS
Email_input = "//input[@id='email']"
Password_input = "//input[@id='password']"
login_button = "//button[@id='submit']"
Validation_text = "//p[text()='Click on any contact to view the Contact Details']"

@pytest.mark.regressiontest_s
def test_login(setUp, tearDown):
    Email_Text = globals_ui.global_driver.find_element(By.XPATH, Email_input)
    Email_Text.send_keys(globals_ui.login_email)

    Password_Text = globals_ui.global_driver.find_element(By.XPATH, Password_input)
    Password_Text.send_keys(globals_ui.password)

    Submit_Button = globals_ui.global_driver.find_element(By.XPATH, login_button)
    Submit_Button.click()

    text = globals_ui.global_driver.find_element(By.XPATH, Validation_text).text
    assert text == "Click on any contact to view the Contact Details", "Login failed"


