from flask import Flask, render_template, jsonify
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from metrics import request_counter, request_latency
import time

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        request_counter.labels(endpoint="/").inc()
        start = time.time()
        response = render_template("index.html")
        request_latency.labels(endpoint="/").observe(time.time() - start)
        return response

    @app.route("/health")
    def health():
        request_counter.labels(endpoint="/health").inc()
        return jsonify({"status": "healthy"}), 200

    @app.route("/metrics")
    def metrics():
        request_counter.labels(endpoint="/metrics").inc()
        return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
