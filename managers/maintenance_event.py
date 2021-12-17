from werkzeug.exceptions import NotFound

from db import db
from managers.auth import auth
from models import UserModel
from models.maintenance_event import MaintenanceEventModel


class MaintanaceEventManager:

    @staticmethod
    def get_all(user):
        if isinstance(user, UserModel):
            return MaintenanceEventModel.query.filter_by(home_owner_id=user.id).all()
        return MaintenanceEventModel.query.all()

    @staticmethod
    def create(maint_event_data, home_owner_id):
        maint_event_data["home_owner_id"] = home_owner_id
        maint_event = MaintenanceEventModel(**maint_event_data)
        db.session.add(maint_event)
        db.session.commit()
        return maint_event

    @staticmethod
    def update(maint_event_data, id_):
        maint_event_q = MaintenanceEventModel.query.filter_by(id=id_)
        maint_event = maint_event_q.first()
        if not maint_event:
            raise NotFound("Maintenance event doesn't exist!")
        user = auth.current_user()

        if not user.id == maint_event.home_owner_id:
            raise NotFound("Maintenance event doesn't exist!")

        maint_event_q.update(maint_event_data)
        return maint_event
