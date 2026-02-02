import pytest
from playwright.sync_api import APIRequestContext

@pytest.mark.xfail
@pytest.mark.regressiontest
def test_put_contact(api_request_context: APIRequestContext, test_token_pw, test_user_pw) -> None:

    token = test_token_pw

    request_json = {
        "firstName": "Amy",
        "lastName": "Miller",
        "birthdate": "1992-02-02",
        "email": "amiller@fake.com",
        "phone": "8005554242",
        "street1": "13 School St.",
        "street2": "Apt. 5",
        "city": "Washington",
        "stateProvince": "QC",
        "postalCode": "A1A1A1",
        "country": "Canada"
    }

    header = {
        'Authorization': f"Bearer {token}"
    }

    response = api_request_context.put(url = "/contacts",data = request_json, headers = header)

    assert response.ok is True

    print("Put Contact Ran Successfully")
