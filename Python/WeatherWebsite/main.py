from flask import Flask, render_template
from geopy.geocoders import Nominatim
import requests

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
    forecast_data = requests.get(forecast_url).json()
    
    return render_template("index.html", name="test")


if __name__ == "__main__":
    app.run(debug=True)
