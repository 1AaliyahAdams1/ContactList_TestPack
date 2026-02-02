import pytest
import requests
import globals_api
import allure

@allure.title("Delete Contact API")
@allure.description("Testing deleting a user - will always fail")
@pytest.mark.xfail(reason="Delete contact fails")
@pytest.mark.regression_test
def test_delete_contact(test_token, test_user):
    token = test_token

    header = {
        'Authorization': f'Bearer {token}'
    }

    req = requests.request(method= 'DELETE',
                           url= globals_api.delete_contact,
                           headers= header)

    assert req.status_code == 200, "API call failed"
    print("Delete contact successful")
