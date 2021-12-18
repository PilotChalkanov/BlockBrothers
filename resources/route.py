from resources.admin import CreateAdmin, LoginAdmin, LoginHomeOwnerManager
from resources.auth import Register, Login, LoginHomeOwner
from resources.admin import CreateHomeOwner, CreateHomeOwnerManager
from resources.maintenance_event import MaintenanceEvent, MaintenanceEventDetails, CloseMaintenanceEvent

routes = (
    (Register, "/register" ),
    (Login, "/login"),
    (LoginHomeOwner, "/home_owner/login"),
    (LoginHomeOwnerManager, "/home_owner_manager/login"),
    (MaintenanceEvent, "/home_owners/maint_event"),
    (MaintenanceEventDetails, "/home_owners/maint_event/<int:id_>"),
    (CloseMaintenanceEvent,"/home_owner_manager/maint_event/<int:id_>/close"),
    # (ListAllMaintenanceEvents, "/home_owners/maint_events"),
    (CreateHomeOwner, "/admin/create_home_owner"),
    (CreateHomeOwnerManager, "/admin/create_home_owner_manager"),
    (CreateAdmin, "/аdmin/create_admin"),
    (LoginAdmin, "/admin/login")
    # (RegisterSportsCenter,"/")
)