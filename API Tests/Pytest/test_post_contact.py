import allure
import requests
import pytest
import globals_api
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@allure.title("Post Contact API")
@allure.description("Testing creating a contact")
@pytest.mark.regression_test
def test_post_contact(test_token, test_user):

    token = test_token

    header = {
        "Authorization": f"Bearer {token}"
    }

    response_json = {
    "firstName": "John",
    "lastName": "Doe",
    "birthdate": "1970-01-01",
    "email": "jdoe@fake.com",
    "phone": "8005555555",
    "street1": "1 Main St.",
    "street2": "Apartment A",
    "city": "Anytown",
    "stateProvince": "KS",
    "postalCode": "12345",
    "country": "USA"
}
    req = requests.request(method="POST",
                           url=globals_api.post_contact,
                           json=response_json,
                           headers=header)

    print(req.json())

    assert req.status_code == 201, "API Call Failed"

    logger.info(f"Token received --> {token}")

    if req.status_code != 201:
        logger.error(f"API call failed --> {req.status_code}")
        logger.error(f"Status code received--> {req.status_code}")
    else:
        logger.info(f"Response is --> {req.json()}")
        logger.info(f"Status code received--> {req.status_code}")

    print("Post contact successful")