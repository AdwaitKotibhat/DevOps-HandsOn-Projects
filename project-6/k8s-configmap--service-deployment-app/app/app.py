from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    color = os.getenv("APP_COLOR", "unknown")
    return f"App Color: {color}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
