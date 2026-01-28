#!/bin/bash

# SecuritySurface API - Get Subdomains Demo
# Demonstrates how to use the API to get subdomains information for a domain

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
DOMAIN="example.com"
PAGE="1"

curl -i -X GET "https://api.securitysurface.com/v1/search/subdomains?domain=${DOMAIN}&page=${PAGE}" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
