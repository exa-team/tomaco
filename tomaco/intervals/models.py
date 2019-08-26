from datetime import datetime

from sqlalchemy_utils import ChoiceType

from tomaco.db import db


class Interval(db.Model):
    BREAK_TYPE = "break"
    POMODORO_TYPE = "pomodoro"
    TYPES = ((BREAK_TYPE, "Break"), (POMODORO_TYPE, "Pomodoro"))

    __tablename__ = "interval"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("intervals", lazy=True))
    finished_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    type = db.Column(ChoiceType(TYPES), nullable=False)

    def __repr__(self):
        return "<id {}, type {}>".format(self.id, self.type)

    def save(self):
        db.session.add(self)

    @staticmethod
    def create(user, interval_type):
        interval_instance = Interval(user=user, type=interval_type)
        interval_instance.save()

        return interval_instance
