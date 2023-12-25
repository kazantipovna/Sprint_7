import json
import requests
import pytest
from data import resp_codes_msg, test_data
from data import urls
import pytest_check as check
import allure


class TestScooterColor:

    @allure.title('Тест выбора цвета самоката')
    @allure.description('Проверяем возможность выбрать цвета самоката при заказе')
    @pytest.mark.parametrize("color", ['["BLACK"]', '["GREY"]', '["BLACK", "GREY"]', '[]'])
    def test_choose_scooter_color_expected_ok(self, color):
        """Тест заказа самоката с выбором цвета"""
        with allure.step(f'Изменяем цвет в словаре с параметрами заказа, теперь "color" = {color}:'):
            test_data.order_data["color"] = color
        with allure.step(f'Заполняем payload словарем:'):
            payload = test_data.order_data
        with allure.step(f'Выполняем запрос с параметрами = {payload}:'):
            response = requests.post(urls.order_url, data=json.dumps(payload))
        with allure.step(f'Проверяем ответ = {response}:'):
            assert resp_codes_msg.order_ok in response.text
            check.equal(response.status_code, 201)
