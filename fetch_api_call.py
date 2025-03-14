import get_cityname
import tomtom_api_call_traffic

traffic = tomtom_api_call_traffic.get_traffic_data(49.235, 6.9969)
city = get_cityname.get_city(49.235, 6.9969)

print(f'City: {city}')
print("🛣️ Road Type:", traffic["flowSegmentData"].get("frc", "Unknown"))
print("🚗 Current Speed:", traffic["flowSegmentData"]["currentSpeed"], "km/h")
print("🏎️ Free Flow Speed:", traffic["flowSegmentData"]["freeFlowSpeed"], "km/h")
print("⛔ Traffic Level:", traffic["flowSegmentData"]["confidence"], "%")