import uuid
from unittest.mock import patch

from tomaco.conftest import INDEX_URL, USER_EMAIL
from tomaco.tests import BaseTest

from ..exceptions import AuthException
from .. import views

ACCESS_TOKEN_PAYLOAD = {"access_token": ["should-be-access-token"]}
USER_DETAILS_PAYLOAD = {"email": USER_EMAIL}


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

    @patch.object(uuid, "uuid4", return_value="should-be-uuid")
    def test_should_redirect_to_oauth_authorize_url(self, _uuidMock, client):
        expected_url = "https://github.com/login/oauth/authorize?client_id=should-be-client-id&redirect_uri=http://localhost:8080/login/complete&scope=email&state=should-be-uuid"  # noqa
        result = self.get(client)

        assert result.status_code == 302
        assert result.location == expected_url


class TestLoginComplete(BaseTest):
    url_name = "login_complete"

    @patch.object(views, "request_access_token", return_value=ACCESS_TOKEN_PAYLOAD)
    @patch.object(views, "get_user_details", return_value=USER_DETAILS_PAYLOAD)
    def test_should_redirect_to_home(
        self, _requestAccessTokenMock, _getUserDetailsMock, client
    ):
        result = self.get(client)

        assert result.status_code == 302
        assert result.location == INDEX_URL

    @patch.object(views, "request_access_token", return_value=ACCESS_TOKEN_PAYLOAD)
    @patch.object(views, "get_user_details", return_value=USER_DETAILS_PAYLOAD)
    def test_should_create_user_session(
        self, _requestAccessTokenMock, _getUserDetailsMock, client
    ):
        self.get(client)

        with client.session_transaction() as sess:
            assert sess["username"] == USER_EMAIL

    @patch.object(
        views,
        "request_access_token",
        side_effect=AuthException("some sort of auth error"),
    )
    def test_should_show_a_unauthorized_when_authorization_fails(
        self, _requestAccessTokenMock, client
    ):
        result = self.get(client)

        assert result.status_code == 401
        assert b"Unauthorized" in result.data


class TestLogout(BaseTest):
    url_name = "logout"

    def test_should_redirect_to_index(self, client):
        result = self.get(client)

        assert result.status_code == 302
        assert result.location == INDEX_URL

    def test_should_destroy_user_session(self, client):
        with client.session_transaction() as sess:
            sess["username"] = USER_EMAIL
        self.get(client)

        with client.session_transaction() as sess:
            assert "username" not in sess
