from geopy.geocoders import Nominatim
import requests
from datetime import datetime

def get_weather_data(city):
    # get latitude and longitude using geopy
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.geocode(city)
    
    if location is None:
        data = []
        error = f"No location found for: {city}"
        return data, error

    print(location.address)
    lat, long = location.latitude, location.longitude

    # retrieve weekly weather forecast via weather.gov API
    try:
        response = requests.get(f"https://api.weather.gov/points/{lat},{long}")
        response.raise_for_status()
        point_data = response.json()
        forecast_url = point_data["properties"]["forecast"]
        
        forecast_response = requests.get(forecast_url)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()["properties"]["periods"]
    except Exception as e:
        print(f"Response error: {e}")
        return [], "We couldn't get the weather for this city"
    
    return forecast_data, ""
    
    # cleaned_data = []
    # for period in forecast_data:
    #     date = datetime.fromisoformat(period["startTime"]).strftime("%m/%d/%Y")
    #     start_time = datetime.fromisoformat(period["startTime"]).strftime("%-I:%M %p")
    #     end_time = datetime.fromisoformat(period["endTime"]).strftime("%-I:%M %p")

    #     cleaned_data.append({
    #         "day": period["name"],
    #         "date": date,
    #         "start_time": start_time,
    #         "end_time": end_time,
    #         "time_zone": "EST",
    #         "temp": period["temperature"],
    #         "temp_unit": period["temperatureUnit"],
    #         "wind_speed": period["windSpeed"],
    #         "wind_direction": period["windDirection"],
    #         "description": period["detailedForecast"],
    #         "precipitation": period["probabilityOfPrecipitation"]["value"],
    #         "icon": period["icon"]
    #     })

    # return cleaned_data, ""
