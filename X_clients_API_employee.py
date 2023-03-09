import requests
from faker import Faker
fake = Faker()
fake_ru = Faker("ru_RU")

class X_clients_API_employee:
    def __init__(self, base_url):
        self.base_url = base_url
        
# - [GET] /employee Получить список сотрудников для компании
    def GET_employee_from_id_company(self, id_company):
        resp = requests.get(self.base_url+'/employee?company='+str(id_company))
        return resp.json()
    
# - [POST] /employee Добавить нового сотрудника
    def POST_employee(self, auth, company_id):
        new_employee = {
            "companyId": str(company_id),
            "firstName": str(fake_ru.first_name()),
            "lastName": str(fake_ru.last_name()),
            "middleName": str(fake_ru.middle_name()),
            "phone": str('+7{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}'.format(*[i for i in fake_ru.phone_number() if i.isdigit()][1:])),
            "url": str(fake.url())
            }
        resp = requests.post(self.base_url+'/employee', json = new_employee, headers = auth)
        employee_id = resp.json()['id']
        return employee_id

# - [GET] /employee/{id} Получить сотрудника по ID
    def GET_employee_id(self, employee_id):
        resp = requests.get(self.base_url+'/employee/'+str(employee_id))
        return resp.json()

# [PATCH] /employee/{id} Изменить информацию о сотруднике
    def PATCH_employee_id(self, employee_id, auth):
        new_employee_correctly = {
            "lastName": fake.last_name(),
            "email": fake.email(),
            "url": fake.url(),
            "isActive": True
            }
        resp = requests.patch(self.base_url+'/employee/'+str(employee_id), headers = auth, json = new_employee_correctly)
        return resp.json()
    
    
