import allure
import requests
import pytest
import globals_api

@allure.title("Get ContactList API")
@allure.description("Testing Getting contact list")
@allure.suite("Suite")
@allure.suite("Suite")
@pytest.mark.regression_test
def test_get_contactlist(test_token, test_user):

    token = test_token

    header = {
        'Authorization': f'Bearer {token}'
    }

    req = requests.request(method="GET",
                           url=globals_api.get_contactlist,
                           headers=header)
    assert req.status_code == 200, "API Call failed"

    print("Get contact list successful")

