from app.db import db 

class CarModel(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Integer, server_default='1',nullable=False)