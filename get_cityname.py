from geopy.geocoders import Nominatim

# Initialize geolocator
geolocator = Nominatim(user_agent="traffic_app")

def get_city(latitude, longitude):
    # Get the location info
    location = geolocator.reverse((latitude, longitude), language='en')

    # Extract the city from the address
    if location:
        address = location.address
        # You can parse the address to extract the city if needed
        address_parts = address.split(", ")
        city = address_parts[-4] if len(address_parts) > 3 else "City not found"
        return city
    else:
        return "Location not found"

