#!/bin/bash

# SecuritySurface API - Get Scan Site Structure Demo
# Demonstrates how to use the API to get the structure of a website

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
SCAN_ID="1207526e-931f-4971-98f8-e08f167cdd66"
DIRECTORY_ID="0"

curl -i -X GET "https://api.securitysurface.com/v1/scan/sitestructure?scan_id=${SCAN_ID}&id=${DIRECTORY_ID}" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
