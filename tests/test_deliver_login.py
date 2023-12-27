import helpers
import allure
import pytest_check as check
from tests.data import urls, resp_codes_msg


class TestDeliverLogin:

    @allure.title('Тест логина')
    @allure.description('Логинимся и ожидаем id курьера в ответе')
    def test_login_expected_id_in_response(self, deliver):
        """Тест успешной авторизации, авторизация возвращает id курьера"""
        resp = helpers.create_post_response(urls.login_url, deliver[0], deliver[1])
        assert str(deliver[3]) in resp.text
        check.equal(resp.status_code, 200)

    @allure.title('Тест логина с незаполненным логином')
    @allure.description('Логинимся с незаполненным логином и ожидаем ошибку')
    def test_login_empty_login_field_expected_error(self, deliver):
        """Тест логина с незаполненным логином"""
        resp = helpers.create_post_response(urls.login_url, '', deliver[1])
        assert resp_codes_msg.code_400 in resp.text
        check.equal(resp.status_code, 400)

    @allure.title('Тест логина с незаполненным паролем')
    @allure.description('Логинимся с незаполненным паролем и ожидаем ошибку')
    def test_login_empty_pass_field_expected_error(self, deliver):
        """Тест логина с незаполненным паролем"""
        resp = helpers.create_post_response(urls.login_url, deliver[0], '')
        assert resp_codes_msg.code_400 in resp.text
        check.equal(resp.status_code, 400)

    @allure.title('Тест логина незарегистрированного курьера')
    @allure.description('Логинимся с незарегистрированными данными и ожидаем ошибку')
    def test_login_unregister_user_expected_error(self, deliver):
        """Тест логина незарегистрированного курьера"""
        resp = helpers.create_post_response(urls.login_url, "Unregister_user_login", "Unregister_user_pass")
        assert resp_codes_msg.code_404 in resp.text
        check.equal(resp.status_code, 404)

