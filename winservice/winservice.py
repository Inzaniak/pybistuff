# THIS CODE HAS TO BE RUN AS ADMIN
from taskobra import Service

path_to_script = "PATH_TO_YOUR_SCRIPT.py"
service = Service("ServiceExample")
service.create_service(path_to_script)
service.start_service()
print(service.status)

# To remove the service:
service.stop_service()
service.remove_service()