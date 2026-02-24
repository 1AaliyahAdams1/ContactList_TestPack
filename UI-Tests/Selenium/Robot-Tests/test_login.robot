*** Settings ***
Library    SeleniumLibrary
Resource   utils.resource

*** Test Cases ***
Test Login
    Open Website
    Input Email
    Input Password    
    Submit Credentials
    Validate Login
    Close Browser
    
*** Keywords ***
Input Email
    Input Text    ${Email_input}    ${EMAIL}

Input Password
    Input Text    ${Password_input}   ${PASSWORD}

