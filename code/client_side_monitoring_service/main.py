import json
import logging
from flask import Flask, request

# This is a simple client-side monitoring service that captures JavaScript errors,
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/log', methods=['POST'])
def log_event():
    try:
        data = request.get_json()
        logging.info("Received log: %s", json.dumps(data))
        return {"status": "success"}, 200
    except Exception as e:
        logging.error("Error processing log: %s", str(e))
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000);
