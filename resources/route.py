from resources.auth import Register, Login
from resources.maintenance_event import CreateMaintenanceEvent, MaintenanceEventDetail, ListAllMaintenanceEvents

routes = (
    (Register, "/register" ),
    (Login, "/login"),
    (CreateMaintenanceEvent, "/home_owners/maint_event"),
    (MaintenanceEventDetail, "/home_owners/maint_event/<int: id_>"),
    (ListAllMaintenanceEvents, "/home_owners/maint_events")
    # (RegisterCar,"/"),
    # (RegisterSportsCenter,"/")
)