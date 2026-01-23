import requests

latitude = float(input("Enter latitude coordinate: "))
longitude = float(input("Enter longitude coordinate: "))

response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
# print(response.status_code)

data = response.json()
coordinates = data["geometry"]["coordinates"]
forecast_url = data["properties"]["forecast"]
time_zone = data["properties"]["timeZone"]

location_data = data["properties"]["relativeLocation"]["properties"]
city = location_data["city"]
state = location_data["state"]

forecast_response = requests.get(forecast_url)
# print(forecast_response.status_code)

forecast_data = forecast_response.json()
periods = forecast_data["properties"]["periods"]

print("Weather Summary")
print(f"Location: {city}, {state}")
print(f"Coordinates: {coordinates[1]}, {coordinates[0]}")
print(f"Time Zone: {time_zone}")
print("\nHere is your weekly report:")
for period in periods:
    print(period["name"])
    print(f"Temperature: {period["temperature"]}°{period["temperatureUnit"]}")
    print(f"Wind Speed: {period["windSpeed"]}")
    print(f"Wind Direction: {period["windDirection"]}")
    print(f"Detailed Forecast: {period["detailedForecast"]}\n")