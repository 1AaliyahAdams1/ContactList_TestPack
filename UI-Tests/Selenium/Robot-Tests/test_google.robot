*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Google Smoke Test
    Open Browser  https://www.google.com  chrome
    Title Should be  Google
    Log  Browser opened successfully
    Close Browser