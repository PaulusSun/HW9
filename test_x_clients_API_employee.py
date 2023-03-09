from metods_for_db import EmployeeTable
from X_clients_API_employee import X_clients_API_employee
from X_clients_API_company import X_clients_API_company
from X_clients_API_auth import X_clients_API_auth

base_url = "https://x-clients-be.onrender.com"

# Валидный login_password
login_password = {
    "username": "stella", 
    "password": "sun-fairy"
    }

x_clients_API_auth = X_clients_API_auth(base_url, login_password)
x_clients_API_company = X_clients_API_company(base_url)
x_clients_API_employee = X_clients_API_employee(base_url)
db = EmployeeTable("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")

def test_GET_employee():
    db.add_company()
    company_id = db.get_max_company_id()
    db.add_employee(company_id)
    employee_list_API = len(x_clients_API_employee.GET_employee_from_id_company(company_id))
    employee_list_DB = len(db.get_employee_list(company_id))

    assert employee_list_API == employee_list_DB

    db.delete_employee_by_company_id(company_id)
    db.delete_company(company_id)

def test_POST_employee():
    db.add_company()
    company_id = db.get_max_company_id()
    employee_list_DB_before = len(db.get_employee_list(company_id))
    auth = x_clients_API_auth.auth()
    x_clients_API_employee.POST_employee(auth, company_id)
    employee_list_DB_after = len(db.get_employee_list(company_id))
    
    assert employee_list_DB_after - employee_list_DB_before == 1

    db.delete_employee_by_company_id(company_id)
    db.delete_company(company_id)

def test_GET_employee_id():
    db.add_company()
    company_id = db.get_max_company_id()
    db.add_employee(company_id)
    employee_id = db.get_max_employee_id(company_id)
    employee_API = x_clients_API_employee.GET_employee_id(employee_id)
    employee_DB = db.get_employee_by_id(employee_id, company_id)[0]
 
    assert employee_DB["companyId"] == employee_API["companyId"]
    assert employee_DB["first_name"] == employee_API["firstName"]
    assert employee_DB["last_name"] == employee_API["lastName"]
    assert employee_DB["middle_name"] == employee_API["middleName"]
    assert employee_DB["phone"] == employee_API["phone"]
    assert employee_DB["avatar_url"] == employee_API["avatar_url"]
    assert employee_DB["email"] == employee_API["email"]
    assert employee_DB["isActive"] == employee_API["isActive"]
  
    db.delete_employee_by_company_id(company_id)
    db.delete_company(company_id)  

def test_PATCH_employee_id():
    db.add_company()
    company_id = db.get_max_company_id()
    db.add_employee(company_id)
    employee_id = db.get_max_employee_id(company_id)
    auth = x_clients_API_auth.auth()
    

    employee_API = x_clients_API_employee.PATCH_employee_id(employee_id, auth)
    employee_DB = db.get_employee_by_id(employee_id, company_id)[0]

    assert employee_DB["avatar_url"] == employee_API["url"]
    assert employee_DB["email"] == employee_API["email"]
    assert employee_DB["isActive"] == employee_API["isActive"]
    assert employee_DB["last_name"] == employee_API["lastName"]

    db.delete_employee_by_company_id(company_id)
    db.delete_company(company_id) 