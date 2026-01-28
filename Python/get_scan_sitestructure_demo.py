"""
SecuritySurface API - Get Scan Site Structure Demo
Demonstrates how to use the API to get the structure of a website
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get site structure"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    scan_id = "1207526e-931f-4971-98f8-e08f167cdd45"  # Scan ID
    directory_id = 0  # Root directory ID (0 for root)
    
    # Get site structure
    structure_data = api_client.get_scan_sitestructure(scan_id=scan_id, directory_id=directory_id)
    
    if structure_data:
        print(json.dumps(structure_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve site structure"}, indent=2))


if __name__ == "__main__":
    main()
