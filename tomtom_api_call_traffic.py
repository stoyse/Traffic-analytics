import requests
from dotenv import load_dotenv
import os
load_dotenv()


API_KEY = os.getenv("TOMTOM_API_KEY")

# 📍 Set coordinates (Example: Berlin)
latitude = 49.235
longitude = 6.9969

# 🔗 TomTom Traffic Flow API URL
url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json?key={API_KEY}&point={latitude},{longitude}"

# 📩 Send request
response = requests.get(url)

# 📜 Parse response
if response.status_code == 200:
    data = response.json()
    print(data)
    print("🛣️ Road Type:", data["flowSegmentData"].get("frc", "Unknown"))
    print("🚗 Current Speed:", data["flowSegmentData"]["currentSpeed"], "km/h")
    print("🏎️ Free Flow Speed:", data["flowSegmentData"]["freeFlowSpeed"], "km/h")
    print("⛔ Traffic Level:", data["flowSegmentData"]["confidence"], "%")
else:
    print("❌ Error:", response.status_code, response.text)