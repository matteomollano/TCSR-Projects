from geopy.geocoders import Nominatim
import requests
import json

def get_lat_long(location_name):
    geolocator = Nominatim(user_agent="my-app")
    
    location = geolocator.geocode(location_name)
    
    if location:
        return location.latitude, location.longitude
    else:
        return None

# getting coordinates
location = input("Enter location/address: ")
coordinates = get_lat_long(location)
lat, lon = coordinates

# make request
url = f"https://api.weather.gov/points/{lat},{lon}"
print(url)

res = requests.get(url)
data = res.json()
# print(json.dumps(data, indent=4))

forecast_url = data["properties"]["forecast"]
# print(forecast_url)

forecast_data = requests.get(forecast_url).json()
# print(json.dumps(forecast_data, indent=4))

periods = forecast_data["properties"]["periods"]
# print(json.dumps(periods, indent=4))

for period in periods:
    print(f"{period["name"]} {period["temperature"]}°{period["temperatureUnit"]}")
    print(f"Wind speed is {period["windSpeed"]} {period["windDirection"]}")
    print(f"Forecast: {period["detailedForecast"]}\n")