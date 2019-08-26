import pytest

from ..models import Interval


class TestInterval:
    def test_should_have_a_string_representation(self, user):
        interval = Interval(user=user, type=Interval.POMODORO_TYPE)
        interval.id = 1

        assert str(interval) == "<id 1, type pomodoro>"

    @pytest.mark.usefixtures("db")
    def test_should_persist_interval_in_the_database(self, user):
        interval = Interval(user=user, type=Interval.POMODORO_TYPE)
        interval.save()

        assert Interval.query.count() == 1

    def test_should_automatically_fill_the_finished_at_field(self, db, user):
        interval = Interval(user=user, type=Interval.POMODORO_TYPE)
        interval.save()
        db.session.commit()

        assert bool(interval.finished_at)

    def test_should_create_an_interval_in_the_database(self, db, user):
        interval = Interval.create(user, Interval.POMODORO_TYPE)
        db.session.commit()

        assert bool(interval.id)
