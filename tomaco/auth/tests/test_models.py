from ..models import User


class TestUser:
    USER_EMAIL = "gandalf@thegrey.com"

    def test_should_have_a_string_representation(self):
        user = User(self.USER_EMAIL)
        user.id = 1

        assert str(user) == "<id 1>"
