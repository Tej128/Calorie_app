import requests
import json
import sys

PROMETHEUS_URL = "http://localhost:9090"
NAMESPACE = "default"
APP_LABEL = "calorie-api"

def query_prometheus(promql):
    try:
        response = requests.get(
            f"{PROMETHEUS_URL}/api/v1/query",
            params={"query": promql}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error querying Prometheus: {e}")
        sys.exit(1)

def print_json_result(result):
    if result["status"] != "success":
        print("Prometheus query failed.")
        return
    print(json.dumps(result["data"], indent=2))

# Query 1: CPU Usage (resource-level)
cpu_query = f'rate(container_cpu_usage_seconds_total{{namespace="{NAMESPACE}", pod=~"{APP_LABEL}.*"}}[1m])'
cpu_result = query_prometheus(cpu_query)
print("\n CPU Usage (rate over 1m):")
print_json_result(cpu_result)

# Query 2: HTTP Request Count (from flask exporter)
http_query = f'flask_http_request_total{{instance=~"{APP_LABEL}.*"}}'
http_result = query_prometheus(http_query)
print("\n Flask HTTP Request Total:")
print_json_result(http_result)
