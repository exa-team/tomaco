from flask_sqlalchemy import SQLAlchemy


class DoesNotExist(Exception):
    pass


db = SQLAlchemy()
