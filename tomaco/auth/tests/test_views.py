import uuid

import pytest

from tomaco.conftest import INDEX_URL
from tomaco.tests import BaseTest

from .. import views
from ..exceptions import AuthException
from ..models import User


class TestLogin(BaseTest):
    url_name = "login"

    def test_should_access_the_login_page(self, client):
        result = self.get(client)

        assert result.status_code == 200
        assert b"Login" in result.data

    def test_should_redirect_to_home_when_already_logged_in(self, auth_client):
        result = self.get(auth_client)

        assert result.status_code == 302
        assert result.location == INDEX_URL


class TestLoginStart(BaseTest):
    url_name = "login_start"

    def test_should_redirect_to_oauth_authorize_url(self, mocker, client):
        mocker.patch.object(uuid, "uuid4", return_value="should-be-uuid")
        expected_url = "https://github.com/login/oauth/authorize?client_id=should-be-client-id&redirect_uri=http://localhost:8080/login/complete&scope=email&state=should-be-uuid"  # noqa
        result = self.get(client)

        assert result.status_code == 302
        assert result.location == expected_url


class TestLoginComplete(BaseTest):
    url_name = "login_complete"

    @pytest.fixture
    def get_user_details_mock(self, mocker, user):
        data = {"email": user.email, "login": user.username}
        return mocker.patch.object(views, "get_user_details", return_value=data)

    @pytest.fixture
    def request_access_token_mock(self, mocker):
        payload = {"access_token": ["should-be-access-token"]}
        mocker.patch.object(views, "request_access_token", return_value=payload)

    @pytest.fixture
    def user_get_or_create_mock(self, user, mocker):
        return mocker.patch.object(User, "get_or_create", return_value=user)

    @pytest.mark.usefixtures(
        "get_user_details_mock", "request_access_token_mock", "user_get_or_create_mock"
    )
    def test_should_redirect_to_home(self, client, user):
        result = self.get(client)

        assert result.status_code == 302
        assert result.location == INDEX_URL

    @pytest.mark.usefixtures("get_user_details_mock", "request_access_token_mock")
    def test_should_get_or_create_user_from_the_database(
        self, client, user, db_session_commit_mock, user_get_or_create_mock
    ):
        self.get(client)

        user_get_or_create_mock.assert_called_once_with(user.username, email=user.email)
        db_session_commit_mock.assert_called()

    @pytest.mark.usefixtures(
        "get_user_details_mock", "request_access_token_mock", "user_get_or_create_mock"
    )
    def test_should_create_user_session(self, client, user):
        self.get(client)

        with client.session_transaction() as sess:
            assert sess["username"] == user.username

    def test_should_show_a_unauthorized_when_authorization_fails(self, client, mocker):
        mocker.patch.object(
            views,
            "request_access_token",
            side_effect=AuthException("some sort of auth error"),
        )

        result = self.get(client)

        assert result.status_code == 401
        assert b"Unauthorized" in result.data


class TestLogout(BaseTest):
    url_name = "logout"

    def test_should_redirect_to_index(self, client):
        result = self.get(client)

        assert result.status_code == 302
        assert result.location == INDEX_URL

    def test_should_destroy_user_session(self, client, user):
        with client.session_transaction() as sess:
            sess["username"] = user.email
        self.get(client)

        with client.session_transaction() as sess:
            assert "username" not in sess
