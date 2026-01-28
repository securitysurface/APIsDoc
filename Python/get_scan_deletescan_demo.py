"""
SecuritySurface API - Delete Scan Demo
Demonstrates how to use the API to delete a specific scan
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to delete a scan"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Scan ID to delete
    scan_ids = ["1207526e-931f-4971-98f8-e08f167cdd45"]  # Array of scan IDs
    
    # Delete scan
    delete_data = api_client.delete_scan(scan_ids=scan_ids)
    
    if delete_data:
        print(json.dumps(delete_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to delete scan"}, indent=2))


if __name__ == "__main__":
    main()
