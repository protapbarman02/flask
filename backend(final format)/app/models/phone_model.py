from app.db import db

class PhoneModel(db.Model):
    # initialize database table name
    __tablename__ = "phones"

    # table column/fiels
    id = db.Column(db.Integer, primary_key=True)
    modelname = db.Column(db.String(100),nullable=False)
    brand = db.Column(db.String(100),nullable=False)
    price = db.Column(db.Float, nullable=False)
    about = db.Column(db.String(500),nullable=True)
    is_smart_phone = db.Column(db.Boolean(),default=True)
    status = db.Column(db.Integer, server_default='1', nullable=False)

    # one to many relationship 
    # child 
    # foreign key
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
