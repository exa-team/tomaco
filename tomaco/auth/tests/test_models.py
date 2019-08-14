import pytest
from ..models import User


@pytest.mark.usefixtures("db")
class TestUser:
    USER_EMAIL = "gandalf@thegrey.com"

    def test_should_have_a_string_representation(self):
        user = User(email=self.USER_EMAIL)
        user.id = 1

        assert str(user) == "<id 1>"

    def test_should_persist_user_in_the_database(self):
        user = User(email=self.USER_EMAIL)
        user.save()

        assert User.query.count() == 1

    def test_should_create_a_new_user_in_the_database(self):
        user = User.get_or_create(self.USER_EMAIL)

        assert type(user) == User
        assert User.query.count() == 1

    def test_should_get_the_user_from_database_when_it_exists(self):
        user = User(email=self.USER_EMAIL)
        user.save()

        result = User.get_or_create(self.USER_EMAIL)

        assert user == result
        assert User.query.count() == 1
