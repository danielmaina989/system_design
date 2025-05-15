from flask import Flask, jsonify
from monitoring_middleware import monitor_requests

app = Flask(__name__)
monitor_requests(app)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/error")
def error():
    raise ValueError("Something went wrong")

@app.route("/")
def index():
    return jsonify(message="Hello from server")

if __name__ == "__main__":
    app.run(debug=True)
