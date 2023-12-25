import json

import requests
import random
import string
from data import urls
import allure
from data import test_data


@allure.title('Создание курьера')
@allure.description('Создаем курьера, записываем его данные в список и возвращаем этот список')
def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    with allure.step('Заполняем payload рандомно сгенерированными данными:'):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

    with allure.step('Отправляем запрос на создание курьера:'):
        response = requests.post(urls.register_url, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

    with allure.step('Логинимся для получения id курьера:'):
        deliver_id = get_deliver_id(login_pass[0], login_pass[1])
        login_pass.append(deliver_id)

    with allure.step(f'Создан курьер login = {login_pass[0]}, password = {login_pass[1]}, '
                     f'first_name = {login_pass[2]}, deliver_id = {login_pass[3]}:'):
        return login_pass


@allure.description('Удаляем курьера по его id')
def delete_deliver(deliver_id):
    payload = {"id": deliver_id}
    with allure.step(f'Удаляем курьера с id = {deliver_id}'):
        response = requests.delete(urls.register_url + f'/{deliver_id}', data=payload)
        return response


@allure.description('Выполняем логин курьера, чтобы получить его id')
def get_deliver_id(name, password):
    payload = {"login": name, "password": password}
    deliver_id = requests.post(urls.login_url, data=payload).json()['id']
    with allure.step(f'Получили id курьера = {deliver_id}:'):
        return deliver_id
