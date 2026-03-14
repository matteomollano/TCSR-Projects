import requests, json

lat = input("Enter latitude: ")
lon = input("Enter longitude: ")

url = "https://api.weather.gov/points/" + lat + "," + lon
print(url)

res = requests.get(url)
print(res)

data = res.json()
# print(json.dumps(data, indent=4))

forecast_url = data["properties"]["forecast"]
# print(forecast_url)

forecast_data = requests.get(forecast_url).json()
# print(json.dumps(forecast_data, indent=4))

periods = forecast_data["properties"]["periods"]

for period in periods:
    print(period["name"], period["temperature"], period["temperatureUnit"])
    print(period["detailedForecast"])
    print()