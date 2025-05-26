#!/bin/bash

NAMESPACE=${1:-default}
APP_LABEL="calorie-api"
CPU_THRESHOLD=50   
MEM_THRESHOLD=100  


POD_NAME=$(kubectl get pods -n "$NAMESPACE" --no-headers | awk "/$APP_LABEL/ {print \$1}" | head -n 1)

if [ -z "$POD_NAME" ]; then
  echo "No pod found with name containing '$APP_LABEL' in namespace '$NAMESPACE'"
  exit 1
fi

echo "Monitoring pod: $POD_NAME"


METRICS=$(kubectl top pod "$POD_NAME" -n "$NAMESPACE" --no-headers 2>/dev/null)

if [ -z "$METRICS" ]; then
  echo "Could not retrieve metrics for pod $POD_NAME"
  exit 1
fi

echo "RAW METRICS: $METRICS"

y
CPU=$(echo "$METRICS" | awk '{print $2}' | sed 's/m//')
MEM=$(echo "$METRICS" | awk '{print $3}' | sed 's/Mi//')

echo "CPU: ${CPU}m"
echo "MEM: ${MEM}Mi"


if [ "$CPU" -gt "$CPU_THRESHOLD" ]; then
  echo "CPU usage is high: ${CPU}m"
fi

if [ "$MEM" -gt "$MEM_THRESHOLD" ]; then
  echo "Memory usage is high: ${MEM}Mi"
fi
