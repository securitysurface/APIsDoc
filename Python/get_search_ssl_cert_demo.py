"""
SecuritySurface API - Get SSL Certificate Demo
Demonstrates how to use the API to get SSL certificate information for a domain
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get SSL certificate"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    domain = "example.com"  # Domain to query
    
    # Get SSL certificate
    ssl_cert_data = api_client.get_ssl_cert(domain=domain)
    
    if ssl_cert_data:
        print(json.dumps(ssl_cert_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve SSL certificate"}, indent=2))


if __name__ == "__main__":
    main()
