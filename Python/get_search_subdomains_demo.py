"""
SecuritySurface API - Get Subdomains Demo
Demonstrates how to use the API to get subdomains information for a domain
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get subdomains"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    domain = "example.com"  # Domain to query
    page = 1  # Page number
    
    # Get subdomains
    subdomains_data = api_client.get_subdomains(domain=domain, page=page)
    
    if subdomains_data:
        print(json.dumps(subdomains_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve subdomains"}, indent=2))


if __name__ == "__main__":
    main()
