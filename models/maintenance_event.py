from sqlalchemy import func

from db import db
from models.enum import State


class MaintenanceEventModel(db.Model):
    __tablename__ = "maintenance_event"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(db.DateTime, onupdate=func.now())
    status = db.Column(db.Enum(State), default=State.pending, nullable=False)
    home_owner_id = db.Column(db.Integer, db.ForeignKey("home_owner.id"))
    home_owner = db.relationship("HomeOwnerModel")
