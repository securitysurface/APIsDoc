# SecuritySurface API - Get Site Technologies Demo
# Demonstrates how to use the API to get technologies information for a domain

$API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
$DOMAIN = "example.com"

$headers = @{
    "apikey" = $API_KEY
    "Content-Type" = "application/json"
}

$uri = "https://api.securitysurface.com/v1/search/site/technologies?domain=$DOMAIN"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers
    $response | ConvertTo-Json -Depth 10
} catch {
    Write-Host "Error: $_"
    $_.Exception.Response | ConvertTo-Json
}
