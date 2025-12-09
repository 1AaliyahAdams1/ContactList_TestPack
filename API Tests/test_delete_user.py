import requests
import pytest
import globals_api

@pytest.mark.smoke_test
def test_delete_user(test_token):

    token = test_token
    header = {
        'Authorization' : f'Bearer {token}'
    }

    response = requests.request(method="DELETE",
                           url= globals_api.delete_user,
                           headers = header)


    assert response.status_code == 200, "API call failed"
    print("Delete user successful")
