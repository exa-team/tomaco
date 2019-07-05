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

from . import auth


def index():
    username = session.get("username")
    return render_template("index.html", username=username)


def login():
    state = uuid.uuid4()
    session["auth_state"] = state

    return redirect(
        auth.authorize_url(
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
        payload = auth.request_access_token(
            current_app.config["GITHUB_ACCESS_TOKEN_URL"],
            current_app.config["GITHUB_CLIENT_ID"],
            current_app.config["GITHUB_CLIENT_SECRET"],
            request.args.get("code"),
            current_app.config["GITHUB_CALLBACK_URI"],
            state,
        )
        user_details = auth.get_user_details(
            current_app.config["GITHUB_USER_RESOURCE_URL"], payload["access_token"][0]
        )
    except auth.AuthException:
        abort(401)

    session["username"] = user_details["email"]

    return redirect(url_for("index"))


def logout():
    if "username" in session:
        session.pop("username")

    return redirect(url_for("index"))


def init_app(app):
    app.add_url_rule("/", "index", index)
    app.add_url_rule("/login", "login", login)
    app.add_url_rule("/login/complete", "login_complete", login_complete)
    app.add_url_rule("/logout", "logout", logout)
