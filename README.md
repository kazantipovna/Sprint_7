# Sprint 7

---
#### Тесты на проверку API учебного сервиса Яндекс Самокат

---

### Каталог tests:
* __test_deliver_create.py__ - тесты создания курьера:
  * **Тесты:**
    * test_deliver_create_correct - тест создания курьера, проверяем, что данные созданного курьера не пустые
    * test_deliver_create_check_expected_ok - Создаем курьера и проверяем, что вернулся код 201 {"ok":true}
    * test_deliver_create_exist_deliver_expected_error - тест на создание двух одинаковых курьеров
    * test_deliver_create_same_login_expected_error - тест на создание курьера с логином, который уже есть
    * test_deliver_create_empty_field_expected_error - тест создания курьера с незаполненным обязательным полем

* __test_deliver_delete.py__ - тесты удаления курьера:
  * **Тесты:**
    * test_delete_deliver_expected_ok - создаем и удаляем курьера, проверяем успешный код удаления
  
* __test_deliver_login.py__ - тесты логина курьера:
  * **Тесты:**
    * test_login_expected_id_in_response - тест успешной авторизации
    * test_login_empty_login_field_expected_error - Тест логина с незаполненным логином
    * test_login_empty_pass_field_expected_error - Тест логина с незаполненным паролем
    * test_login_unregister_user_expected_error - Тест логина незарегистрированного курьера

* __test_order.py__ - тесты цветов при заказе:
  * **Тесты:**
    * test_choose_scooter_color_expected_ok - Тест заказа самоката с выбором всех возможных комбинаций цветов
    
* __test_orders_list.py__ - тест списка заказов курьера:
  * **Тесты:**
    * test_choose_scooter_color_expected_ok - Тест списка заказов курьера

* __helpers.py__ - вспомогательные методы
  * register_new_courier_and_return_login_password - метод создания курьера, возвращает его данные
  * create_payload - Заполняет payload из данных курьера
  * create_post_response - Создает post запрос
  * get_deliver_id - возвращает id курьера
  * delete_deliver - метод удаляет курьера по его id

* __conftest.py__ - фикстуры


  #### Каталог tests/data:
  * __urls.py__ - ссылки-ручки
  * __resp_codes_msg.py__ - сообщения кодов для сверки результатов
  * __test_data.py__ - прочие вспомогательные тестовые данные
