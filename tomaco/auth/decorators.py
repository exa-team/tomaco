from functools import wraps

from flask import redirect, session, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not bool(session.get("username")):
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function
