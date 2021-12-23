from sqlalchemy import func

from db import db


class SubscriptionModel(db.Model):
    __tablename__ = "subscription"

    id = db.Column(db.Integer, primary_key=True)
    provider_subs_id = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(db.DateTime, onupdate=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    home_owner_id = db.Column(db.Integer, db.ForeignKey("home_owner.id"))
    home_owner_manager = db.Column(db.Integer, db.ForeignKey("home_owner_manager.id"))
