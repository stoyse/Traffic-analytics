import requests
from dotenv import load_dotenv
import os
load_dotenv()


API_KEY = os.getenv("TOMTOM_API_KEY")

def get_traffic_data(latitude, longitude):
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json?key={API_KEY}&point={latitude},{longitude}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    

