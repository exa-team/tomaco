import pytest
from httmock import HTTMock, urlmatch

from ..exceptions import AuthException
from ..utils import authorize_url, get_user_details, request_access_token

ACCESS_TOKEN = "should-be-access-token"
ACCESS_TOKEN_URL = "http://access-token-server"
AUTHORIZATION_SERVER = "http://authorization-server"
CLIENT_ID = "client-id"
CLIENT_SECRET = "client-secret"
CODE = "should-be-informed-by-the-auth-server"
REDIRECT_URI = "http://us-again"
SCOPE = "user-email"
STATE = "should-be-a-random-string"
USER_RESOURCE_URL = "http://user-resource-server"


class TestAuthorizeUrl:
    def test_should_return_a_formatted_authorize_url(self):
        result = authorize_url(
            AUTHORIZATION_SERVER, CLIENT_ID, REDIRECT_URI, SCOPE, STATE
        )
        expected = (
            AUTHORIZATION_SERVER
            + "?client_id="
            + CLIENT_ID
            + "&redirect_uri="
            + REDIRECT_URI
            + "&scope="
            + SCOPE
            + "&state="
            + STATE
        )

        assert result == expected


class TestRequestAccessToken:
    @staticmethod
    @urlmatch(netloc=r"access-token-server")
    def access_token_success(url, request):
        return "access_token={}&token_type=should-be-token-type".format(ACCESS_TOKEN)

    @staticmethod
    @urlmatch(netloc=r"access-token-server")
    def access_token_not_found(url, request):
        return {"status_code": 404, "content": "Not Found"}

    @staticmethod
    @urlmatch(netloc=r"access-token-server")
    def access_token_with_invalid_credentails(url, request):
        return {"status_code": 200, "content": "error=incorrect_client_credentials"}

    @staticmethod
    @urlmatch(netloc=r"access-token-server")
    def access_token_with_invalid_content(url, request):
        return {"status_code": 200, "content": "invalid-querystring"}

    def test_should_return_token_and_token_type_when_success(self):
        with HTTMock(self.access_token_success):
            result = request_access_token(
                ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, CODE, REDIRECT_URI, STATE
            )

        assert result == {
            "access_token": [ACCESS_TOKEN],
            "token_type": ["should-be-token-type"],
        }

    def test_should_raise_an_auth_exception_when_access_token_returns_not_found(self):
        with HTTMock(self.access_token_not_found), pytest.raises(
            AuthException
        ) as excpt:
            request_access_token(
                ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, CODE, REDIRECT_URI, STATE
            )

        assert str(excpt.value) == "Not Found"

    def test_should_raise_an_auth_exception_when_there_is_something_wrong_with_the_credentails(
        self
    ):
        with HTTMock(self.access_token_with_invalid_credentails), pytest.raises(
            AuthException
        ) as excpt:
            request_access_token(
                ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, CODE, REDIRECT_URI, STATE
            )

        assert str(excpt.value) == "incorrect_client_credentials"

    def test_should_raise_an_auth_exception_when_the_parsing_step_fails(self):
        with HTTMock(self.access_token_with_invalid_content), pytest.raises(
            AuthException
        ) as excpt:
            request_access_token(
                ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, CODE, REDIRECT_URI, STATE
            )

        assert str(excpt.value) == "There is not valid access token in the response"


class TestGetUserDetails:
    @staticmethod
    @urlmatch(netloc=r"user-resource-server")
    def user_details_success(url, request):
        return {"status_code": 200, "content": '{"username": "should-be-username"}'}

    @staticmethod
    @urlmatch(netloc=r"user-resource-server")
    def user_details_not_found(url, request):
        return {"status_code": 404, "content": "Not Found"}

    @staticmethod
    @urlmatch(netloc=r"user-resource-server")
    def user_details_with_invalid_response(url, request):
        return {"status_code": 200, "content": "should-be-json"}

    def test_should_return_the_user_details_when_resource_returns_successfully(self):
        with HTTMock(self.user_details_success):
            result = get_user_details(USER_RESOURCE_URL, ACCESS_TOKEN)
        assert result == {"username": "should-be-username"}

    def test_should_raise_an_auth_exception_when_resource_is_not_avaiable(self):
        with HTTMock(self.user_details_not_found), pytest.raises(
            AuthException
        ) as excpt:
            get_user_details(USER_RESOURCE_URL, ACCESS_TOKEN)

        assert str(excpt.value) == "Not Found"

    def test_should_raise_an_auth_exception_when_it_fails_to_parse_the_response(self):
        with HTTMock(self.user_details_with_invalid_response), pytest.raises(
            AuthException
        ) as excpt:
            get_user_details(USER_RESOURCE_URL, ACCESS_TOKEN)

        assert str(excpt.value) == "There is a problem while parsing the response"
