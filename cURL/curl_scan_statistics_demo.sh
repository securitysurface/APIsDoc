#!/bin/bash

# SecuritySurface API - Get Scan Statistics Demo
# Demonstrates how to use the API to get detailed statistics for a specific scan

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
SCAN_ID="1207526e-931f-4971-98f8-e08f167cdd66"

curl -i -X GET "https://api.securitysurface.com/v1/scan/statistics?scan_id=${SCAN_ID}" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
