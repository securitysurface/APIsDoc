"""
SecuritySurface API - Stop Scan Demo
Demonstrates how to use the API to stop an ongoing scan
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to stop a scan"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Scan ID to stop
    scan_ids = ["1207526e-931f-4971-98f8-e08f167cdd45"]  # Array of scan IDs
    
    # Stop scan
    stop_data = api_client.stop_scan(scan_ids=scan_ids)
    
    if stop_data:
        print(json.dumps(stop_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to stop scan"}, indent=2))


if __name__ == "__main__":
    main()
