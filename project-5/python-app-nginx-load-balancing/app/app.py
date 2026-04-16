from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    service = os.getenv("SERVICE_NAME", "unknown")
    return f"Served by: {service}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
