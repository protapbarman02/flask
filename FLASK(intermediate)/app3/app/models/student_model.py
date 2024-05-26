from app.db import db


class StudentModel(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)

    phones = db.relationship("PhoneModel", back_populates="student")
