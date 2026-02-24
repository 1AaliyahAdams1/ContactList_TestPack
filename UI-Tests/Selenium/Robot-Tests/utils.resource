*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${WEBSITE URL}    https://thinking-tester-contact-list.herokuapp.com/
${BROWSER}        Chrome
${EMAIL}          0Testciimuvip080Testciimuvip080@gmail.com
${PASSWORD}       1234TEST 
${NAME}           Test
${SURNAME}        Testerson
#XPATHS
${Email_input}        xpath://input[@id='email']
${Password_input}     xpath://input[@id='password']
${login_button}       xpath://button[@id='submit']
${SignUp_button}      xpath://button[@id='signup']
${Name_input}         xpath://input[@id='firstName']
${Surname_input}       xpath://input[@id='lastName']

*** Keywords ***
Open Website
    Open Browser    ${WEBSITE URL}    ${BROWSER}
    Title Should Be    Contact List App

Submit Credentials
    Click Button    ${Login_button}

Validate Login
    Sleep  5 seconds
    Title Should Be  My Contacts