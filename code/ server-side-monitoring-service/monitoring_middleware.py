import time
import logging
from flask import request

logger = logging.getLogger("monitoring")
logging.basicConfig(filename="monitoring.log", level=logging.INFO)

def monitor_requests(app):
    @app.before_request
    def before():
        request.start_time = time.time()

    @app.after_request
    def after(response):
        duration = time.time() - request.start_time
        logger.info(f"{request.method} {request.path} {response.status_code} {duration:.4f}s")
        return response

    @app.errorhandler(Exception)
    def error_handler(e):
        logger.exception(f"Exception in {request.path}: {str(e)}")
        return {"error": "Internal Server Error"}, 500
