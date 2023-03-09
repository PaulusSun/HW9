import requests

class X_clients_API_auth:
    def __init__(self, base_url, login_password):
        self.base_url = base_url
        self.login_password = login_password

    def auth(self):
        resp = requests.post(self.base_url+"/auth/login", json = self.login_password)
        my_headers = {
        'x-client-token': resp.json()["userToken"]
        }
        return my_headers