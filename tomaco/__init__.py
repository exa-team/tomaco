from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import views

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    views.init_app(app)

    return app
