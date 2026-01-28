"""
SecuritySurface API - Get SUMMARY Demo
Demonstrates how to use the API to get security summary information for a domain
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get SUMMARY"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Domain to query
    domain = "example.com"
    
    # Get SUMMARY data
    summary_data = api_client.get_summary(domain=domain)
    
    if summary_data:
        print(json.dumps(summary_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve SUMMARY"}, indent=2))


if __name__ == "__main__":
    main()
