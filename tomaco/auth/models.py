from tomaco.db import db, DoesNotExist


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return "<id {}>".format(self.id)

    def save(self):
        db.session.add(self)

    @staticmethod
    def get_or_create(email):
        try:
            return User.get(email)
        except DoesNotExist:
            pass

        user_instance = User(email=email)
        user_instance.save()

        return user_instance

    @staticmethod
    def get(email):
        user_instance = User.query.filter_by(email=email).first()

        if not user_instance:
            raise DoesNotExist()

        return user_instance
