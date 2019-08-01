from flask import Flask
from flask_migrate import Migrate

from . import views
from .auth import views as auth_views
from .db import db

migrate = Migrate()


def create_app(app_settings):
    app = Flask(__name__)
    app.config.from_object(app_settings)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    views.init_app(app)
    auth_views.init_app(app)

    return app
