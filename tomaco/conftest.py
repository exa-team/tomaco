import pytest

from tomaco import create_app, db as app_db

BASE_URL = "http://localhost"
INDEX_URL = "{}/".format(BASE_URL)
LOGIN_URL = "{}/login".format(BASE_URL)
USER_EMAIL = "should-be-user-email"


@pytest.fixture
def app():
    return create_app("tomaco.settings.Testing")


@pytest.fixture
def db(app):
    with app.app_context():
        app_db.create_all()
        yield app_db
        app_db.session.remove()
        app_db.drop_all()


@pytest.fixture
def auth_client(client):
    with client.session_transaction() as sess:
        sess["username"] = USER_EMAIL

    yield client

    sess.pop("username")
