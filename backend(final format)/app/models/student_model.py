from app.db import db

class StudentModel(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    program = db.Column(db.String(150), nullable=False)
    status = db.Column(db.Integer, server_default='1', nullable=False)

    # one to many relationship 
    # parent 
    phones = db.relationship('PhoneModel',backref='student')