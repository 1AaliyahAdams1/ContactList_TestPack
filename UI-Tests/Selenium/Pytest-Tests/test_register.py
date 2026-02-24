#IMPORTS
import pytest
from selenium.webdriver.common.by import By
import globals_ui

#XPATHS
SignUp_URL = "//button[@id='signup']"
FirstName_URL = "//input[@id='firstName']"
LastName_URL = "//input[@id='lastName']"
Email_URL = "//input[@id='email']"
Password_URL = "//input[@id='password']"
Submit_URL = "//button[@id='submit']"
Validation_text = "//p[text()='Click on any contact to view the Contact Details']"

@pytest.mark.smoketest_s
def test_register(setUp, tearDown):
    SignUp_Button = globals_ui.global_driver.find_element(By.XPATH, SignUp_URL)
    SignUp_Button.click()

    FirstName_Text = globals_ui.global_driver.find_element(By.XPATH, FirstName_URL)
    FirstName_Text.send_keys(globals_ui.first_name)

    LastName_Text = globals_ui.global_driver.find_element(By.XPATH, LastName_URL)
    LastName_Text.send_keys(globals_ui.last_name)

    Email_Text = globals_ui.global_driver.find_element(By.XPATH, Email_URL)
    Email_Text.send_keys(globals_ui.email)

    Password_Text = globals_ui.global_driver.find_element(By.XPATH, Password_URL)
    Password_Text.send_keys(globals_ui.password)

    Submit_Button = globals_ui.global_driver.find_element(By.XPATH, Submit_URL)
    Submit_Button.click()

    text = globals_ui.global_driver.find_element(By.XPATH, Validation_text).text
    assert text == "Click on any contact to view the Contact Details", "Registration failed"


