import allure
import requests
import pytest_check as check
from tests.data import urls, resp_codes_msg


class TestOrdersList:

    @allure.title('Тест списка заказов курьера')
    @allure.description('Проверяем, что в тело ответа возвращается список заказов')
    def test_deliver_orders_list_expected_ok(self, deliver):
        """Тест списка заказов курьера, в ответе ожидаем ordersCount"""
        payload = {"id": deliver[3]}
        with allure.step(f'Получаем список заказов курьера {payload}'):
            response = requests.get(urls.register_url + f'{deliver[3]}/ordersCount', data=payload)
            assert resp_codes_msg.order_list in response.text
            check.equal(response.status_code, 200)
