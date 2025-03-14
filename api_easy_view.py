import requests

from dotenv import load_dotenv
import os
import tomtom_api_call_traffic
load_dotenv()

latitude = 6.8994
longitude = 49.2487

traffic = tomtom_api_call_traffic.get_traffic_data(latitude=latitude, longitude=longitude)

print(traffic)


