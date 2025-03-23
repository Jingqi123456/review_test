import config
import requests


class LoginApi:
    def __init__(self):
        self.verify_url = config.url + "/index.php?m=Home&c=user&a=verify"
        self.login_url = config.url + "/index.php?m=Home&c=user&a=do_login"
        self.session = requests.Session()

    def verify_login(self, data):
        self.session.get(self.verify_url)
        login_response = self.session.post(self.login_url, data=data)
        return login_response
