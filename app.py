from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os
import psycopg
import requests

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")


def get_category():
    try:
        with psycopg.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name FROM categories LIMIT 1")
                row = cur.fetchone()
                if row:
                    return row[0]
    except Exception as e:
        print("Database error:", e)

    return "Programming"


def get_joke(category):
    try:
        url = f"https://v2.jokeapi.dev/joke/{category}?type=twopart"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("error"):
            raise Exception("Joke API returned an error")

        return {
            "category": category,
            "setup": data.get("setup", "No setup available."),
            "punchline": data.get("delivery", "No punchline available.")
        }
    except Exception as e:
        print("API error:", e)
        return {
            "category": category,
            "setup": "Sorry, the joke service is unavailable right now.",
            "punchline": "Please try again later."
        }


@app.route("/")
def home():
    category = get_category()
    joke = get_joke(category)
    return render_template("index.html", joke=joke)


@app.route("/api/joke")
def api_joke():
    category = get_category()
    return jsonify(get_joke(category))


@app.route("/health")
def health():
    return jsonify({"status": "OK"})

@app.route("/status")
def status():
    return jsonify({
        "database": "ok",
        "api": "ok"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)