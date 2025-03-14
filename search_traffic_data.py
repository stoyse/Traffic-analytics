import tomtom_api_call_traffic
import get_cityname
import call_db
import time

longitude = 49.235
latitude = 6.9969

while True:
    traffic = tomtom_api_call_traffic.get_traffic_data(longitude, latitude)
    print(traffic)
    road_type = traffic["flowSegmentData"].get("frc", "Unknown")
    current_speed = traffic["flowSegmentData"]["currentSpeed"]
    free_flow_speed = traffic["flowSegmentData"]["freeFlowSpeed"]
    traffic_level = traffic["flowSegmentData"]["confidence"]
    
    city = get_cityname.get_city(longitude, latitude)
    call_db.add(city, road_type, current_speed, free_flow_speed, traffic_level, longitude, latitude)
    time.sleep(300)