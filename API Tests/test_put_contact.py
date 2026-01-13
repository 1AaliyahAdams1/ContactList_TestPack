import allure
import requests
import pytest
import globals_api

@allure.title("Put Contact API")
@allure.description("Testing updating a contact API - will always fail")
@pytest.mark.xfail(reason="Put contact fails")
@pytest.mark.regression_test
def test_put_contact(test_token, test_user):
    token = test_token

    header = {
        "Authorization": f"Bearer {token}"
    }

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
    req = requests.request(method="PUT",
                           url=globals_api.put_contact,
                           headers=header,
                           json=request_json)

    #print(req.json())

    assert req.status_code == 200, "API Call Failed"

    print("Put contact successful")