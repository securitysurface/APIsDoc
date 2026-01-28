"""
SecuritySurface API - Create Scan Demo
Demonstrates how to use the API to initiate a new scan for a specified address
"""

import json
from securitysurface_api import SecuritySurfaceAPI


def main():
    """Main function - demonstrates how to use the API to create a scan"""
    
    # API key
    API_KEY = "HZCeQgAT1xKl3rk0yZokpd8AwXNmSS22fifoLc0OxnLTmzusI9sJJIcRh8Bqdy6m"
    
    # Create API client instance
    api_client = SecuritySurfaceAPI(api_key=API_KEY)
    
    # Scan parameters
    address = "http://"  # Target address to scan
    comment = "this is a example"  # Comment for the scan
    scan_type = "st.fs"  # Scan type: st.bi, st.xss, st.si, st.hmr, st.fs
    proxyid = "25"  # Proxy ID to use
    useragent = "Default"  # User agent to use
    
    # Create scan
    scan_data = api_client.create_scan(
        address=address,
        comment=comment,
        scan_type=scan_type,
        proxyid=proxyid,
        useragent=useragent
    )
    
    if scan_data:
        print(json.dumps(scan_data, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Failed to create scan"}, indent=2))


if __name__ == "__main__":
    main()
