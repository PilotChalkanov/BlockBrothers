from resources.admin import CreateHomeOwner, CreateAdmin, LoginAdmin
from resources.auth import Register, Login, LoginHomeOwner
from resources.admin import CreateHomeOwner, CreateHomeOwnerManager
from resources.maintenance_event import CreateMaintenanceEvent, MaintenanceEventDetail, ListAllMaintenanceEvents

routes = (
    (Register, "/register" ),
    (Login, "/login"),
    (LoginHomeOwner, "/loginhome_owner/login"),
    (CreateMaintenanceEvent, "/home_owners/maint_event"),
    # (MaintenanceEventDetail, "/home_owners/maint_event/<int: id_>"),
    (ListAllMaintenanceEvents, "/home_owners/maint_events"),
    (CreateHomeOwner, "/admin/create_home_owner"),
    # (CreateHomeOwnerManager), "/admin/create_home_owner_manager"
    (CreateAdmin, "/аdmin/create_admin"),
    (LoginAdmin, "/admin/login")
    # (RegisterSportsCenter,"/")
)