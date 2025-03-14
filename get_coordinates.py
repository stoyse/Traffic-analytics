import requests
import json

# 📍 Set city name (Example: Berlin)
city_name = "Saarbrücken"

# 🔗 Overpass API URL (Free & Open)
overpass_url = "http://overpass-api.de/api/interpreter"

# 📝 Overpass Query to Get Roads in the City
query = f"""
[out:json];
area["name"="{city_name}"]->.searchArea;
way["highway"](area.searchArea);
(._;>;);
out body;
"""



# 📩 Send request
response = requests.get(overpass_url, params={"data": query})

# 📜 Parse response
if response.status_code == 200:
    data = response.json()
    
    # Extract coordinates
    road_coordinates = []
    nodes = {node["id"]: (node["lat"], node["lon"]) for node in data["elements"] if node["type"] == "node"}
    
    for element in data["elements"]:
        if element["type"] == "way":
            way_coords = [nodes[node_id] for node_id in element["nodes"] if node_id in nodes]
            road_coordinates.append(way_coords)
    
    print("✅ Total Roads Found:", len(road_coordinates))
    for road in road_coordinates[:5]:  # Print first 5 roads
        print(road)
    for road in road_coordinates:
        print(f'Road: {road}')
        open('coordinates.txt', 'a').write(f'{road}\n')
        with open('coordinates.json', 'w') as f:
            json.dump(road_coordinates, f)
    print("📝 Coordinates saved to 'coordinates.txt'")
    print("📝 Coordinates saved to 'coordinates.json'")
else:
    print("❌ Error:", response.status_code, response.text)