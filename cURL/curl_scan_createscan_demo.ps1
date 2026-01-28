# SecuritySurface API - Create Scan Demo
# Demonstrates how to use the API to initiate a new scan for a specified address

$API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
$ADDRESS = "http://"
$COMMENT = "this is a example"
$SCAN_TYPE = "st.fs"
$PROXYID = "25"
$USERAGENT = "Default"

$headers = @{
    "apikey" = $API_KEY
    "Content-Type" = "application/json"
}

$body = @{
    address = $ADDRESS
    comment = $COMMENT
    type = $SCAN_TYPE
    proxyid = $PROXYID
    useragent = $USERAGENT
} | ConvertTo-Json

$uri = "https://api.securitysurface.com/v1/scan/createscan"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body
    $response | ConvertTo-Json -Depth 10
} catch {
    Write-Host "Error: $_"
    $_.Exception.Response | ConvertTo-Json
}
