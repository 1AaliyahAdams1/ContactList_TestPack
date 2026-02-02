import pytest
from playwright.sync_api import APIRequestContext

@pytest.mark.xfail
@pytest.mark.regressiontest
def test_patch_contact(api_request_context: APIRequestContext, test_token_pw, test_user_pw) -> None:

    token = test_token_pw

    request_json = {

        "firstName": "Anna"
    }

    header = {
        'Authorization': f"Bearer {token}"
    }

    response = api_request_context.patch(url = "/contacts/",data = request_json, headers = header)

    assert response.ok is True

    print("Contact Patched Successfully")
