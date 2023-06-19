import requests


def send_request(url, payload, headers):
    response = requests.post(url, json=payload, headers=headers)
    return response

def assert_status_code(response, expected_code):
    assert response.status_code == expected_code

def assert_json_value(response, key, expected_value):
    assert response.json()[key] == expected_value