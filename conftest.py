from email.base64mime import header_length

pytest_plugins = ["pytest_playwright"]

import requests
import pytest
import globals_api
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator

#====================================================================
#Fixtures for pytest tests
#====================================================================

@pytest.fixture
def test_user(test_token):

    token = test_token

    yield

    header = {
        'Authorization' : f'Bearer {token}'
    }

    response = requests.request(method="DELETE",
                           url= globals_api.delete_user,
                           headers = header)

    assert response.status_code == 200, "API call failed"
    print("User deleted")


@pytest.fixture
def test_token():
    request_json = {
        "firstName": globals_api.firstName,
        "lastName": globals_api.lastName,
        "email": globals_api.generateEmail(),
        "password": globals_api.password
    }

    header = {
        'Authorization': 'Bearer {{token}}'
    }
    req = requests.request(method="POST",
                           url=globals_api.post_user,
                           json=request_json,
                           headers=header)

    print(req.json())
    assert req.status_code == 201, "API call failed"
    print("User created")

    token = req.json()['token']
    print("Token generated")
    return token

#====================================================================
# Fixtures for Playwright tests
#====================================================================
@pytest.fixture
def api_request_context(playwright : Playwright,) -> Generator[APIRequestContext, None, None]:

    request_context = playwright.request.new_context(
        base_url= globals_api.base_url,
    )

    yield request_context
    request_context.dispose()

@pytest.fixture
def test_token_pw(api_request_context: APIRequestContext):
    request_json = {
        "firstName": globals_api.firstName,
        "lastName": globals_api.lastName,
        "email": globals_api.generateEmail(),
        "password": globals_api.password
    }

    header = {
        'Authorization': "Bearer {{token}}"
    }

    response = api_request_context.post(url="/users", data=request_json, headers=header)

    assert response.ok is True
    print("User created")

    Token = response.json()['token']
    print("Token generated")
    return Token

@pytest.fixture
def test_user_pw(api_request_context: APIRequestContext, test_token_pw):

    token = test_token_pw

    yield

    token = test_token_pw

    header = {
        'Authorization': f"Bearer {token}"
    }

    response = api_request_context.delete(url="/users/me", headers=header)

    assert response.ok is True
    print("User Deleted")
