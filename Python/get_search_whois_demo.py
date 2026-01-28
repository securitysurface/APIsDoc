"""
SecuritySurface API - Get WHOIS Current Demo
Demonstrates how to use the API to get current WHOIS information for a domain
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get WHOIS current information"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Domain to query
    domain = "example.com"
    
    # Get WHOIS data
    whois_data = api_client.get_whois_current(domain=domain)
    
    if whois_data:
        print(json.dumps(whois_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve WHOIS data"}, indent=2))


if __name__ == "__main__":
    main()
