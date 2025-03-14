import requests

API_KEY = ""
BASE_URL = "https://api.tomtom.com/routing/1/calculateRoute"

# Define start & end points
start_lat, start_lon = 52.52, 13.405  # Berlin
end_lat, end_lon = 48.8566, 2.3522   # Paris

# Construct API request URL
url = f"{BASE_URL}/{start_lat},{start_lon}:{end_lat},{end_lon}/json?key={API_KEY}"

# Send request
response = requests.get(url)
data = response.json()

# Print route summary
if response.status_code == 200:
    print("Distance (m):", data['routes'][0]['summary']['lengthInMeters'])
    print("Estimated Time (s):", data['routes'][0]['summary']['travelTimeInSeconds'])
else:
    print("Error:", data)