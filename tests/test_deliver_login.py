import requests
from data import resp_codes_msg
from data import urls
import allure
import pytest_check as check


class TestDeliverLogin:

    @allure.title('Тест логина')
    @allure.description('Логинимся и ожидаем id курьера в ответе')
    def test_login_expected_id_in_response(self, deliver):
        """Тест успешной авторизации, авторизация возвращает id курьера"""
        payload = {"login": deliver[0], "password": deliver[1]}
        with allure.step(f'Логинимся с параметрами login = {deliver[0]}, password = {deliver[1]}:'):
            response = requests.post(urls.login_url, data=payload)
        with allure.step(f'Проверяем ответ = {response}:'):
            assert str(deliver[3]) in response.text
            check.equal(response.status_code, 200)

    @allure.title('Тест логина с незаполненным полем')
    @allure.description('Логинимся с незаполненным обязательным полем и ожидаем ошибку')
    def test_login_empty_required_field_expected_error(self, deliver):
        """Тест логина с незаполненным логином или незаполненным паролем"""
        payload = [{"login": deliver[0], "password": ""}, {"login": "", "password": deliver[1]}]
        for i in range(len(payload)):
            with allure.step(f'Логинимся с параметрами {payload[i]}:'):
                response = requests.post(urls.login_url, data=payload[i])
                with allure.step(f'Проверяем ответ = {response}:'):
                    assert resp_codes_msg.code_400 in response.text
                    check.equal(response.status_code, 400)

    @allure.title('Тест логина незарегистрированного курьера')
    @allure.description('Логинимся с незарегистрированными данными и ожидаем ошибку')
    def test_login_unregister_user_expected_error(self, deliver):
        """Тест логина незарегистрированного курьера"""
        payload = {"login": "Unregister_user_login", "password": "Unregister_user_pass"}
        with allure.step(f'Логинимся с параметрами {payload}:'):
            response = requests.post(urls.login_url, data=payload)
        with allure.step(f'Проверяем ответ = {response}:'):
            assert resp_codes_msg.code_404 in response.text
            check.equal(response.status_code, 404)

