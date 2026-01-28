# SecuritySurface API cURL Demos

This directory contains cURL demo scripts for the SecuritySurface API. All demos are available in both Bash (.sh) and PowerShell (.ps1) formats.

## Overview

All demo scripts follow the same pattern:
- Set API key and parameters as variables
- Use curl (Bash) or Invoke-RestMethod (PowerShell) to make API requests
- Output raw JSON responses

## Available Formats

- **Bash Scripts (.sh)**: For Linux, macOS, and Unix-like systems
- **PowerShell Scripts (.ps1)**: For Windows 11 and Windows PowerShell environments

## Search API Demos

### 1. Get Summary
**Bash:** `curl_search_summary_demo.sh`  
**PowerShell:** `curl_search_summary_demo.ps1`  
**Endpoint:** `/v1/search/summary`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_summary_demo.sh

# PowerShell
.\curl_search_summary_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

---

### 2. Get WHOIS Current
**Bash:** `curl_search_whois_demo.sh`  
**PowerShell:** `curl_search_whois_demo.ps1`  
**Endpoint:** `/v1/search/whois/current`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_whois_demo.sh

# PowerShell
.\curl_search_whois_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

---

### 3. Get DNS Current
**Bash:** `curl_search_dns_current_demo.sh`  
**PowerShell:** `curl_search_dns_current_demo.ps1`  
**Endpoint:** `/v1/search/dns/current`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_dns_current_demo.sh

# PowerShell
.\curl_search_dns_current_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

---

### 4. Get DNS Reverse
**Bash:** `curl_search_dns_reverse_demo.sh`  
**PowerShell:** `curl_search_dns_reverse_demo.ps1`  
**Endpoint:** `/v1/search/dns/reverse`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_dns_reverse_demo.sh

# PowerShell
.\curl_search_dns_reverse_demo.ps1
```

**Parameters:**
- `domain` (string, required): IP address or domain to query, e.g., "8.8.8.8"
- `type` (string, required): Type of DNS record to query, e.g., "a", "aaaa", "mx", "ns", "soa", "txt"
- `page` (int, required): Page number for pagination, default is 1

---

### 5. Get DNS History
**Bash:** `curl_search_dns_history_demo.sh`  
**PowerShell:** `curl_search_dns_history_demo.ps1`  
**Endpoint:** `/v1/search/dns/history`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_dns_history_demo.sh

# PowerShell
.\curl_search_dns_history_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"
- `type` (string, required): Type of DNS record to query, e.g., "A", "AAAA", "MX", "NS", "SOA", "TXT"
- `page` (int, required): Page number for pagination, default is 1

---

### 6. Get Subdomains
**Bash:** `curl_search_subdomains_demo.sh`  
**PowerShell:** `curl_search_subdomains_demo.ps1`  
**Endpoint:** `/v1/search/subdomains`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_subdomains_demo.sh

# PowerShell
.\curl_search_subdomains_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"
- `page` (int, required): Page number for pagination, default is 1

---

### 7. Get IP Blocks
**Bash:** `curl_search_ip_blocks_demo.sh`  
**PowerShell:** `curl_search_ip_blocks_demo.ps1`  
**Endpoint:** `/v1/search/ip/blocks`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_ip_blocks_demo.sh

# PowerShell
.\curl_search_ip_blocks_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

---

### 8. Get IP Detection
**Bash:** `curl_search_ip_detection_demo.sh`  
**PowerShell:** `curl_search_ip_detection_demo.ps1`  
**Endpoint:** `/v1/search/ip/detection`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_ip_detection_demo.sh

# PowerShell
.\curl_search_ip_detection_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

---

### 9. Get SSL Certificate
**Bash:** `curl_search_ssl_cert_demo.sh`  
**PowerShell:** `curl_search_ssl_cert_demo.ps1`  
**Endpoint:** `/v1/search/ssl/cert`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_ssl_cert_demo.sh

# PowerShell
.\curl_search_ssl_cert_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

---

### 10. Get Site Technologies
**Bash:** `curl_search_site_technologies_demo.sh`  
**PowerShell:** `curl_search_site_technologies_demo.ps1`  
**Endpoint:** `/v1/search/site/technologies`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_site_technologies_demo.sh

# PowerShell
.\curl_search_site_technologies_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

---

### 11. Get Site Associated Domains
**Bash:** `curl_search_site_associated_domains_demo.sh`  
**PowerShell:** `curl_search_site_associated_domains_demo.ps1`  
**Endpoint:** `/v1/search/site/associateddomains`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_search_site_associated_domains_demo.sh

# PowerShell
.\curl_search_site_associated_domains_demo.ps1
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

---

## Scan API Demos

### 12. Get Scan Proxy
**Bash:** `curl_scan_proxy_demo.sh`  
**PowerShell:** `curl_scan_proxy_demo.ps1`  
**Endpoint:** `/v1/scan/getproxy`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_scan_proxy_demo.sh

# PowerShell
.\curl_scan_proxy_demo.ps1
```

**Parameters:**
- No parameters required

---

### 13. Create Scan
**Bash:** `curl_scan_createscan_demo.sh`  
**PowerShell:** `curl_scan_createscan_demo.ps1`  
**Endpoint:** `/v1/scan/createscan`  
**Method:** POST

**Usage:**
```bash
# Bash
bash curl_scan_createscan_demo.sh

# PowerShell
.\curl_scan_createscan_demo.ps1
```

**Parameters:**
- `address` (string, required): The target address to scan, e.g., "https://example.com"
- `comment` (string, required): The comment to be used for the scan
- `type` (string, required): Type of scan - "st.bi" (Crawl Only), "st.xss" (Cross-site Scripting), "st.si" (SQL Injection), "st.hmr" (Critical/High/Medium Risk), "st.fs" (Full-scan)
- `proxyid` (string, required): The unique identifier of the proxy to be used
- `useragent` (string, required): The user agent to be used, default is "Default"

---

### 14. Get Scan Overview
**Bash:** `curl_scan_overview_demo.sh`  
**PowerShell:** `curl_scan_overview_demo.ps1`  
**Endpoint:** `/v1/scan/overview`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_scan_overview_demo.sh

# PowerShell
.\curl_scan_overview_demo.ps1
```

**Parameters:**
- No parameters required

---

### 15. Get Scan Scans
**Bash:** `curl_scan_scans_demo.sh`  
**PowerShell:** `curl_scan_scans_demo.ps1`  
**Endpoint:** `/v1/scan/scans`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_scan_scans_demo.sh

# PowerShell
.\curl_scan_scans_demo.ps1
```

**Parameters:**
- `c` (int, required): The starting index for pagination, defaults to 0
- `l` (int, required): The number of scan results to return, defaults to 100

---

### 16. Stop Scan
**Bash:** `curl_scan_stopscan_demo.sh`  
**PowerShell:** `curl_scan_stopscan_demo.ps1`  
**Endpoint:** `/v1/scan/stopscan`  
**Method:** POST

**Usage:**
```bash
# Bash
bash curl_scan_stopscan_demo.sh

# PowerShell
.\curl_scan_stopscan_demo.ps1
```

**Parameters:**
- `scan_id` (array, required): An array of scan IDs to be stopped

---

### 17. Get Scan Statistics
**Bash:** `curl_scan_statistics_demo.sh`  
**PowerShell:** `curl_scan_statistics_demo.ps1`  
**Endpoint:** `/v1/scan/statistics`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_scan_statistics_demo.sh

# PowerShell
.\curl_scan_statistics_demo.ps1
```

**Parameters:**
- `scan_id` (string, required): The unique identifier of the scan

---

### 18. Get Scan Site Structure
**Bash:** `curl_scan_sitestructure_demo.sh`  
**PowerShell:** `curl_scan_sitestructure_demo.ps1`  
**Endpoint:** `/v1/scan/sitestructure`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_scan_sitestructure_demo.sh

# PowerShell
.\curl_scan_sitestructure_demo.ps1
```

**Parameters:**
- `scan_id` (string, required): The unique identifier for the scan
- `id` (int, required): The ID of the directory to query, root directory is represented by 0, defaults to 0

---

### 19. Get Scan Vulnerabilities
**Bash:** `curl_scan_vulnerabilities_demo.sh`  
**PowerShell:** `curl_scan_vulnerabilities_demo.ps1`  
**Endpoint:** `/v1/scan/vulnerabilities`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_scan_vulnerabilities_demo.sh

# PowerShell
.\curl_scan_vulnerabilities_demo.ps1
```

**Parameters:**
- `scan_id` (string, required): The ID of the scan to query
- `c` (int, required): The starting position for the query, starts from 0, defaults to 0
- `l` (int, required): The number of vulnerabilities to retrieve, defaults to 100

---

### 20. Get Scan Vulnerability Detail
**Bash:** `curl_scan_vulnerabilitydetail_demo.sh`  
**PowerShell:** `curl_scan_vulnerabilitydetail_demo.ps1`  
**Endpoint:** `/v1/scan/vulnerabilitydetail`  
**Method:** GET

**Usage:**
```bash
# Bash
bash curl_scan_vulnerabilitydetail_demo.sh

# PowerShell
.\curl_scan_vulnerabilitydetail_demo.ps1
```

**Parameters:**
- `vlun_id` (string, required): The unique identifier for the vulnerability

---

### 21. Delete Scan
**Bash:** `curl_scan_deletescan_demo.sh`  
**PowerShell:** `curl_scan_deletescan_demo.ps1`  
**Endpoint:** `/v1/scan/deletescan`  
**Method:** POST

**Usage:**
```bash
# Bash
bash curl_scan_deletescan_demo.sh

# PowerShell
.\curl_scan_deletescan_demo.ps1
```

**Parameters:**
- `scan_id` (array, required): An array of scan IDs to be deleted

---

## Common Features

### Bash Scripts (.sh)

- Use `curl` command with `-i` flag to include headers in output
- Use `-X` flag to specify HTTP method (GET, POST)
- Use `-H` flag to set request headers
- Use `-d` flag for POST request body data
- Variables are set at the top of the script

### PowerShell Scripts (.ps1)

- Use `Invoke-RestMethod` cmdlet for HTTP requests
- Headers are defined as hashtable `@{}`
- Request body is converted to JSON using `ConvertTo-Json`
- Response is converted to JSON using `ConvertTo-Json -Depth 10`
- Error handling with try-catch blocks

### API Key

All demos use the same API key (hardcoded for demonstration purposes). In production, you should:
- Use environment variables to store API keys
- Never commit API keys to version control
- Rotate API keys regularly

## Running Scripts

### Bash Scripts (Linux/macOS)

```bash
# Make script executable (first time only)
chmod +x curl_search_summary_demo.sh

# Run the script
bash curl_search_summary_demo.sh
# or
./curl_search_summary_demo.sh
```

### PowerShell Scripts (Windows 11)

```powershell
# If execution policy is restricted, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Run the script
.\curl_search_summary_demo.ps1
```

## File Structure

```
cURL/
├── curl_search_summary_demo.sh                  # Summary demo (Bash)
├── curl_search_summary_demo.ps1                 # Summary demo (PowerShell)
├── curl_search_whois_demo.sh                    # WHOIS demo (Bash)
├── curl_search_whois_demo.ps1                   # WHOIS demo (PowerShell)
├── curl_search_dns_current_demo.sh              # DNS Current demo (Bash)
├── curl_search_dns_current_demo.ps1             # DNS Current demo (PowerShell)
├── curl_search_dns_reverse_demo.sh              # DNS Reverse demo (Bash)
├── curl_search_dns_reverse_demo.ps1             # DNS Reverse demo (PowerShell)
├── curl_search_dns_history_demo.sh               # DNS History demo (Bash)
├── curl_search_dns_history_demo.ps1              # DNS History demo (PowerShell)
├── curl_search_subdomains_demo.sh               # Subdomains demo (Bash)
├── curl_search_subdomains_demo.ps1              # Subdomains demo (PowerShell)
├── curl_search_ip_blocks_demo.sh                # IP Blocks demo (Bash)
├── curl_search_ip_blocks_demo.ps1               # IP Blocks demo (PowerShell)
├── curl_search_ip_detection_demo.sh             # IP Detection demo (Bash)
├── curl_search_ip_detection_demo.ps1            # IP Detection demo (PowerShell)
├── curl_search_ssl_cert_demo.sh                 # SSL Certificate demo (Bash)
├── curl_search_ssl_cert_demo.ps1                # SSL Certificate demo (PowerShell)
├── curl_search_site_technologies_demo.sh         # Site Technologies demo (Bash)
├── curl_search_site_technologies_demo.ps1       # Site Technologies demo (PowerShell)
├── curl_search_site_associated_domains_demo.sh  # Associated Domains demo (Bash)
├── curl_search_site_associated_domains_demo.ps1 # Associated Domains demo (PowerShell)
├── curl_scan_proxy_demo.sh                     # Scan Proxy demo (Bash)
├── curl_scan_proxy_demo.ps1                    # Scan Proxy demo (PowerShell)
├── curl_scan_createscan_demo.sh                 # Create Scan demo (Bash)
├── curl_scan_createscan_demo.ps1                # Create Scan demo (PowerShell)
├── curl_scan_overview_demo.sh                   # Scan Overview demo (Bash)
├── curl_scan_overview_demo.ps1                  # Scan Overview demo (PowerShell)
├── curl_scan_scans_demo.sh                     # Scan Scans demo (Bash)
├── curl_scan_scans_demo.ps1                    # Scan Scans demo (PowerShell)
├── curl_scan_stopscan_demo.sh                  # Stop Scan demo (Bash)
├── curl_scan_stopscan_demo.ps1                 # Stop Scan demo (PowerShell)
├── curl_scan_statistics_demo.sh                 # Scan Statistics demo (Bash)
├── curl_scan_statistics_demo.ps1                # Scan Statistics demo (PowerShell)
├── curl_scan_sitestructure_demo.sh              # Scan Site Structure demo (Bash)
├── curl_scan_sitestructure_demo.ps1             # Scan Site Structure demo (PowerShell)
├── curl_scan_vulnerabilities_demo.sh            # Scan Vulnerabilities demo (Bash)
├── curl_scan_vulnerabilities_demo.ps1           # Scan Vulnerabilities demo (PowerShell)
├── curl_scan_vulnerabilitydetail_demo.sh        # Scan Vulnerability Detail demo (Bash)
├── curl_scan_vulnerabilitydetail_demo.ps1       # Scan Vulnerability Detail demo (PowerShell)
├── curl_scan_deletescan_demo.sh                # Delete Scan demo (Bash)
├── curl_scan_deletescan_demo.ps1                # Delete Scan demo (PowerShell)
└── README.md                                    # This file
```

## Notes

- All scripts use the same API key for demonstration purposes
- Bash scripts use `curl` command which is available on most Unix-like systems
- PowerShell scripts use `Invoke-RestMethod` which is built into Windows PowerShell
- All scripts output raw JSON responses
- Error handling is included in PowerShell scripts using try-catch blocks
- The API base URL is `https://api.securitysurface.com/v1`
- Authentication is done via the `apikey` header
