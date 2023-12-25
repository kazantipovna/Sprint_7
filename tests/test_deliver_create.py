import requests
import pytest
from data import test_data, resp_codes_msg
from data import urls
import pytest_check as check
import allure
import helpers


class TestDeliverCreate:
    @allure.title('Тест создания курьера')
    @allure.description('Создаем курьера и проверяем, что его данные не пустые')
    def test_deliver_create_correct(self, deliver):
        """Курьера можно создать"""
        with allure.step(f'Создан курьер с id = {deliver[3]}:'):
            assert deliver != []

    @allure.title('Тест успешного кода')
    @allure.description('Создаем курьера и проверяем, что вернулся успешный код 201')
    def test_deliver_create_check_expected_ok(self):
        """Создаем курьера и проверяем, что вернулся код 201 {"ok":true}"""
        with allure.step(f'Создаем курьера с параметрами {test_data.register_ok}:'):
            payload_reg = {"login": test_data.register_ok[0],
                           "password": test_data.register_ok[1],
                           "firstName": test_data.register_ok[2]}
            response_reg = requests.post(urls.register_url, data=payload_reg)
        with allure.step(f'Проверяем ответ = {response_reg}:'):
            assert resp_codes_msg.code_201 in response_reg.text
            check.equal(response_reg.status_code, 201)
        with allure.step(f'Удаляем курьера после теста:'):
            helpers.delete_deliver(helpers.get_deliver_id(test_data.register_ok[0], test_data.register_ok[1]))

    @allure.title('Тест создания двух одинаковых курьеров')
    @allure.description('Создаем курьера, создаем точно такого же, и проверяем, что вернулся код ошибки')
    def test_deliver_create_exist_deliver_expected_error(self, deliver):
        """Нельзя создать двух одинаковых курьеров"""
        with allure.step(f'Создан курьер = {deliver}:'):
            payload = {"login": deliver[0], "password": deliver[1], "firstName": deliver[2]}
        with allure.step(f'Создаем такого же = {deliver}:'):
            response = requests.post(urls.register_url, data=payload)
        with allure.step(f'Проверяем ответ = {response}:'):
            assert resp_codes_msg.code_409 in response.text
            check.equal(response.status_code, 409)

    @allure.title('Тест создания курьера с уже существующим логином')
    @allure.description('Создаем курьера, создаем с таким же логином, и проверяем, что вернулся код ошибки')
    def test_deliver_create_same_login_expected_error(self, deliver):
        """Создаем курьера с логином, который уже есть, возвращается ошибка"""
        with allure.step(f'Создан курьер с логином = {deliver[0]}, создаем еще одного с таким же логином:'):
            payload = {"login": deliver[0], "password": deliver[0], "firstName": deliver[0]}
            response = requests.post(urls.register_url, data=payload)
        with allure.step(f'Проверяем ответ = {response}:'):
            assert resp_codes_msg.code_409 in response.text
            check.equal(response.status_code, 409)

    @allure.title('Тест создания курьера с незаполненным обязательным полем')
    @allure.description('Если одно из полей не заполнено, ожидаем ошибку')
    @pytest.mark.parametrize("login, password, firstName", test_data.register_field_missed)
    def test_deliver_create_empty_field_expected_error(self, login, password, firstName):
        """Создаем курьера с незаполненным обязательным полем"""
        with allure.step(f'Пытаемся создать курьера без обязательного поля = {test_data.register_field_missed}:'):
            payload = {"login": login, "password": password, "firstName": firstName}
            response = requests.post(urls.register_url, data=payload)
        with allure.step(f'Проверяем ответ = {response}:'):
            assert resp_codes_msg.code_400 in response.text
            check.equal(response.status_code, 400)
