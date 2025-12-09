import requests
import pytest
import globals_api

@pytest.fixture
def test_user(test_token):

    token = test_token

    yield

    header = {
        'Authorization' : f'Bearer {token}'
    }

    response = requests.request(method="DELETE",
                           url= globals_api.delete_user,
                           headers = header)

    assert response.status_code == 200, "API call failed"
    print("User deleted")



@pytest.fixture
def test_token():
    request_json = {
        "firstName": globals_api.firstName,
        "lastName": globals_api.lastName,
        "email": globals_api.generateEmail(),
        "password": globals_api.password
    }

    header = {
        'Authorization': 'Bearer {{token}}'
    }
    req = requests.request(method="POST",
                           url=globals_api.post_user,
                           json=request_json,
                           headers=header)

    print(req.json())
    assert req.status_code == 201, "API call failed"
    print("User created")

    token = req.json()['token']
    print("Token generated")
    return token