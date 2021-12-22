from db import db


class VendorModel(db.Model):
    __tablename__ = "vendors"

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(13), nullable=False)
