import pytest

from tomaco.auth.models import User
from tomaco.tests import BaseTest

from ..models import Interval


class TestInterval(BaseTest):
    url_name = "interval"
    payload = {"type": Interval.POMODORO_TYPE}

    @pytest.fixture
    def interval_create_mock(self, mocker, user):
        interval_instance = Interval(id=1, user=user, type=Interval.POMODORO_TYPE)
        return mocker.patch.object(Interval, "create", return_value=interval_instance)

    @pytest.fixture
    def user_get_mock(self, mocker, user):
        return mocker.patch.object(User, "get", return_value=user)

    @pytest.mark.usefixtures("user_get_mock")
    def test_should_store_the_interval_in_the_database_for_the_auth_user(
        self, auth_client, user, db_session_commit_mock, interval_create_mock
    ):
        self.post(auth_client, self.payload)

        interval_create_mock.assert_called_once_with(user, Interval.POMODORO_TYPE)
        db_session_commit_mock.assert_called()

    @pytest.mark.usefixtures("interval_create_mock", "user_get_mock")
    def test_should_return_created(self, auth_client):
        result = self.post(auth_client, self.payload)
        assert result.status_code == 201

    def test_should_forbid_unauthorized_access(self, client):
        result = self.get(client)
        assert result.status_code == 405
