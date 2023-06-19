from config import token, URL_ADD, URL_CHECK
from helpers import send_request, assert_status_code, assert_json_value

class TestAddBL:
    def test_add_BL8(self):
        headers = {'Content-type': 'application/json; charset=UTF-8',
                   'Authorization': f'Bearer {token}'}
        payload = {"numbers": ["89953168411"]}
        response = send_request(URL_ADD, payload, headers)
        assert_status_code(response, 200)
        payload_check = {"number": "79953168411"}
        response_check = send_request(URL_CHECK, payload_check, headers)
        assert_status_code(response_check, 200)
        assert_json_value(response_check, "is_exist", True)

    def test_add_BL7(self):
        headers = {'Content-type': 'application/json; charset=UTF-8',
                   'Authorization': f'Bearer {token}'}
        payload = {"numbers": ["+79953168411"]}
        response = send_request(URL_ADD, payload, headers)
        assert_status_code(response, 200)
        payload_check = {"number": "89953168411"}
        response_check = send_request(URL_CHECK, payload_check, headers)
        assert_status_code(response_check, 200)
        assert_json_value(response_check, "is_exist", True)

    def test_min_phone_length(self):
        headers = {'Content-type': 'application/json; charset=UTF-8',
                   'Authorization': f'Bearer {token}'}
        payload = {"numbers": ["796499235"]}
        response = send_request(URL_ADD, payload, headers)
        assert_status_code(response, 200)
        payload_check = {"number": "796499235"}
        response_check = send_request(URL_CHECK, payload_check, headers)
        assert_status_code(response_check, 200)
        assert_json_value(response_check, "is_exist", True)

    def test_max_phone_length(self):
        headers = {
            'Content-type': 'application/json; charset=UTF-8',
            'Authorization': f'Bearer {token}'}
        payload = {"numbers": ["123456789012345678"]}
        response = send_request(URL_ADD, payload, headers)
        assert_status_code(response, 200)
        payload_check = {"number": "123456789012345678"}
        response_check = send_request(URL_CHECK, payload_check, headers)
        assert_status_code(response_check, 200)
        assert_json_value(response_check, "is_exist", True)


class TestNegativeScenario:
    def test_invalid_json(self):
        headers = {
            'Content-type': 'application/json; charset=UTF-8',
            'Authorization': f'Bearer {token}'}
        payload = "pusto"
        response = send_request(URL_ADD, payload, headers)
        assert_status_code(response, 400)

    def test_spec_symbol(self):
        headers = {
            'Content-type': 'application/json; charset=UTF-8',
            'Authorization': f'Bearer {token}'}
        payload = "*7995318411"
        response = send_request(URL_ADD, payload, headers)
        assert_status_code(response, 400)