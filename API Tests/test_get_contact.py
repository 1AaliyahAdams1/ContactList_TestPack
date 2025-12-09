import requests
import pytest
import globals_api

@pytest.mark.regression_test
def test_get_contact(test_token, test_user):
    token = test_token

    header = {
        'Authorization': f'Bearer {token}'
    }

    req = requests.request(method= "GET",
                           url= globals_api.get_contact,
                           headers= header)
    assert req.status_code == 200, "API Call failed"
    print("Get contact successful")



