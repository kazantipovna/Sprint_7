import pytest
import helpers


@pytest.fixture
def deliver():
    deliver = helpers.register_new_courier_and_return_login_password()
    yield deliver
    helpers.delete_deliver(deliver[3])
