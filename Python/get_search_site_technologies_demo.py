"""
SecuritySurface API - Get Site Technologies Demo
Demonstrates how to use the API to get technologies information for a domain
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get site technologies"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    domain = "example.com"  # Domain to query
    
    # Get site technologies
    site_technologies_data = api_client.get_site_technologies(domain=domain)
    
    if site_technologies_data:
        print(json.dumps(site_technologies_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve site technologies"}, indent=2))


if __name__ == "__main__":
    main()
