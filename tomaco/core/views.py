from flask import render_template, session

from tomaco.auth.decorators import login_required


@login_required
def index():
    username = session.get("username")
    return render_template("index.html", username=username)


def init_app(app):
    app.add_url_rule("/", "index", index)
