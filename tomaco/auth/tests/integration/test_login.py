import pytest

from ...models import User


@pytest.mark.integration
class TestLogin:
    def teardown_method(self, method):
        User.query.delete()
        User.query.session.commit()

    def test_should_access_login_page_when_not_logged_in(self, it_client):
        result = it_client.get("http://0.0.0.0:8080/login")
        assert result.status_code == 200

    def test_should_create_user_after_login(self, it_client):
        it_client.get("http://0.0.0.0:8080/login/start")
        assert User.query.filter_by(username="gandalf").count() == 1
