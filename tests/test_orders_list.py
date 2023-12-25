import allure
import requests
from data import resp_codes_msg
from data import urls
import pytest_check as check


class TestOrdersList:

    @allure.title('Тест списка заказов курьера')
    @allure.description('Проверяем, что в тело ответа возвращается список заказов')
    def test_deliver_orders_list_expected_ok(self, deliver):
        """Тест списка заказов курьера, в ответе ожидаем ordersCount"""
        payload = {"id": deliver[3]}
        with allure.step(f'Получаем список заказов курьера с id = {deliver[3]}:'):
            response = requests.get(urls.register_url + f'{deliver[3]}/ordersCount', data=payload)
        with allure.step(f'Проверяем ответ = {response}:'):
            assert resp_codes_msg.order_list in response.text
            check.equal(response.status_code, 200)
