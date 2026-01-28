#!/bin/bash

# SecuritySurface API - Get Scan Vulnerabilities Demo
# Demonstrates how to use the API to get a list of vulnerabilities from scans

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
SCAN_ID="1207526e-931f-4971-98f8-e08f167cdd66"
START_POSITION="0"
LIMIT="100"

curl -i -X GET "https://api.securitysurface.com/v1/scan/vulnerabilities?scan_id=${SCAN_ID}&c=${START_POSITION}&l=${LIMIT}" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
