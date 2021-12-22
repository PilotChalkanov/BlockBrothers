from sqlalchemy import func

from db import db


class PaymentModel(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.String(10))
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(db.DateTime, onupdate=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    home_owner_id = db.Column(db.Integer, db.ForeignKey("home_owner.id"))
    home_owner_manager = db.Column(db.Integer, db.ForeignKey("home_owner_manager.id"))
