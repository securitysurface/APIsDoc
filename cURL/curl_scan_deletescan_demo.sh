#!/bin/bash

# SecuritySurface API - Delete Scan Demo
# Demonstrates how to use the API to delete a specific scan

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
SCAN_ID="1207526e-931f-4971-98f8-e08f167cdd66"

curl -i -X POST "https://api.securitysurface.com/v1/scan/deletescan" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json" \
-d "{\"scan_id\":[\"${SCAN_ID}\"]}"
