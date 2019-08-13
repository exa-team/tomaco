from tomaco.db import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "<id {}>".format(self.id)

    def save(self):
        db.session.add(self)

    @staticmethod
    def get_or_create(email):
        user_instance = User.query.filter_by(email=email).first()
        if user_instance:
            return user_instance

        user_instance = User(email=email)
        user_instance.save()

        return user_instance
