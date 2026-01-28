"""
SecuritySurface API - Get Scan Vulnerabilities Demo
Demonstrates how to use the API to get a list of vulnerabilities from scans
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to get scan vulnerabilities"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Query parameters
    scan_id = "1207526e-931f-4971-98f8-e08f167cdd66"  # Scan ID
    start_position = 0  # Starting position (starts from 0)
    limit = 100  # Number of vulnerabilities to retrieve
    
    # Get vulnerabilities
    vulnerabilities_data = api_client.get_scan_vulnerabilities(
        scan_id=scan_id,
        start_position=start_position,
        limit=limit
    )
    
    if vulnerabilities_data:
        print(json.dumps(vulnerabilities_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to retrieve vulnerabilities"}, indent=2))


if __name__ == "__main__":
    main()
