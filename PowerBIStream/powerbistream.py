import requests
from datetime import datetime
import time
import psutil
import json

DEVICE = 'MyPC'

while True:
    now = datetime.strftime(datetime.utcnow(), "%Y-%m-%dT%H:%M:%S%Z")
    json_data = [{
        "computerName": DEVICE,
        "timestamp": now,
        "cpuPercentage": psutil.cpu_percent(),
        "memoryAvailable": psutil.virtual_memory().available,
        "memoryCommitted": psutil.virtual_memory().used
    }]
    res = requests.post('YOUR_POWERBI_API_ENDPOINT', data=json.dumps(json_data))
    print(res.status_code)
    time.sleep(5)
    