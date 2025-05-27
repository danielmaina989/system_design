import time
import requests

API_ENDPOINT = "http://localhost:5000/logs"

def generate_logs():
    logs = [
        {"level": "INFO", "message": "User logged in."},
        {"level": "ERROR", "message": "Database connection failed."},
        {"level": "DEBUG", "message": "Debugging session started."}
    ]
    while True:
        for log in logs:
            try:
                response = requests.post(API_ENDPOINT, json=log)
                print(f"Sent log: {log}, Status: {response.status_code}")
            except Exception as e:
                print(f"Failed to send log: {e}")
            time.sleep(2)

if __name__ == "__main__":
    generate_logs()
