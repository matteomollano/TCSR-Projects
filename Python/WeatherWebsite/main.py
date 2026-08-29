from flask import Flask, render_template, request
from get_weather import get_weather_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_weather", methods=["GET"])
def get_weather():
    city = request.args["city"].strip()
    data, error = get_weather_data(city)
    
    return render_template("index.html", data=data, city=city, error=error)


if __name__ == "__main__":
    app.run(debug=True)
