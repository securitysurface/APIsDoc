#!/bin/bash

# SecuritySurface API - Get DNS Reverse Demo
# Demonstrates how to use the API to get reverse DNS lookup information

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
DOMAIN="8.8.8.8"
DNS_TYPE="a"
PAGE="1"

curl -i -X GET "https://api.securitysurface.com/v1/search/dns/reverse?domain=${DOMAIN}&type=${DNS_TYPE}&page=${PAGE}" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
