from tomaco.conftest import LOGIN_URL, USER_EMAIL

from . import BaseTest

ACCESS_TOKEN_PAYLOAD = {"access_token": ["should-be-access-token"]}
USER_DETAILS_PAYLOAD = {"email": USER_EMAIL}


class TestIndex(BaseTest):
    url_name = "index"

    def test_should_access_the_index_page(self, auth_client):
        result = self.get(auth_client)

        assert result.status_code == 200
        assert b"Tomaco" in result.data

    def test_should_redirect_to_login_page_when_anonymous(self, client):
        result = self.get(client)

        assert result.status_code == 302
        assert result.location == LOGIN_URL

    def test_should_show_a_logout_entry_when_logged_in(self, auth_client):
        result = self.get(auth_client)
        assert b"/logout" in result.data
