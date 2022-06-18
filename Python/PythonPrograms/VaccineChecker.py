import json
import time
import requests
from plyer.utils import platform
from plyer import notification


response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=682016&date=26-06-2021")
while True:
    time.sleep(1)
    complete = response.content
    novaccine = """b'{"sessions":[]}'"""
    if novaccine == complete:
        print("No Vaccine")
    else:
        your_json = complete
        parsed = json.loads(your_json)
        print(json.dumps(parsed, indent=4, sort_keys=True))
        notification.notify(title='Vaccine Checker', message='Vaccine is available')