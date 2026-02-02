import allure
import requests
import pytest
import globals_api
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@allure.title("Delete User API")
@allure.description("Testing deleting a user")
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

    logger.info(f"Token received --> {token}")

    if response.status_code != 200:
        logger.error(f"Status code received--> {response.status_code}")
    else:
        logger.info(f"Status code received--> {response.status_code}")

    print("Delete user successful")
