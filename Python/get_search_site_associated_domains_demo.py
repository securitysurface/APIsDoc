"""
SecuritySurface API - Get Site Associated Domains Demo
Demonstrates how to use the API to get associated domains information for a domain
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get site associated domains"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    domain = "example.com"  # Domain to query
    
    # Get site associated domains
    associated_domains_data = api_client.get_site_associated_domains(domain=domain)
    
    if associated_domains_data:
        print(json.dumps(associated_domains_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve associated domains"}, indent=2))


if __name__ == "__main__":
    main()
