# SecuritySurface API - Get Scan Site Structure Demo
# Demonstrates how to use the API to get the structure of a website

$API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
$SCAN_ID = "1207526e-931f-4971-98f8-e08f167cdd66"
$DIRECTORY_ID = "0"

$headers = @{
    "apikey" = $API_KEY
    "Content-Type" = "application/json"
}

$uri = "https://api.securitysurface.com/v1/scan/sitestructure?scan_id=$SCAN_ID&id=$DIRECTORY_ID"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers
    $response | ConvertTo-Json -Depth 10
} catch {
    Write-Host "Error: $_"
    $_.Exception.Response | ConvertTo-Json
}
