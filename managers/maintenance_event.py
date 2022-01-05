from werkzeug.exceptions import NotFound

from db import db
from managers.auth import auth
from models import HomeOwnerModel, HomeOwnerManagerModel
from models.maintenance_event import MaintenanceEventModel


class MaintanaceEventManager:
    @staticmethod
    def get_all(user):
        if isinstance(user, HomeOwnerModel):
            return MaintenanceEventModel.query.filter_by(home_owner_id=user.id).all()
        elif isinstance(user, HomeOwnerManagerModel):
            return MaintenanceEventModel.query.filter_by(status="pending")
        return MaintenanceEventModel.query.all()

    @staticmethod
    def create(maint_event_data, home_owner_id):
        maint_event_data["home_owner_id"] = home_owner_id
        maint_event = MaintenanceEventModel(**maint_event_data)
        db.session.add(maint_event)
        db.session.flush()
        return maint_event

    @staticmethod
    def update_event(maint_event_data, id_):
        maint_event_q = MaintenanceEventModel.query.filter_by(id=id_)
        maint_event = maint_event_q.first()
        if not maint_event:
            raise NotFound("Maintenance event doesn't exist!")
        user = auth.current_user()

        if not user.id == maint_event.home_owner_id:
            raise NotFound("Maintenance event doesn't exist!")

        maint_event_q.update(maint_event_data)
        db.session.add(maint_event)
        db.session.flush()
        return maint_event

    @staticmethod
    def close(id_):
        maint_event = MaintanaceEventManager.find_by_id(id_)
        # TODO -> create payment to vendors Account
        maint_event.status = "closed"
        db.session.add(maint_event)
        db.session.flush()
        return maint_event

    @staticmethod
    def raise_event(id_):

        maint_event = MaintanaceEventManager.find_by_id(id_)

        # TODO - To sent emails to vendors

    @staticmethod
    def delete_event(id_):

        maint_event = MaintanaceEventManager.find_by_id(id_)
        db.session.delete(maint_event)
        db.session.flush()

    @staticmethod
    def find_by_id(id_):
        maint_event_q = MaintenanceEventModel.query.filter_by(id=id_)
        maint_event = maint_event_q.first()
        if not maint_event:
            raise NotFound("Maintenance event doesn't exist!")
        return maint_event
