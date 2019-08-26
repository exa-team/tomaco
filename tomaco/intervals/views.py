from flask import request, session

from tomaco.auth.decorators import login_required
from tomaco.auth.models import User
from .models import Interval, db


@login_required
def interval():
    username = session.get("username")
    user = User.get(username)
    payload = request.json

    interval = Interval.create(user, payload.get("type", Interval.POMODORO_TYPE))

    db.session.commit()

    return str(interval.id), 201


def init_app(app):
    app.add_url_rule("/interval", "interval", interval, methods=("POST",))
