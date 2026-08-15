from flask import Flask, render_template
from geopy.geocoders import Nominatim
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # get latitude and longitude using geopy
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.geocode("Roslyn, New York")
    lat, long = location.latitude, location.longitude
    
    # retrieve weekly weather forecast via weather.gov API
    response = requests.get(f"https://api.weather.gov/points/{lat},{long}").json()
    forecast_url = response["properties"]["forecast"]
    forecast_data = requests.get(forecast_url).json()["properties"]["periods"]
    
    cleaned_data = []
    for period in forecast_data:
        
        date = datetime.fromisoformat(period["startTime"]).strftime("%m/%d/%Y")
        start_time = datetime.fromisoformat(period["startTime"]).strftime("%-I:%M %p")
        end_time = datetime.fromisoformat(period["endTime"]).strftime("%-I:%M %p")
        
        cleaned_data.append({
            "day": period["name"],
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "time_zone": "EST",
            "temp": period["temperature"],
            "temp_unit": period["temperatureUnit"],
            "wind_speed": period["windSpeed"],
            "wind_direction": period["windDirection"],
            "description": period["detailedForecast"],
            "precipitation": period["probabilityOfPrecipitation"]["value"],
            "icon": period["icon"]
        })
        
    return render_template("index.html", data=cleaned_data)


if __name__ == "__main__":
    app.run(debug=True)
