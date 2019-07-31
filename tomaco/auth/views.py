import uuid

from flask import (
    abort,
    current_app,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from .exceptions import AuthException
from .utils import authorize_url, get_user_details, request_access_token


def login():
    if bool(session.get("username")):
        return redirect(url_for("index"))

    return render_template("login.html")


def login_start():
    state = uuid.uuid4()
    session["auth_state"] = state

    return redirect(
        authorize_url(
            current_app.config["GITHUB_AUTHORIZE_URL"],
            current_app.config["GITHUB_CLIENT_ID"],
            current_app.config["GITHUB_CALLBACK_URI"],
            current_app.config["GITHUB_SCOPE"],
            state,
        )
    )


def login_complete():
    state = session.get("auth_state")

    try:
        payload = request_access_token(
            current_app.config["GITHUB_ACCESS_TOKEN_URL"],
            current_app.config["GITHUB_CLIENT_ID"],
            current_app.config["GITHUB_CLIENT_SECRET"],
            request.args.get("code"),
            current_app.config["GITHUB_CALLBACK_URI"],
            state,
        )
        user_details = get_user_details(
            current_app.config["GITHUB_USER_RESOURCE_URL"], payload["access_token"][0]
        )
    except AuthException:
        abort(401)

    session["username"] = user_details["email"]

    return redirect(url_for("index"))


def logout():
    if "username" in session:
        session.pop("username")

    return redirect(url_for("index"))


def init_app(app):
    app.add_url_rule("/login", "login", login)
    app.add_url_rule("/login/start", "login_start", login_start)
    app.add_url_rule("/login/complete", "login_complete", login_complete)
    app.add_url_rule("/logout", "logout", logout)
