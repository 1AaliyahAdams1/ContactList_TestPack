import requests
import pytest
import globals_api

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

    print("Patch contact successful")