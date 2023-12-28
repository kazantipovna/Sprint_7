import json
import requests
import pytest
import pytest_check as check
import allure
from tests.data import urls, test_data, resp_codes_msg


class TestScooterColor:

    @allure.title('Тест выбора цвета самоката')
    @allure.description('Проверяем возможность выбрать цвета самоката при заказе')
    @pytest.mark.parametrize("color", ['["BLACK"]', '["GREY"]', '["BLACK", "GREY"]', '[]'])
    def test_choose_scooter_color_expected_ok(self, color):
        """Тест заказа самоката с выбором цвета"""
        test_data.order_data["color"] = color
        payload = test_data.order_data
        with allure.step(f'Заказываем самокат цвета {color}'):
            response = requests.post(urls.order_url, data=json.dumps(payload))
            assert resp_codes_msg.order_ok in response.text
            check.equal(response.status_code, 201)
