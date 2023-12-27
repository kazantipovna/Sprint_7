import requests
import random
import string
import allure
from tests.data import urls


@allure.step('Создаем курьера:')
def register_new_courier_and_return_login_password():
    """Создаем курьера, записываем его данные в список и возвращаем этот список"""
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(urls.register_url, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    deliver_id = get_deliver_id(login_pass[0], login_pass[1])
    login_pass.append(deliver_id)

    with allure.step(f'Создан курьер login = {login_pass[0]}, password = {login_pass[1]}, '
                     f'first_name = {login_pass[2]}, deliver_id = {login_pass[3]}:'):
        return login_pass


def create_payload(login, password, name=None):
    """Заполняет payload из данных курьера"""
    payload = {"login": login, "password": password, "firstName": name}
    return payload


@allure.step('Выполняем запрос:')
def create_post_response(url, login, password, name=None):
    """Создает post запрос"""
    payload = create_payload(login, password, name)
    response = requests.post(url, data=payload)
    return response


@allure.step('Получаем id курьера:')
def get_deliver_id(login, password):
    """Возвращает id курьера после логина"""
    deliver_id = create_post_response(urls.login_url, login, password).json()['id']
    return deliver_id


@allure.step('Удаляем курьера по его id:')
def delete_deliver(deliver_id):
    """Удаляет курьера по его id"""
    payload = {"id": deliver_id}
    response = requests.delete(urls.register_url + f'/{deliver_id}', data=payload)
    return response
