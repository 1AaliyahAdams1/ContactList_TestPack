import pytest
from playwright.sync_api import APIRequestContext

@pytest.mark.regressiontest
def test_get_contact(api_request_context: APIRequestContext, test_token_pw, test_user_pw) -> None:

    token = test_token_pw

    header = {
        'Authorization': f"Bearer {token}"
    }

    response = api_request_context.get(url = "/contacts/", headers = header)

    assert response.ok is True

    print("Contact Fetched Successfully")
