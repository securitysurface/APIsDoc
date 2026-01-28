"""
SecuritySurface API - Get DNS Current Demo
Demonstrates how to use the API to get current DNS records for a domain
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get current DNS records"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Domain to query
    domain = "example.com"
    
    # Get DNS records
    dns_data = api_client.get_dns_current(domain=domain)
    
    if dns_data:
        print(json.dumps(dns_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve DNS records"}, indent=2))


if __name__ == "__main__":
    main()
