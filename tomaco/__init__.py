from flask import Flask
from flask_migrate import Migrate

from .auth import views as auth_views
from .core import views as core_views
from .db import db
from .intervals import views as interval_views

migrate = Migrate()


def create_app(app_settings):
    app = Flask(__name__)
    app.config.from_object(app_settings)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    auth_views.init_app(app)
    core_views.init_app(app)
    interval_views.init_app(app)

    return app
