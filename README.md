# HW9**Задание.** Стабилизируйте автотесты из домашнего задания 8 “Знакомство с библиотекой Requests” на методы:

- [GET] /employee
- [POST] /employee
- [GET] /employee/{id}
- [PATCH] /employee/{id}

Добавьте в тесты методы работы с БД, которые создают, удаляют, редактируют и вычитывают записи из БД.

**Строка подключения к БД:** `postgres://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients`

**Таблица:** employee

**Структура таблицы:**

| Названиe | Тип данных	 | Not Null	 | Значение По умолчанию |
| --- | --- | --- | --- |
| id | int | + | автоинкремент |
| isActive | bool | + | true |
| createDateTime | timestamp | + | функция в БД now() |
| lastChangedDateTime | timestamp | + | функция в БД now() |
| first_name | varchar(20) | + |  |
| last_name | varchar(20) | + |  |
| middle_name | varchar(20) |  |  |
| phone | varchar(15) | + |  |
| email | varchar(256) |  |  |
| avatar_url | varchar(1024) |  |  |
| companyId | int |  |  |

**Требования:**

- тесты должны работать с библиотекой `pytest`
- тесты должны использовать библиотеку `requests`
- тесты должны использовать библиотеку `SQLAlchemy`
- тесты должны предварительно создавать себе тестовые данные через обращение к БД
- тесты должны удалять за собой созданные данные через обращение к БД
- тесты должны быть стабильны:
    - их не нужно редактировать перед каждым запуском
    - повторный запуск теста приводит к тому же статусу

🤓 если сервис не получает запросы 30 минут, он выключается. Первое обращение к сервису потребует больше времени (около 2 минут), т.к. сервис запускается заново. Учитывайте это при работе.

**Swagger:** [https://x-clients-be.onrender.com/docs/](https://x-clients-be.onrender.com/docs/)

**URL приложения:** [https://x-clients-be.onrender.com](https://x-clients-be.onrender.com)
