from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    role = db.Column(db.String(20), nullable=False)
    section = db.Column(db.String(10), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(80), nullable=False)
    lectures = db.relationship("Lecture", backref="teacher", lazy=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "subject": self.subject}

class Lecture(db.Model):
    __tablename__ = "lecture"
    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(10), nullable=False)
    subject = db.Column(db.String(80), nullable=False)
    day = db.Column(db.String(10), nullable=False)
    time_slot = db.Column(db.String(50), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"), nullable=False)
    status = db.Column(db.String(20), default="Scheduled")

    def to_dict(self):
        return {
            "id": self.id,
            "section": self.section,
            "subject": self.subject,
            "day": self.day,
            "time_slot": self.time_slot,
            "teacher": self.teacher.name if self.teacher else None,
            "status": self.status
        }