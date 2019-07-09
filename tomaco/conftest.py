import pytest

from tomaco import create_app

BASE_URL = "http://localhost"
INDEX_URL = "{}/".format(BASE_URL)
LOGIN_URL = "{}/login".format(BASE_URL)
USER_EMAIL = "should-be-user-email"


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def auth_client(client):
    with client.session_transaction() as sess:
        sess["username"] = USER_EMAIL

    yield client

    sess.pop("username")
