# SecuritySurface API Python Demos

This directory contains Python demo scripts for the SecuritySurface API. All demos return raw JSON data from the API responses.

## Overview

All demo scripts follow the same pattern:
- Import the `SecuritySurfaceAPI` class from `securitysurface_api.py`
- Create an API client instance with your API key
- Call the appropriate API method
- Output raw JSON data using `json.dumps()`

## API Client Class

The main API client class is located in `securitysurface_api.py`. This class provides methods for all available SecuritySurface API endpoints.

## Available Demos

### 1. Get Summary
**File:** `get_search_summary_demo.py`  
**API Method:** `get_summary(domain)`  
**Endpoint:** `/v1/search/summary`  
**Description:** Get security summary information for a specified domain, including DMARC, SPF, site, and network information.

**Usage:**
```bash
python get_search_summary_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

**Returns:** Raw JSON containing summary data with DMARC, SPF, site, and network information.

---

### 2. Get WHOIS Current
**File:** `get_search_whois_demo.py`  
**API Method:** `get_whois_current(domain)`  
**Endpoint:** `/v1/search/whois/current`  
**Description:** Get current WHOIS information for a specified domain, including registrar, registration dates, status, and contact information.

**Usage:**
```bash
python get_search_whois_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

**Returns:** Raw JSON containing WHOIS data with registrar, dates, status, and contact information.

---

### 3. Get DNS Current
**File:** `get_search_dns_current_demo.py`  
**API Method:** `get_dns_current(domain)`  
**Endpoint:** `/v1/search/dns/current`  
**Description:** Get current DNS records for a specified domain, including A, AAAA, MX, NS, SOA, and TXT records.

**Usage:**
```bash
python get_search_dns_current_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

**Returns:** Raw JSON containing DNS records (A, AAAA, MX, NS, SOA, TXT).

---

### 4. Get DNS Reverse
**File:** `get_search_dns_reverse_demo.py`  
**API Method:** `get_dns_reverse(domain, dns_type, page)`  
**Endpoint:** `/v1/search/dns/reverse`  
**Description:** Get reverse DNS lookup information for a specified IP address or domain.

**Usage:**
```bash
python get_search_dns_reverse_demo.py
```

**Parameters:**
- `domain` (string, required): IP address or domain to query, e.g., "8.8.8.8"
- `dns_type` (string, required): Type of DNS record to query, e.g., "a", "aaaa", "mx", "ns", "soa", "txt"
- `page` (int, required): Page number for pagination, default is 1

**Returns:** Raw JSON containing reverse DNS records with DNS type, TTL, and raw text data.

---

### 5. Get DNS History
**File:** `get_search_dns_history_demo.py`  
**API Method:** `get_dns_history(domain, dns_type, page)`  
**Endpoint:** `/v1/search/dns/history`  
**Description:** Get DNS history for a specified domain, including changes over a specified time range.

**Usage:**
```bash
python get_search_dns_history_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"
- `dns_type` (string, required): Type of DNS record to query, e.g., "A", "AAAA", "MX", "NS", "SOA", "TXT"
- `page` (int, required): Page number for pagination, default is 1

**Returns:** Raw JSON containing historical DNS records with DNS type, TTL, and raw text data.

---

### 6. Get Subdomains
**File:** `get_search_subdomains_demo.py`  
**API Method:** `get_subdomains(domain, page)`  
**Endpoint:** `/v1/search/subdomains`  
**Description:** Get subdomains information for a specified domain, including details such as IP address, organization, ISP, and country.

**Usage:**
```bash
python get_search_subdomains_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"
- `page` (int, required): Page number for pagination, default is 1

**Returns:** Raw JSON containing subdomains with first_seen and last_seen dates.

---

### 7. Get IP Blocks
**File:** `get_search_ip_blocks_demo.py`  
**API Method:** `get_ip_blocks(domain)`  
**Endpoint:** `/v1/search/ip/blocks`  
**Description:** Get IP blocks information associated with a specified domain, including details about IP addresses, IP versions, and RDAP information.

**Usage:**
```bash
python get_search_ip_blocks_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

**Returns:** Raw JSON containing IP blocks with IP addresses, IP versions, and RDAP information.

---

### 8. Get IP Detection
**File:** `get_search_ip_detection_demo.py`  
**API Method:** `get_ip_detection(domain)`  
**Endpoint:** `/v1/search/ip/detection`  
**Description:** Get IP detection information for a specified domain, including details such as IP addresses, ASN, country, ISP, location, and CDN status.

**Usage:**
```bash
python get_search_ip_detection_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

**Returns:** Raw JSON containing IP detection information with IP addresses, ASN, country, ISP, location, and CDN status.

---

### 9. Get SSL Certificate
**File:** `get_search_ssl_cert_demo.py`  
**API Method:** `get_ssl_cert(domain)`  
**Endpoint:** `/v1/search/ssl/cert`  
**Description:** Get detailed information about the SSL certificate for a specified domain, including version, signature, fingerprints, issuer, subject, validity period, serial number, and cipher details.

**Usage:**
```bash
python get_search_ssl_cert_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

**Returns:** Raw JSON containing SSL certificate information with version, signature, fingerprints, issuer, subject, validity period, serial number, and cipher details.

---

### 10. Get Site Technologies
**File:** `get_search_site_technologies_demo.py`  
**API Method:** `get_site_technologies(domain)`  
**Endpoint:** `/v1/search/site/technologies`  
**Description:** Get information about the technologies used by a specified domain, including details such as category, website, description, and icon for each technology.

**Usage:**
```bash
python get_search_site_technologies_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

**Returns:** Raw JSON containing technologies information with category, website, description, and icon for each technology.

---

### 11. Get Site Associated Domains
**File:** `get_search_site_associated_domains_demo.py`  
**API Method:** `get_site_associated_domains(domain)`  
**Endpoint:** `/v1/search/site/associateddomains`  
**Description:** Get a list of domains associated with a specified domain, including information about the organization and ISP.

**Usage:**
```bash
python get_search_site_associated_domains_demo.py
```

**Parameters:**
- `domain` (string, required): The domain to query, e.g., "example.com"

**Returns:** Raw JSON containing associated domains with organization and ISP information.

---

## Scan APIs

### 12. Get Scan Proxy
**File:** `get_scan_proxy_demo.py`  
**API Method:** `get_scan_proxy()`  
**Endpoint:** `/v1/scan/getproxy`  
**Description:** Get a list of available proxy/tunnel servers with their current latency information. Use this endpoint to select the optimal proxy server for your scanning tasks.

**Usage:**
```bash
python get_scan_proxy_demo.py
```

**Parameters:**
- No parameters required

**Returns:** Raw JSON containing proxy server information with id, name, and delay.

---

### 13. Create Scan
**File:** `get_scan_createscan_demo.py`  
**API Method:** `create_scan(address, comment, scan_type, proxyid, useragent)`  
**Endpoint:** `/v1/scan/createscan`  
**Description:** Initiate a new scan for a specified address. You can specify the type of scan and optionally add a comment to the scan.

**Usage:**
```bash
python get_scan_createscan_demo.py
```

**Parameters:**
- `address` (string, required): The target address to scan, e.g., "https://example.com"
- `comment` (string, required): The comment to be used for the scan
- `scan_type` (string, required): Type of scan - "st.bi" (Crawl Only), "st.xss" (Cross-site Scripting), "st.si" (SQL Injection), "st.hmr" (Critical/High/Medium Risk), "st.fs" (Full-scan)
- `proxyid` (string, required): The unique identifier of the proxy to be used
- `useragent` (string, required): The user agent to be used, default is "Default"

**Returns:** Raw JSON containing scan_id, server_id, and status.

---

### 14. Get Scan Overview
**File:** `get_scan_overview_demo.py`  
**API Method:** `get_scan_overview()`  
**Endpoint:** `/v1/scan/overview`  
**Description:** Get an overview of scan operations, including the total number of scans, the status of current scans, and vulnerability counts.

**Usage:**
```bash
python get_scan_overview_demo.py
```

**Parameters:**
- No parameters required

**Returns:** Raw JSON containing scans_completed_count, scans_running_count, scans_waiting_count, scans_total_count, and vuln_count.

---

### 15. Get Scan Scans
**File:** `get_scan_scans_demo.py`  
**API Method:** `get_scan_scans(start_index, limit)`  
**Endpoint:** `/v1/scan/scans`  
**Description:** Get a list of scan results, including details such as the target address, scan status, and vulnerability counts.

**Usage:**
```bash
python get_scan_scans_demo.py
```

**Parameters:**
- `start_index` (int, required): The starting index for pagination, defaults to 0
- `limit` (int, required): The number of scan results to return, defaults to 100

**Returns:** Raw JSON containing pagination information and scan results with address, tag, profile, start_date, progress, status, scan_id, and vuln_counts.

---

### 16. Stop Scan
**File:** `get_scan_stopscan_demo.py`  
**API Method:** `stop_scan(scan_ids)`  
**Endpoint:** `/v1/scan/stopscan`  
**Description:** Stop an ongoing scan by providing the scan ID. The scan_id parameter is an array of scan IDs.

**Usage:**
```bash
python get_scan_stopscan_demo.py
```

**Parameters:**
- `scan_ids` (list, required): An array of scan IDs to be stopped

**Returns:** Raw JSON containing status message.

---

### 17. Get Scan Statistics
**File:** `get_scan_statistics_demo.py`  
**API Method:** `get_scan_statistics(scan_id)`  
**Endpoint:** `/v1/scan/statistics`  
**Description:** Get detailed statistics for a specific scan, including progress, status, vulnerabilities found, and other relevant information.

**Usage:**
```bash
python get_scan_statistics_demo.py
```

**Parameters:**
- `scan_id` (string, required): The unique identifier of the scan

**Returns:** Raw JSON containing progress, progress_status, duration, aborted status, scan_status, target_info, vuln_counts, and discovered_hosts.

---

### 18. Get Scan Site Structure
**File:** `get_scan_sitestructure_demo.py`  
**API Method:** `get_scan_sitestructure(scan_id, directory_id)`  
**Endpoint:** `/v1/scan/sitestructure`  
**Description:** Get the structure of a website based on the specified directory ID. The id parameter is the root node ID.

**Usage:**
```bash
python get_scan_sitestructure_demo.py
```

**Parameters:**
- `scan_id` (string, required): The unique identifier for the scan
- `directory_id` (int, required): The ID of the directory to query, root directory is represented by 0, defaults to 0

**Returns:** Raw JSON containing site structure with id, type, name, parent_id, and path.

---

### 19. Get Scan Vulnerabilities
**File:** `get_scan_vulnerabilities_demo.py`  
**API Method:** `get_scan_vulnerabilities(scan_id, start_position, limit)`  
**Endpoint:** `/v1/scan/vulnerabilities`  
**Description:** Get a list of vulnerabilities from scans.

**Usage:**
```bash
python get_scan_vulnerabilities_demo.py
```

**Parameters:**
- `scan_id` (string, required): The ID of the scan to query
- `start_position` (int, required): The starting position for the query, starts from 0, defaults to 0
- `limit` (int, required): The number of vulnerabilities to retrieve, defaults to 100

**Returns:** Raw JSON containing pagination information and vulnerabilities with name, url, parameter, severity, and id.

---

### 20. Get Scan Vulnerability Detail
**File:** `get_scan_vulnerabilitydetail_demo.py`  
**API Method:** `get_scan_vulnerabilitydetail(vlun_id)`  
**Endpoint:** `/v1/scan/vulnerabilitydetail`  
**Description:** Get detailed information about a specific vulnerability identified by its vlun_id. It includes the vulnerability name, affected details, severity, description, request/response data, and more.

**Usage:**
```bash
python get_scan_vulnerabilitydetail_demo.py
```

**Parameters:**
- `vlun_id` (string, required): The unique identifier for the vulnerability

**Returns:** Raw JSON containing vulnerability details including name, parameter, url, severity, description, details, request, and response.

---

### 21. Delete Scan
**File:** `get_scan_deletescan_demo.py`  
**API Method:** `delete_scan(scan_ids)`  
**Endpoint:** `/v1/scan/deletescan`  
**Description:** Delete a specific scan by its ID. Once a scan is deleted, it cannot be recovered. The scan_id parameter is an array of scan IDs.

**Usage:**
```bash
python get_scan_deletescan_demo.py
```

**Parameters:**
- `scan_ids` (list, required): An array of scan IDs to be deleted

**Returns:** Raw JSON containing status message.

---

## Common Features

### All Demos Return Raw JSON

All demo scripts output raw JSON data using `json.dumps()` with the following settings:
- `indent=2`: Pretty-printed JSON with 2-space indentation
- `ensure_ascii=False`: Preserves non-ASCII characters

### Error Handling

If an API request fails, all demos return a JSON error object:
```json
{
  "error": "Failed to retrieve [data type]"
}
```

### API Key

All demos use the same API key (hardcoded for demonstration purposes). In production, you should:
- Use environment variables to store API keys
- Never commit API keys to version control
- Rotate API keys regularly

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:
- `requests>=2.31.0`

## File Structure

```
Python/
├── securitysurface_api.py                      # Main API client class
├── get_search_summary_demo.py                  # Summary demo
├── get_search_whois_demo.py                    # WHOIS demo
├── get_search_dns_current_demo.py              # DNS Current demo
├── get_search_dns_reverse_demo.py              # DNS Reverse demo
├── get_search_dns_history_demo.py              # DNS History demo
├── get_search_subdomains_demo.py               # Subdomains demo
├── get_search_ip_blocks_demo.py                # IP Blocks demo
├── get_search_ip_detection_demo.py             # IP Detection demo
├── get_search_ssl_cert_demo.py                # SSL Certificate demo
├── get_search_site_technologies_demo.py        # Site Technologies demo
├── get_search_site_associated_domains_demo.py  # Associated Domains demo
├── get_scan_proxy_demo.py                      # Scan Proxy demo
├── get_scan_createscan_demo.py                 # Create Scan demo
├── get_scan_overview_demo.py                   # Scan Overview demo
├── get_scan_scans_demo.py                      # Scan Scans demo
├── get_scan_stopscan_demo.py                   # Stop Scan demo
├── get_scan_statistics_demo.py                 # Scan Statistics demo
├── get_scan_sitestructure_demo.py              # Scan Site Structure demo
├── get_scan_vulnerabilities_demo.py            # Scan Vulnerabilities demo
├── get_scan_vulnerabilitydetail_demo.py        # Scan Vulnerability Detail demo
├── get_scan_deletescan_demo.py                 # Delete Scan demo
├── requirements.txt                             # Python dependencies
└── README.md                                    # This file
```

## Usage Examples

### Search API Example

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

### Scan API Example

```python
from securitysurface_api import SecuritySurfaceAPI
import json

# Initialize API client
api_client = SecuritySurfaceAPI(api_key="your_api_key")

# Get scan overview
overview_data = api_client.get_scan_overview()

# Output raw JSON
if overview_data:
    print(json.dumps(overview_data, indent=2, ensure_ascii=False))
```

## Notes

- All API methods return `Optional[Dict[Any, Any]]` - they return `None` if the request fails
- All demos handle errors gracefully and output JSON error objects
- The API base URL is `https://api.securitysurface.com/v1` by default
- Authentication is done via the `apikey` header
