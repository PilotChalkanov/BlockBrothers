from db import db


class CarModel(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer,primary_key=True)
    registration_plate = db.Column(db.String(10),nullable=False,unique=True)
    brand = db.Column(db.String(50),nullable=False)
    model = db.Column(db.String(50),nullable=False)
    home_owner_id = db.Column(db.Integer,db.ForeignKey("home_owner.id"))
    home_owner = db.relationship("HomeOwnerModel")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = db.relationship("UserModel")
    home_owner_manager_id = db.Column(db.Integer, db.ForeignKey("home_owner_manager.id"))
    home_owner_manager = db.relationship("HomeOwnerManagerModel")

