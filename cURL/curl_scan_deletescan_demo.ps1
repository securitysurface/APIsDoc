# SecuritySurface API - Delete Scan Demo
# Demonstrates how to use the API to delete a specific scan

$API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
$SCAN_ID = "1207526e-931f-4971-98f8-e08f167cdd66"

$headers = @{
    "apikey" = $API_KEY
    "Content-Type" = "application/json"
}

$body = @{
    scan_id = @($SCAN_ID)
} | ConvertTo-Json

$uri = "https://api.securitysurface.com/v1/scan/deletescan"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body
    $response | ConvertTo-Json -Depth 10
} catch {
    Write-Host "Error: $_"
    $_.Exception.Response | ConvertTo-Json
}
