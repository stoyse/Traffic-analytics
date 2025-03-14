import requests

from dotenv import load_dotenv
import os
load_dotenv()


API_KEY = os.getenv("TOMTOM_API_KEY")

latitude = 6.9969
longitude = 49.235


url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json?key={API_KEY}&point={latitude},{longitude}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("🛣️ Road Name:", data["flowSegmentData"].get("frc", "Unknown"))
    print("🚗 Current Speed:", data["flowSegmentData"]["currentSpeed"], "km/h")
    print("🏎️ Free Flow Speed:", data["flowSegmentData"]["freeFlowSpeed"], "km/h")
    print("⛔ Traffic Level:", data["flowSegmentData"]["confidence"], "%")


else:
    print("❌ Error:", response.status_code, response.text)