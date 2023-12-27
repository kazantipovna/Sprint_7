import pytest
import pytest_check as check
import allure
import helpers
from tests.data import urls, test_data, resp_codes_msg


class TestDeliverCreate:
    @allure.title('Тест создания курьера')
    @allure.description('Создаем курьера и проверяем, что его данные не пустые')
    def test_deliver_create_correct(self, deliver):
        """Курьера можно создать"""
        assert deliver != []

    @allure.title('Тест успешного кода')
    @allure.description('Создаем курьера и проверяем, что вернулся успешный код 201')
    def test_deliver_create_check_expected_ok(self):
        """Создаем курьера и проверяем, что вернулся код 201 {"ok":true}"""
        resp = helpers.create_post_response(urls.register_url,
                                            test_data.register_ok[0],
                                            test_data.register_ok[1],
                                            test_data.register_ok[2])
        assert resp_codes_msg.code_201 in resp.text
        check.equal(resp.status_code, 201)
        helpers.delete_deliver(helpers.get_deliver_id(test_data.register_ok[0], test_data.register_ok[1]))

    @allure.title('Тест создания двух одинаковых курьеров')
    @allure.description('Создаем курьера, создаем точно такого же, и проверяем, что вернулся код ошибки')
    def test_deliver_create_exist_deliver_expected_error(self, deliver):
        """Нельзя создать двух одинаковых курьеров"""
        resp = helpers.create_post_response(urls.register_url, deliver[0], deliver[1], deliver[2])
        assert resp_codes_msg.code_409 in resp.text
        check.equal(resp.status_code, 409)

    @allure.title('Тест создания курьера с уже существующим логином')
    @allure.description('Создаем курьера, создаем с таким же логином, и проверяем, что вернулся код ошибки')
    def test_deliver_create_same_login_expected_error(self, deliver):
        """Создаем курьера с логином, который уже есть, возвращается ошибка"""
        resp = helpers.create_post_response(urls.register_url, deliver[0], deliver[0], deliver[0])
        assert resp_codes_msg.code_409 in resp.text
        check.equal(resp.status_code, 409)

    @allure.title('Тест создания курьера с незаполненным обязательным полем')
    @allure.description('Если одно из полей не заполнено, ожидаем ошибку')
    @pytest.mark.parametrize("login, password, firstName", test_data.register_field_missed)
    def test_deliver_create_empty_field_expected_error(self, login, password, firstName):
        """Создаем курьера с незаполненным обязательным полем"""
        resp = helpers.create_post_response(urls.register_url, login, password, firstName)
        assert resp_codes_msg.code_400 in resp.text
        check.equal(resp.status_code, 400)

