import pytest

from tomaco import create_app
from tomaco import db as app_db
from tomaco.auth.models import User

BASE_URL = "http://localhost"
INDEX_URL = "{}/".format(BASE_URL)
LOGIN_URL = "{}/login".format(BASE_URL)


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
def user(db):
    user = User(username="bbaggins", email="bilbo@baggins.middleearth")
    user.save()

    return user


@pytest.fixture
def auth_client(client, user):
    with client.session_transaction() as sess:
        sess["username"] = user.email

    yield client

    if "username" in sess:
        sess.pop("username")


@pytest.fixture
def db_session_commit_mock(mocker, db):
    return mocker.patch.object(db.session, "commit")
