import pytest
from playwright.sync_api import APIRequestContext

@pytest.mark.regressiontest
def test_patch_contact(api_request_context: APIRequestContext, test_token_pw, test_user_pw) -> None:

    token = test_token_pw

    request_json = {
        "firstName": "John",
        "lastName": "Doe",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }

    header = {
        'Authorization': f"Bearer {token}"
    }

    response = api_request_context.post(url = "/contacts",data = request_json, headers = header)

    assert response.ok is True

    print("Contact Created Successfully")
