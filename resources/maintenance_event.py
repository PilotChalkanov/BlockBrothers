
from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.maintenance_event import MaintanaceEventManager
from models.enum import RoleType
from schemas.request.maintenace_event import MaintenanceEventRequestSchema
from schemas.response.maintenance_event import MaintenanceEventResponseSchema
from utils.decorators import validate_schema, permission_required


class CreateMaintenanceEvent(Resource):

    @auth.login_required
    @permission_required(RoleType.home_owner)
    @validate_schema(MaintenanceEventRequestSchema)
    def post(self):
        current_homeowner = auth.current_user()
        complaint = MaintanaceEventManager.create(request.get_json(),current_homeowner.id)
        schema = MaintenanceEventResponseSchema()
        return schema.dump(complaint)

class MaintenanceEventDetail(Resource):

    def get(self, id_):
        pass
    @auth.login_required
    @permission_required(RoleType.home_owner)
    @validate_schema(MaintenanceEventRequestSchema)
    def put(self,id_):
        updated_maint_event = MaintanaceEventManager.update(request.get_json(),id_)
        schema = MaintenanceEventResponseSchema()
        return schema.dump(updated_maint_event)

class ListAllMaintenanceEvents(Resource):
    def get(self):
        #TODO add logic for different roles
        maint_events = MaintanaceEventManager.get_all()
        schema = MaintenanceEventResponseSchema()
        return schema.dump(maint_events, many=True)




