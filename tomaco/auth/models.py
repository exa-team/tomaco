from tomaco.db import db, DoesNotExist


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=True)
    username = db.Column(db.String(), nullable=False, unique=True)

    def __repr__(self):
        return "<id {}>".format(self.id)

    def save(self):
        db.session.add(self)

    @staticmethod
    def get_or_create(username, **kwargs):
        try:
            return User.get(username=username)
        except DoesNotExist:
            pass

        user_instance = User(username=username, **kwargs)
        user_instance.save()

        return user_instance

    @staticmethod
    def get(**kwargs):
        user_instance = User.query.filter_by(**kwargs).first()

        if not user_instance:
            raise DoesNotExist()

        return user_instance
