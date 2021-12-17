from resources.admin import CreateHomeOwner, CreateAdmin, LoginAdmin
from resources.auth import Register, Login, LoginHomeOwner
from resources.admin import CreateHomeOwner, CreateHomeOwnerManager
from resources.maintenance_event import MaintenanceEvent, ListAllMaintenanceEvents, \
    MaintenanceEventDetails

routes = (
    (Register, "/register" ),
    (Login, "/login"),
    (LoginHomeOwner, "/loginhome_owner/login"),
    (MaintenanceEvent, "/home_owners/maint_event"),
    (MaintenanceEventDetails, "/home_owners/maint_event/<int:id_>"),
    # (ListAllMaintenanceEvents, "/home_owners/maint_events"),
    (CreateHomeOwner, "/admin/create_home_owner"),
    # (CreateHomeOwnerManager), "/admin/create_home_owner_manager"
    (CreateAdmin, "/аdmin/create_admin"),
    (LoginAdmin, "/admin/login")
    # (RegisterSportsCenter,"/")
)