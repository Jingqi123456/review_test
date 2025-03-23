import pytest
from common.read_json import read_json
from api.login_api import LoginApi


class TestLogin:
    def setup_class(self):
        self.login = LoginApi()

    @pytest.mark.parametrize("request_body, status, msg, status_code", read_json('login_data.json'))
    def test_login(self, request_body, status, msg, status_code):
        login_response = self.login.verify_login(data=request_body)
        assert status_code == login_response.status_code
        assert msg in login_response.json().get("msg")
        assert status == login_response.json().get("status")

