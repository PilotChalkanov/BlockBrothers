from resources.admin import CreateHomeOwner
from resources.auth import Register, Login
from resources.admin import CreateHomeOwner, CreateHomeOwnerManager
from resources.maintenance_event import CreateMaintenanceEvent, MaintenanceEventDetail, ListAllMaintenanceEvents

routes = (
    (Register, "/register" ),
    (Login, "/login"),
    (CreateMaintenanceEvent, "/home_owners/maint_event"),
    (MaintenanceEventDetail, "/home_owners/maint_event/<int: id_>"),
    (ListAllMaintenanceEvents, "/home_owners/maint_events"),
    (CreateHomeOwner, "/admin/create_home_owner"),
    # (CreateHomeOwnerManager), "/admin/create_home_owner_manager"
    # (CreateAdmin), "dmin/create_admin",
    # (RegisterSportsCenter,"/")
)