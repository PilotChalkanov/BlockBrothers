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
    @permission_required(RoleType.home_owner)
    @validate_schema(MaintenanceEventRequestSchema)
    def post(self):
        current_homeowner = auth.current_user()
        maint_event = MaintanaceEventManager.create(request.get_json(),current_homeowner.id)
        schema = MaintenanceEventCreateResponseSchema()
        return schema.dump(maint_event)


class MaintenanceEventDetails(Resource):
    def get(self):
        pass

    @auth.login_required
    @permission_required(RoleType.home_owner)
    @validate_schema(MaintenanceEventRequestSchema)
    def put(self, id_):
        updated_maint_event = MaintanaceEventManager.update(request.get_json(), id_)
        schema = MaintenanceEventCreateResponseSchema()
        return schema.dump(updated_maint_event)

    def delete(self):
        pass

class MaintenanceEventDetail(Resource):

    def get(self, id_):
        pass


class ListAllMaintenanceEvents(Resource):
    def get(self):
        #TODO add logic for different roles
        maint_events = MaintanaceEventManager.get_all()
        schema = MaintenanceEventResponseSchema()
        return schema.dump(maint_events, many=True)




