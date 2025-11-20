from prometheus_client import Counter, Histogram

# Count total requests per endpoint
request_counter = Counter(
    "app_request_count",
    "Total number of requests per endpoint",
    ["endpoint"]
)

# Measure request latency
request_latency = Histogram(
    "app_request_latency_seconds",
    "Request latency per endpoint",
    ["endpoint"]
)
