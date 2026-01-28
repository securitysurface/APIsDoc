#!/bin/bash

# SecuritySurface API - Get Scan Proxy Demo
# Demonstrates how to use the API to get available proxy/tunnel servers

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"

curl -i -X GET "https://api.securitysurface.com/v1/scan/getproxy" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
