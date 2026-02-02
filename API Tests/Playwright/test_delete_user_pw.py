import pytest
from playwright.sync_api import APIRequestContext

@pytest.mark.smoketest
def test_delete_user(api_request_context: APIRequestContext, test_token_pw) -> None:

    token = test_token_pw

    header = {
        'Authorization': f"Bearer {token}"
    }

    response = api_request_context.delete(url = "/users/me", headers = header)

    assert response.ok is True
    print("User Deleted Successfully")