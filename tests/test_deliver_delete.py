import allure
import helpers
import pytest_check as check
from tests.data import resp_codes_msg


class TestDeliverDelete:

    @allure.title('Тест удаления курьера')
    @allure.description('Создаем курьера, удаляем, и проверяем, что в ответе вернулся успешный код')
    def test_delete_deliver_expected_ok(self):
        """Проверяем удаление курьера"""
        deliver = helpers.register_new_courier_and_return_login_password()
        del_deliver = helpers.delete_deliver(deliver[3])
        assert resp_codes_msg.code_201 in del_deliver.text
        check.equal(del_deliver.status_code, 200)
