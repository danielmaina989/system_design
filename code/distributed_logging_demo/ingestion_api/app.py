from flask import Flask, request, jsonify
import json
import queue

app = Flask(__name__)
log_queue = queue.Queue()  # This simulates a message broker like Kafka

@app.route("/logs", methods=["POST"])
def ingest_log():
    log_data = request.get_json()
    if not log_data:
        return jsonify({"error": "Invalid log format"}), 400

    log_queue.put(log_data)
    return jsonify({"status": "Log received"}), 200

def get_log_queue():
    return log_queue

if __name__ == "__main__":
    app.run(debug=True, port=5000)
