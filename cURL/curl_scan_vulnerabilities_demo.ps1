# SecuritySurface API - Get Scan Vulnerabilities Demo
# Demonstrates how to use the API to get a list of vulnerabilities from scans

$API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
$SCAN_ID = "1207526e-931f-4971-98f8-e08f167cdd66"
$START_POSITION = "0"
$LIMIT = "100"

$headers = @{
    "apikey" = $API_KEY
    "Content-Type" = "application/json"
}

$uri = "https://api.securitysurface.com/v1/scan/vulnerabilities?scan_id=$SCAN_ID&c=$START_POSITION&l=$LIMIT"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers
    $response | ConvertTo-Json -Depth 10
} catch {
    Write-Host "Error: $_"
    $_.Exception.Response | ConvertTo-Json
}
