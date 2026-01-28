"""
SecuritySurface API - Get Scan Scans Demo
Demonstrates how to use the API to get a list of scan results
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get scan results"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    start_index = 0  # Starting index for pagination
    limit = 100  # Number of scan results to return
    
    # Get scan results
    scans_data = api_client.get_scan_scans(start_index=start_index, limit=limit)
    
    if scans_data:
        print(json.dumps(scans_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve scan results"}, indent=2))


if __name__ == "__main__":
    main()
