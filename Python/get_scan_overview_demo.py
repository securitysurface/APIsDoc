"""
SecuritySurface API - Get Scan Overview Demo
Demonstrates how to use the API to get an overview of scan operations
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get scan overview"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Get scan overview
    overview_data = api_client.get_scan_overview()
    
    if overview_data:
        print(json.dumps(overview_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve scan overview"}, indent=2))


if __name__ == "__main__":
    main()
