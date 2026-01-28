#!/bin/bash

# SecuritySurface API - Get Scan Overview Demo
# Demonstrates how to use the API to get an overview of scan operations

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"

curl -i -X GET "https://api.securitysurface.com/v1/scan/overview" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
