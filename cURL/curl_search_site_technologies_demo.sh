#!/bin/bash

# SecuritySurface API - Get Site Technologies Demo
# Demonstrates how to use the API to get technologies information for a domain

API_KEY="HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
DOMAIN="example.com"

curl -i -X GET "https://api.securitysurface.com/v1/search/site/technologies?domain=${DOMAIN}" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
