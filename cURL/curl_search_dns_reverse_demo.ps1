# SecuritySurface API - Get DNS Reverse Demo
# Demonstrates how to use the API to get reverse DNS lookup information

$API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
$DOMAIN = "8.8.8.8"
$DNS_TYPE = "a"
$PAGE = "1"

$headers = @{
    "apikey" = $API_KEY
    "Content-Type" = "application/json"
}

$uri = "https://api.securitysurface.com/v1/search/dns/reverse?domain=$DOMAIN&type=$DNS_TYPE&page=$PAGE"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers
    $response | ConvertTo-Json -Depth 10
} catch {
    Write-Host "Error: $_"
    $_.Exception.Response | ConvertTo-Json
}
