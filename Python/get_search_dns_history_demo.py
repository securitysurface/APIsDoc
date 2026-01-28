"""
SecuritySurface API - Get DNS History Demo
Demonstrates how to use the API to get DNS history for a domain
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get DNS history"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    domain = "example.com"  # Domain to query
    dns_type = "A"  # DNS record type: A, AAAA, MX, NS, SOA, TXT
    page = 1  # Page number
    
    # Get DNS history
    dns_history_data = api_client.get_dns_history(domain=domain, dns_type=dns_type, page=page)
    
    if dns_history_data:
        print(json.dumps(dns_history_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve DNS history"}, indent=2))


if __name__ == "__main__":
    main()
