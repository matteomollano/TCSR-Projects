import requests

lat = input("Enter latitude: ")
long = input("Enter longitude: ")

response = requests.get(f"https://api.weather.gov/points/{lat},{long}")
# print(response.text)

data = response.json()
properties = data["properties"]
forecast_url = properties["forecast"]

city = properties["relativeLocation"]["properties"]["city"]
state = properties["relativeLocation"]["properties"]["state"]

forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()
# print(forecast_response.text)

periods = forecast_data["properties"]["periods"]
# print(periods)

print(f"Weather for {city}, {state}")
for period in periods:
    name = period["name"]
    temp = period["temperature"]
    unit = period["temperatureUnit"]
    wind_speed = period["windSpeed"]
    wind_direction = period["windDirection"]
    details = period["detailedForecast"]
    
    print(f"{name} - {temp} {unit}")
    print(f"{wind_speed} {wind_direction}")
    print(details)
    print()