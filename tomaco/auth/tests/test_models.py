import pytest

from tomaco.db import DoesNotExist

from ..models import User

USER_EMAIL = "legolas@middleearth.com"


@pytest.mark.usefixtures("db")
class TestUser:
    def test_should_have_a_string_representation(self):
        user = User(email=USER_EMAIL)
        user.id = 1

        assert str(user) == "<id 1>"

    def test_should_persist_user_in_the_database(self):
        user = User(email=USER_EMAIL)
        user.save()

        assert User.query.count() == 1


@pytest.mark.usefixtures("db")
class TestUserGetOrCreate:
    def test_should_create_a_new_user_in_the_database(self):
        user = User.get_or_create(USER_EMAIL)

        assert type(user) == User
        assert User.query.count() == 1

    def test_should_get_the_user_from_database_when_it_exists(self, user):
        result = User.get_or_create(user.email)

        assert user.id == result.id
        assert User.query.count() == 1


@pytest.mark.usefixtures("db")
class TestUserGet:
    def test_should_return_an_user_instance_from_the_database(self, user):
        result = User.get(user.email)

        assert result.email == user.email
        assert user == result

    def test_should_raise_does_not_exist_when_user_is_not_found(self):
        with pytest.raises(DoesNotExist):
            User.get(USER_EMAIL)
