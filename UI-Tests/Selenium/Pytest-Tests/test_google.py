#IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.mark.smoketest_s
def test_google():
    # Installing Chrome Driver (Instance)
    service = Service(ChromeDriverManager().install())

    # Intialize driver to interact with Chrome
    driver = webdriver.Chrome(service=service)

    # Navigate to command
    driver.get("https://www.google.com")

    # Verifying that the browser opened
    if driver.title == "Google":
        print("Browser opened successfully")
    else:
        print("Browser not found")

    # Closes the driver
    driver.quit()