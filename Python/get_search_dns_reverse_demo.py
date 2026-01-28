"""
SecuritySurface API - Get DNS Reverse Demo
Demonstrates how to use the API to get reverse DNS lookup information
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get reverse DNS lookup information"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    domain = "8.8.8.8"  # IP address or domain
    dns_type = "a"  # DNS record type: a, aaaa, mx, ns, soa, txt
    page = 1  # Page number
    
    # Get reverse DNS records
    reverse_dns_data = api_client.get_dns_reverse(domain=domain, dns_type=dns_type, page=page)
    
    if reverse_dns_data:
        print(json.dumps(reverse_dns_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve reverse DNS records"}, indent=2))


if __name__ == "__main__":
    main()
