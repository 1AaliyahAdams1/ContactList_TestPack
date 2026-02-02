import allure
import requests
import pytest
import globals_api
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@allure.title("Post User API")
@allure.description("Testing creating a user")
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

    if req.status_code != 201:
        logger.error(f"API call failed --> {req.status_code}")
        logger.error(f"Status code received--> {req.status_code}")
    else:
        logger.info(f"Response is --> {req.json()}")
        logger.info(f"Status code received--> {req.status_code}")

    print("Post user successful")


