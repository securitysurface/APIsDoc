#!/bin/bash

# SecuritySurface API - Create Scan Demo
# Demonstrates how to use the API to initiate a new scan for a specified address

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
ADDRESS="http://"
COMMENT="this is a example"
SCAN_TYPE="st.fs"
PROXYID="25"
USERAGENT="Default"

curl -i -X POST "https://api.securitysurface.com/v1/scan/createscan" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json" \
-d "{\"address\":\"${ADDRESS}\",\"comment\":\"${COMMENT}\",\"type\":\"${SCAN_TYPE}\",\"proxyid\":\"${PROXYID}\",\"useragent\":\"${USERAGENT}\"}"
