import allure
import requests
import pytest
import globals_api
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@allure.title("Patch Contact API")
@allure.description("Testing updating a contact - will always fail")
@pytest.mark.xfail(reason="Patch contact fails")
@pytest.mark.regression_test
def test_patch_contact(test_token, test_user):

    token = test_token

    request_json = {

        "firstName": "Anna"
    }

    header = {
        'Authorization': f'Bearer {token}'
    }

    req = requests.request(method="PATCH",
                           url=globals_api.patch_contact,
                           json = request_json,
                           headers=header)

    #print(req.json())

    assert req.status_code == 200, "API Call failed"

    logger.info(f"Token received --> {token}")

    if req.status_code != 200:
        logger.error(f"API call failed --> {req.status_code}")
        logger.error(f"Status code received--> {req.status_code}")
    else:
        logger.info(f"Response is --> {req.json()}")
        logger.info(f"Status code received--> {req.status_code}")

    print("Patch contact successful")