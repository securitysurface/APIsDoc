# SecuritySurface API Demos

This repository contains demo code for the SecuritySurface API, providing examples in both Python and cURL (Bash/PowerShell) formats. All demos demonstrate how to interact with the SecuritySurface API to retrieve security information, perform scans, and manage vulnerability data.

## Features

- **21 API Endpoints**: Complete coverage of SecuritySurface API
- **Multiple Language Support**: Python and cURL implementations
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Ready-to-Use**: All demos are fully functional and can be run immediately
- **Raw JSON Output**: All demos return raw JSON data for easy integration

## Table of Contents

- [Quick Start](#quick-start)
- [API Categories](#api-categories)
- [Python Demos](#python-demos)
- [cURL Demos](#curl-demos)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

### Python

```bash
# Install dependencies
cd Python
pip install -r requirements.txt

# Run a demo
python get_search_summary_demo.py
```

### cURL (Bash)

```bash
# Make script executable
chmod +x cURL/curl_search_summary_demo.sh

# Run the script
bash cURL/curl_search_summary_demo.sh
```

### cURL (PowerShell - Windows 11)

```powershell
# Set execution policy (first time only)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Run the script
cd cURL
.\curl_search_summary_demo.ps1
```

## API Categories

### Search APIs (11 endpoints)

Domain security and information lookup APIs:

1. **Summary** - Get security summary (DMARC, SPF, network info)
2. **WHOIS Current** - Get current WHOIS information
3. **DNS Current** - Get current DNS records
4. **DNS Reverse** - Reverse DNS lookup
5. **DNS History** - Historical DNS records
6. **Subdomains** - Get subdomain information
7. **IP Blocks** - Get IP block information
8. **IP Detection** - Get IP detection details
9. **SSL Certificate** - Get SSL certificate information
10. **Site Technologies** - Get website technologies
11. **Associated Domains** - Get associated domains

### Scan APIs (10 endpoints)

Security scanning and vulnerability management:

1. **Get Proxy** - Get available proxy servers
2. **Create Scan** - Initiate a new security scan
3. **Scan Overview** - Get scan operations overview
4. **Scan Scans** - List all scan results
5. **Stop Scan** - Stop an ongoing scan
6. **Scan Statistics** - Get detailed scan statistics
7. **Site Structure** - Get website structure
8. **Vulnerabilities** - List vulnerabilities from scans
9. **Vulnerability Detail** - Get detailed vulnerability information
10. **Delete Scan** - Delete a scan

## Python Demos

The Python implementation provides a reusable API client class (`SecuritySurfaceAPI`) and individual demo scripts for each endpoint.

### Installation

```bash
cd Python
pip install -r requirements.txt
```

### API Client Class

All Python demos use the `SecuritySurfaceAPI` class from `securitysurface_api.py`:

```python
from securitysurface_api import SecuritySurfaceAPI
import json

# Initialize API client
api_client = SecuritySurfaceAPI(api_key="your_api_key")

# Get summary for a domain
summary_data = api_client.get_summary(domain="example.com")

# Output raw JSON
if summary_data:
    print(json.dumps(summary_data, indent=2, ensure_ascii=False))
```

### Available Python Demos

| API | File | Method |
|-----|------|--------|
| Get Summary | `get_search_summary_demo.py` | `get_summary(domain)` |
| Get WHOIS | `get_search_whois_demo.py` | `get_whois_current(domain)` |
| Get DNS Current | `get_search_dns_current_demo.py` | `get_dns_current(domain)` |
| Get DNS Reverse | `get_search_dns_reverse_demo.py` | `get_dns_reverse(domain, dns_type, page)` |
| Get DNS History | `get_search_dns_history_demo.py` | `get_dns_history(domain, dns_type, page)` |
| Get Subdomains | `get_search_subdomains_demo.py` | `get_subdomains(domain, page)` |
| Get IP Blocks | `get_search_ip_blocks_demo.py` | `get_ip_blocks(domain)` |
| Get IP Detection | `get_search_ip_detection_demo.py` | `get_ip_detection(domain)` |
| Get SSL Certificate | `get_search_ssl_cert_demo.py` | `get_ssl_cert(domain)` |
| Get Site Technologies | `get_search_site_technologies_demo.py` | `get_site_technologies(domain)` |
| Get Associated Domains | `get_search_site_associated_domains_demo.py` | `get_site_associated_domains(domain)` |
| Get Scan Proxy | `get_scan_proxy_demo.py` | `get_scan_proxy()` |
| Create Scan | `get_scan_createscan_demo.py` | `create_scan(address, comment, scan_type, proxyid, useragent)` |
| Get Scan Overview | `get_scan_overview_demo.py` | `get_scan_overview()` |
| Get Scan Scans | `get_scan_scans_demo.py` | `get_scan_scans(start_index, limit)` |
| Stop Scan | `get_scan_stopscan_demo.py` | `stop_scan(scan_ids)` |
| Get Scan Statistics | `get_scan_statistics_demo.py` | `get_scan_statistics(scan_id)` |
| Get Site Structure | `get_scan_sitestructure_demo.py` | `get_scan_sitestructure(scan_id, directory_id)` |
| Get Vulnerabilities | `get_scan_vulnerabilities_demo.py` | `get_scan_vulnerabilities(scan_id, start_position, limit)` |
| Get Vulnerability Detail | `get_scan_vulnerabilitydetail_demo.py` | `get_scan_vulnerabilitydetail(vlun_id)` |
| Delete Scan | `get_scan_deletescan_demo.py` | `delete_scan(scan_ids)` |

For detailed documentation, see [Python/README.md](Python/README.md)

## cURL Demos

The cURL implementation provides shell scripts in both Bash (.sh) and PowerShell (.ps1) formats for direct API calls.

### Bash Scripts (.sh)

For Linux, macOS, and Unix-like systems:

```bash
cd cURL
bash curl_search_summary_demo.sh
```

### PowerShell Scripts (.ps1)

For Windows 11 and Windows PowerShell:

```powershell
cd cURL
.\curl_search_summary_demo.ps1
```

### Available cURL Demos

All APIs are available in both Bash and PowerShell formats:

| API | Bash File | PowerShell File |
|-----|-----------|-----------------|
| Get Summary | `curl_search_summary_demo.sh` | `curl_search_summary_demo.ps1` |
| Get WHOIS | `curl_search_whois_demo.sh` | `curl_search_whois_demo.ps1` |
| Get DNS Current | `curl_search_dns_current_demo.sh` | `curl_search_dns_current_demo.ps1` |
| Get DNS Reverse | `curl_search_dns_reverse_demo.sh` | `curl_search_dns_reverse_demo.ps1` |
| Get DNS History | `curl_search_dns_history_demo.sh` | `curl_search_dns_history_demo.ps1` |
| Get Subdomains | `curl_search_subdomains_demo.sh` | `curl_search_subdomains_demo.ps1` |
| Get IP Blocks | `curl_search_ip_blocks_demo.sh` | `curl_search_ip_blocks_demo.ps1` |
| Get IP Detection | `curl_search_ip_detection_demo.sh` | `curl_search_ip_detection_demo.ps1` |
| Get SSL Certificate | `curl_search_ssl_cert_demo.sh` | `curl_search_ssl_cert_demo.ps1` |
| Get Site Technologies | `curl_search_site_technologies_demo.sh` | `curl_search_site_technologies_demo.ps1` |
| Get Associated Domains | `curl_search_site_associated_domains_demo.sh` | `curl_search_site_associated_domains_demo.ps1` |
| Get Scan Proxy | `curl_scan_proxy_demo.sh` | `curl_scan_proxy_demo.ps1` |
| Create Scan | `curl_scan_createscan_demo.sh` | `curl_scan_createscan_demo.ps1` |
| Get Scan Overview | `curl_scan_overview_demo.sh` | `curl_scan_overview_demo.ps1` |
| Get Scan Scans | `curl_scan_scans_demo.sh` | `curl_scan_scans_demo.ps1` |
| Stop Scan | `curl_scan_stopscan_demo.sh` | `curl_scan_stopscan_demo.ps1` |
| Get Scan Statistics | `curl_scan_statistics_demo.sh` | `curl_scan_statistics_demo.ps1` |
| Get Site Structure | `curl_scan_sitestructure_demo.sh` | `curl_scan_sitestructure_demo.ps1` |
| Get Vulnerabilities | `curl_scan_vulnerabilities_demo.sh` | `curl_scan_vulnerabilities_demo.ps1` |
| Get Vulnerability Detail | `curl_scan_vulnerabilitydetail_demo.sh` | `curl_scan_vulnerabilitydetail_demo.ps1` |
| Delete Scan | `curl_scan_deletescan_demo.sh` | `curl_scan_deletescan_demo.ps1` |

For detailed documentation, see [cURL/README.md](cURL/README.md)

## API Reference

### Base URL

```
https://api.securitysurface.com/v1
```

### Authentication

All API requests require an API key passed in the `apikey` header:

```
apikey: your_api_key
```

### Response Format

All API responses are in JSON format. Successful responses include a `status` field with value `"ss_success"`.

### Error Handling

If a request fails, the API may return an error response. All demo scripts handle errors gracefully and output error information.

## Project Structure

```
.
├── Python/
│   ├── securitysurface_api.py          # Main API client class
│   ├── get_search_*.py                 # Search API demos (11 files)
│   ├── get_scan_*.py                   # Scan API demos (10 files)
│   ├── requirements.txt                # Python dependencies
│   └── README.md                       # Python documentation
├── cURL/
│   ├── curl_search_*.sh                # Search API Bash demos (11 files)
│   ├── curl_search_*.ps1               # Search API PowerShell demos (11 files)
│   ├── curl_scan_*.sh                  # Scan API Bash demos (10 files)
│   ├── curl_scan_*.ps1                 # Scan API PowerShell demos (10 files)
│   └── README.md                       # cURL documentation
└── README.md                           # This file
```

## Requirements

### Python

- Python 3.6+
- `requests` library (>=2.31.0)

Install dependencies:
```bash
pip install -r Python/requirements.txt
```

### cURL

- **Bash**: `curl` command (usually pre-installed on Linux/macOS)
- **PowerShell**: Windows PowerShell 5.1+ or PowerShell Core 7+

## Usage Examples

### Python Example

```python
from securitysurface_api import SecuritySurfaceAPI
import json

# Initialize API client
api_client = SecuritySurfaceAPI(api_key="your_api_key")

# Get summary for a domain
summary_data = api_client.get_summary(domain="example.com")

# Output raw JSON
if summary_data:
    print(json.dumps(summary_data, indent=2, ensure_ascii=False))
```

### cURL Bash Example

```bash
API_KEY="your_api_key"
DOMAIN="example.com"

curl -i -X GET "https://api.securitysurface.com/v1/search/summary?domain=${DOMAIN}" \
-H "apikey: ${API_KEY}" \
-H "Content-Type: application/json"
```

### cURL PowerShell Example

```powershell
$API_KEY = "your_api_key"
$DOMAIN = "example.com"

$headers = @{
    "apikey" = $API_KEY
    "Content-Type" = "application/json"
}

$uri = "https://api.securitysurface.com/v1/search/summary?domain=$DOMAIN"

$response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers
$response | ConvertTo-Json -Depth 10
```

## API Key Security

⚠️ **Important Security Notes:**

- All demo scripts include a hardcoded API key for demonstration purposes
- **Never commit API keys to version control**
- Use environment variables to store API keys in production
- Rotate API keys regularly
- If your API key is exposed, revoke it immediately and generate a new one

### Using Environment Variables

**Python:**
```python
import os
api_key = os.getenv('SECURITYSURFACE_API_KEY', 'default-key')
```

**Bash:**
```bash
API_KEY="${SECURITYSURFACE_API_KEY}"
```

**PowerShell:**
```powershell
$API_KEY = $env:SECURITYSURFACE_API_KEY
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is provided as-is for demonstration purposes. Please refer to the SecuritySurface API documentation for terms of service and usage guidelines.

## Support

For API documentation and support, visit:
- API Documentation: https://securitysurface.com/doc/api
- API Base URL: https://api.securitysurface.com/v1

## Related Documentation

- [Python API Demos Documentation](Python/README.md)
- [cURL API Demos Documentation](cURL/README.md)
