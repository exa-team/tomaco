from tomaco.db import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "<id {}>".format(self.id)
