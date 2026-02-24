from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    cities = [
        {"name": "Cork", "temp": "10°C", "desc": "light drizzle"},
        {"name": "Dublin", "temp": "8°C", "desc": "clear sky"},
        {"name": "London", "temp": "11°C", "desc": "broken clouds"},
        {"name": "Paris", "temp": "14°C", "desc": "broken clouds"},
    ]
    return render_template("index.html", cities=cities)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)