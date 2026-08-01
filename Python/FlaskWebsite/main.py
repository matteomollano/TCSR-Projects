from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        name = name.title()
    return render_template('hello.html', person=name)

@app.route('/pokemon/')
@app.route('/pokemon/<id>')
def pokemon(id=1):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url)

    if response.status_code == 404:
        image_url = "https://i.pinimg.com/originals/c7/d7/02/c7d70249300e5473a14ded83c694d242.png"
        return render_template("pokemon.html", name=None, image_url=image_url)

    data = response.json()
    name = data["forms"][0]["name"]
    image_url = data["sprites"]["front_default"]

    return render_template("pokemon.html", name=name, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
