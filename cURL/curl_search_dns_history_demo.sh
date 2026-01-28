#!/bin/bash

# SecuritySurface API - Get DNS History Demo
# Demonstrates how to use the API to get DNS history for a domain

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
DOMAIN="example.com"
DNS_TYPE="A"
PAGE="1"

curl -i -X GET "https://api.securitysurface.com/v1/search/dns/history?domain=${DOMAIN}&type=${DNS_TYPE}&page=${PAGE}" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
