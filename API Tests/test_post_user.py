import requests
import pytest
import globals_api

@pytest.mark.smoke_test
def test_post_user():
    request_json ={
        "firstName": globals_api.firstName,
        "lastName": globals_api.lastName,
        "email": globals_api.generateEmail(),
        "password": globals_api.password
    }

    header = {
        'Authorization' : "Bearer {{token}}"
    }
    req = requests.request(method = "POST",
                           url= globals_api.post_user,
                           json=request_json,
                           headers = header)

    print(req.json())

    assert req.status_code == 201, "API Call Failed"

    print("Post user successful")



test_post_user()