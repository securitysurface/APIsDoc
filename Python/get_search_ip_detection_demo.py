"""
SecuritySurface API - Get IP Detection Demo
Demonstrates how to use the API to get IP detection information for a domain
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get IP detection"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    domain = "example.com"  # Domain to query
    
    # Get IP detection
    ip_detection_data = api_client.get_ip_detection(domain=domain)
    
    if ip_detection_data:
        print(json.dumps(ip_detection_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve IP detection"}, indent=2))


if __name__ == "__main__":
    main()
