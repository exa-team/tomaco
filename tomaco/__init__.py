from flask import Flask
from . import views


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    views.init_app(app)

    return app
