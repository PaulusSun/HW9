
import requests

class X_clients_API_company:
    def __init__(self, base_url):
        self.base_url = base_url

    def GET_id_company(self):
        company_list = requests.get(self.base_url+"/company")
        id_company = company_list.json()[3]['id']
        return id_company