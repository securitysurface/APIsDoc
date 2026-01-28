#!/bin/bash

# SecuritySurface API - Get Scan Scans Demo
# Demonstrates how to use the API to get a list of scan results

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
START_INDEX="0"
LIMIT="100"

curl -i -X GET "https://api.securitysurface.com/v1/scan/scans?c=${START_INDEX}&l=${LIMIT}" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
