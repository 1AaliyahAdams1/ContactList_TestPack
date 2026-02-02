import pytest
from playwright.sync_api import APIRequestContext
import globals_api

@pytest.mark.smoketest
def test_post_user(api_request_context: APIRequestContext) -> None:

    request_json = {
        "firstName": globals_api.firstName,
        "lastName": globals_api.lastName,
        "email": globals_api.generateEmail(),
        "password": globals_api.password
    }

    header = {
        'Authorization': "Bearer {{token}}"
    }

    response = api_request_context.post(url = "/users", data = request_json, headers = header)

    assert response.ok is True
    data = response.json()
    print(data)
    print("User Created Successfully")
