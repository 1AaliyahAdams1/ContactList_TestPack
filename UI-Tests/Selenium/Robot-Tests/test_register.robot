*** Settings ***
Library     SeleniumLibrary
Resource    utils.resource

*** Variables ***
${NEW EMAIL}

*** Test Cases ***
Test Register
    Open Website
    CLick Register Button
    Input Credentials
    Submit Credentials
    Validate Login
    Close Browser

*** Keywords ***
CLick Register button
    CLick button    ${SignUp_button}

Generate Email
    ${randNum}=    Evaluate    random.randint(1, 10)    random
    ${randWord}=   Evaluate    "Test" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=${randNum}))    random
    ${NEW EMAIL}=      Set Variable    0${randWord}0${randNum}0${randWord}0${randNum}0@gmail.com
    [Return]       ${NEW EMAIL}

Input Credentials
    Input Text      ${Name_input}      ${NAME}
    Input Text      ${Surname_input}   ${SURNAME}
    ${NEW EMAIL}=   Generate Email
    Input Text      ${Email_input}     ${NEW EMAIL}
    Input Text      ${Password_input}  ${PASSWORD}
