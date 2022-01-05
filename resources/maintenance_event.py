import json

from flask import request
from flask_restful import Resource
from managers.auth import auth
from managers.maintenance_event import MaintanaceEventManager
from models.enum import RoleType
from schemas.request.maintenace_event import MaintenanceEventRequestSchema
from schemas.response.maintenance_event import MaintenanceEventCreateResponseSchema
from utils.decorators import validate_schema, permission_required


class MaintenanceEvent(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        # TODO add logic for different roles
        maint_events = MaintanaceEventManager.get_all(user)
        schema = MaintenanceEventCreateResponseSchema()
        return schema.dump(maint_events, many=True)

    @auth.login_required
    @permission_required(RoleType.home_owner)
    @validate_schema(MaintenanceEventRequestSchema)
    def post(self):
        current_homeowner = auth.current_user()
        maint_event = MaintanaceEventManager.create(
            request.get_json(), current_homeowner.id
        )
        schema = MaintenanceEventCreateResponseSchema()
        return schema.dump(maint_event), 201


class MaintenanceEventDetails(Resource):
    @auth.login_required
    @permission_required(RoleType.home_owner)
    @validate_schema(MaintenanceEventRequestSchema)
    def put(self, id_):
        updated_maint_event = MaintanaceEventManager.update_event(
            request.get_json(), id_
        )
        schema = MaintenanceEventCreateResponseSchema()
        return schema.dump(updated_maint_event)

    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, id_):
        MaintanaceEventManager.delete_event(id_)
        return {"message": "deleted successfully"}, 204


class CloseMaintenanceEvent(Resource):
    @auth.login_required
    @permission_required(RoleType.home_owner_manager)
    def put(self, id_):
        updated_maint_event = MaintanaceEventManager.close(id_)

        return {"status": updated_maint_event.status}


class RaiseMaintenanceEvent(Resource):
    pass
