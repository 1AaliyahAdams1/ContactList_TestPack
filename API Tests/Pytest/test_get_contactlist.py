import allure
import requests
import pytest
import globals_api
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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

    logger.info(f"Token received --> {token}")

    if req.status_code != 200:
        logger.error(f"API call failed --> {req.status_code}")
        logger.error(f"Status code received--> {req.status_code}")
    else:
        logger.info(f"Response is --> {req.json()}")
        logger.info(f"Status code received--> {req.status_code}")

    print("Get contact list successful")