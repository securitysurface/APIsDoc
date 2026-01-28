"""
SecuritySurface API - Get Scan Statistics Demo
Demonstrates how to use the API to get detailed statistics for a specific scan
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get scan statistics"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Scan ID
    scan_id = "1207526e-931f-4971-98f8-e08f167cdd45"
    
    # Get scan statistics
    statistics_data = api_client.get_scan_statistics(scan_id=scan_id)
    
    if statistics_data:
        print(json.dumps(statistics_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve scan statistics"}, indent=2))


if __name__ == "__main__":
    main()
