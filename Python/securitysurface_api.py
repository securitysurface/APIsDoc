"""
SecuritySurface API Client Class
General class for calling SecuritySurface API
"""

import requests
import json
from typing import Optional, Dict, Any


class SecuritySurfaceAPI:
    """SecuritySurface API Client Class"""
    
    def __init__(self, api_key: str, base_url: str = "https://api.securitysurface.com/v1"):
        """
        Initialize API client
        
        Args:
            api_key: API key
            base_url: API base URL, default is https://api.securitysurface.com/v1
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
        # Set default request headers
        self.session.headers.update({
            'apikey': self.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Optional[Dict[Any, Any]]:
        """
        Generic method for sending HTTP requests
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            **kwargs: Additional request parameters (query params, request body, etc.)
        
        Returns:
            API response JSON data, returns None if request fails
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=30,
                **kwargs
            )
            
            # Check HTTP status code
            response.raise_for_status()
            
            # Parse JSON response
            data = response.json()
            return data
            
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Content: {response.text}")
            return None
            
        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")
            return None
            
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            print(f"Response Content: {response.text}")
            return None
    
    def get_summary(self, domain: str) -> Optional[Dict[Any, Any]]:
        """
        Get security summary information for a specified domain
        
        Args:
            domain: Domain to query, e.g., example.com
        
        Returns:
            API response JSON data containing DMARC, SPF, site, and network information
        """
        endpoint = "/search/summary"
        params = {
            'domain': domain
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_whois_current(self, domain: str) -> Optional[Dict[Any, Any]]:
        """
        Get current WHOIS information for a specified domain
        
        Args:
            domain: Domain to query, e.g., example.com
        
        Returns:
            API response JSON data containing registrar, registration dates, status, and contact information
        """
        endpoint = "/search/whois/current"
        params = {
            'domain': domain
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_dns_current(self, domain: str) -> Optional[Dict[Any, Any]]:
        """
        Get current DNS records for a specified domain
        
        Args:
            domain: Domain to query, e.g., example.com
        
        Returns:
            API response JSON data containing A, AAAA, MX, NS, SOA, and TXT records
        """
        endpoint = "/search/dns/current"
        params = {
            'domain': domain
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_dns_reverse(self, domain: str, dns_type: str, page: int = 1) -> Optional[Dict[Any, Any]]:
        """
        Get reverse DNS lookup information for a specified IP address or domain
        
        Args:
            domain: IP address or domain to query, e.g., 8.8.8.8
            dns_type: Type of DNS record to query, e.g., a, aaaa, mx, ns, soa, txt
            page: Page number for pagination, default is 1
        
        Returns:
            API response JSON data containing reverse DNS records with DNS type, TTL, and raw text data
        """
        endpoint = "/search/dns/reverse"
        params = {
            'domain': domain,
            'type': dns_type,
            'page': page
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_dns_history(self, domain: str, dns_type: str, page: int = 1) -> Optional[Dict[Any, Any]]:
        """
        Get DNS history for a specified domain, including changes over a specified time range
        
        Args:
            domain: Domain to query, e.g., example.com
            dns_type: Type of DNS record to query, e.g., A, AAAA, MX, NS, SOA, TXT
            page: Page number for pagination, default is 1
        
        Returns:
            API response JSON data containing historical DNS records with DNS type, TTL, and raw text data
        """
        endpoint = "/search/dns/history"
        params = {
            'domain': domain,
            'type': dns_type,
            'page': page
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_subdomains(self, domain: str, page: int = 1) -> Optional[Dict[Any, Any]]:
        """
        Get subdomains information for a specified domain
        
        Args:
            domain: Domain to query, e.g., example.com
            page: Page number for pagination, default is 1
        
        Returns:
            API response JSON data containing subdomains with details such as IP address, organization, ISP, and country
        """
        endpoint = "/search/subdomains"
        params = {
            'domain': domain,
            'page': page
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_ip_blocks(self, domain: str) -> Optional[Dict[Any, Any]]:
        """
        Get IP blocks information associated with a specified domain
        
        Args:
            domain: Domain to query, e.g., example.com
        
        Returns:
            API response JSON data containing IP blocks with details about IP addresses, IP versions, and RDAP information
        """
        endpoint = "/search/ip/blocks"
        params = {
            'domain': domain
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_ip_detection(self, domain: str) -> Optional[Dict[Any, Any]]:
        """
        Get IP detection information for a specified domain
        
        Args:
            domain: Domain to query, e.g., example.com
        
        Returns:
            API response JSON data containing IP detection information with details such as IP addresses, ASN, country, ISP, location, and CDN status
        """
        endpoint = "/search/ip/detection"
        params = {
            'domain': domain
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_ssl_cert(self, domain: str) -> Optional[Dict[Any, Any]]:
        """
        Get SSL certificate information for a specified domain
        
        Args:
            domain: Domain to query, e.g., example.com
        
        Returns:
            API response JSON data containing detailed SSL certificate information including version, signature, fingerprints, issuer, subject, validity period, serial number, and cipher details
        """
        endpoint = "/search/ssl/cert"
        params = {
            'domain': domain
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_site_technologies(self, domain: str) -> Optional[Dict[Any, Any]]:
        """
        Get information about technologies used by a specified domain
        
        Args:
            domain: Domain to query, e.g., example.com
        
        Returns:
            API response JSON data containing technologies information with details such as category, website, description, and icon for each technology
        """
        endpoint = "/search/site/technologies"
        params = {
            'domain': domain
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_site_associated_domains(self, domain: str) -> Optional[Dict[Any, Any]]:
        """
        Get a list of domains associated with a specified domain
        
        Args:
            domain: Domain to query, e.g., example.com
        
        Returns:
            API response JSON data containing associated domains with information about organization and ISP
        """
        endpoint = "/search/site/associateddomains"
        params = {
            'domain': domain
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_scan_proxy(self) -> Optional[Dict[Any, Any]]:
        """
        Get a list of available proxy/tunnel servers with their current latency information
        
        Returns:
            API response JSON data containing proxy server information with id, name, and delay
        """
        endpoint = "/scan/getproxy"
        return self._request('GET', endpoint)
    
    def create_scan(self, address: str, comment: str, scan_type: str, proxyid: str, useragent: str = "Default") -> Optional[Dict[Any, Any]]:
        """
        Initiate a new scan for a specified address
        
        Args:
            address: The target address to scan, e.g., "https://example.com"
            comment: The comment to be used for the scan
            scan_type: Type of scan - "st.bi" (Crawl Only), "st.xss" (Cross-site Scripting), 
                      "st.si" (SQL Injection), "st.hmr" (Critical/High/Medium Risk), "st.fs" (Full-scan)
            proxyid: The unique identifier of the proxy to be used
            useragent: The user agent to be used, default is "Default"
        
        Returns:
            API response JSON data containing scan_id, server_id, and status
        """
        endpoint = "/scan/createscan"
        data = {
            'address': address,
            'comment': comment,
            'type': scan_type,
            'proxyid': proxyid,
            'useragent': useragent
        }
        
        return self._request('POST', endpoint, json=data)
    
    def get_scan_overview(self) -> Optional[Dict[Any, Any]]:
        """
        Get an overview of scan operations
        
        Returns:
            API response JSON data containing total number of scans, status of current scans, and vulnerability counts
        """
        endpoint = "/scan/overview"
        return self._request('GET', endpoint)
    
    def get_scan_scans(self, start_index: int = 0, limit: int = 100) -> Optional[Dict[Any, Any]]:
        """
        Get a list of scan results
        
        Args:
            start_index: The starting index for pagination, defaults to 0
            limit: The number of scan results to return, defaults to 100
        
        Returns:
            API response JSON data containing scan results with target address, scan status, and vulnerability counts
        """
        endpoint = "/scan/scans"
        params = {
            'c': start_index,
            'l': limit
        }
        
        return self._request('GET', endpoint, params=params)
    
    def stop_scan(self, scan_ids: list) -> Optional[Dict[Any, Any]]:
        """
        Stop an ongoing scan by providing the scan ID
        
        Args:
            scan_ids: An array of scan IDs to be stopped
        
        Returns:
            API response JSON data containing status message
        """
        endpoint = "/scan/stopscan"
        data = {
            'scan_id': scan_ids
        }
        
        return self._request('POST', endpoint, json=data)
    
    def get_scan_statistics(self, scan_id: str) -> Optional[Dict[Any, Any]]:
        """
        Get detailed statistics for a specific scan
        
        Args:
            scan_id: The unique identifier of the scan
        
        Returns:
            API response JSON data containing progress, status, vulnerabilities found, and other relevant information
        """
        endpoint = "/scan/statistics"
        params = {
            'scan_id': scan_id
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_scan_sitestructure(self, scan_id: str, directory_id: int = 0) -> Optional[Dict[Any, Any]]:
        """
        Get the structure of a website based on the specified directory ID
        
        Args:
            scan_id: The unique identifier for the scan
            directory_id: The ID of the directory to query, root directory is represented by 0, defaults to 0
        
        Returns:
            API response JSON data containing site structure with id, type, name, parent_id, and path
        """
        endpoint = "/scan/sitestructure"
        params = {
            'scan_id': scan_id,
            'id': directory_id
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_scan_vulnerabilities(self, scan_id: str, start_position: int = 0, limit: int = 100) -> Optional[Dict[Any, Any]]:
        """
        Get a list of vulnerabilities from scans
        
        Args:
            scan_id: The ID of the scan to query
            start_position: The starting position for the query, starts from 0, defaults to 0
            limit: The number of vulnerabilities to retrieve, defaults to 100
        
        Returns:
            API response JSON data containing vulnerabilities with name, url, parameter, severity, and id
        """
        endpoint = "/scan/vulnerabilities"
        params = {
            'scan_id': scan_id,
            'c': start_position,
            'l': limit
        }
        
        return self._request('GET', endpoint, params=params)
    
    def get_scan_vulnerabilitydetail(self, vlun_id: str) -> Optional[Dict[Any, Any]]:
        """
        Get detailed information about a specific vulnerability
        
        Args:
            vlun_id: The unique identifier for the vulnerability
        
        Returns:
            API response JSON data containing vulnerability details including name, affected details, severity, description, request/response data, and more
        """
        endpoint = "/scan/vulnerabilitydetail"
        params = {
            'vlun_id': vlun_id
        }
        
        return self._request('GET', endpoint, params=params)
    
    def delete_scan(self, scan_ids: list) -> Optional[Dict[Any, Any]]:
        """
        Delete a specific scan by its ID
        
        Args:
            scan_ids: An array of scan IDs to be deleted
        
        Returns:
            API response JSON data containing status message
        """
        endpoint = "/scan/deletescan"
        data = {
            'scan_id': scan_ids
        }
        
        return self._request('POST', endpoint, json=data)
