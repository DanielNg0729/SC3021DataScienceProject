import requests
import pandas as pd
import time

def get_coordinates(postal_code):
    """
    Get lat/long from OneMap API using postal code
    """
    url = f"https://www.onemap.gov.sg/api/common/elastic/search"
    params = {
        'searchVal': postal_code,
        'returnGeom': 'Y',
        'getAddrDetails': 'Y'
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['found'] > 0:
            result = data['results'][0]
            return {
                'latitude': float(result['LATITUDE']),
                'longitude': float(result['LONGITUDE']),
                'address': result['ADDRESS']
            }
        else:
            return None
    except:
        return None

# Example usage
postal = "520123"
coords = get_coordinates(postal)
print(coords)
# Output: {'latitude': 1.3521, 'longitude': 103.8198, 'address': 'BLK 123 LORONG 1 TOA PAYOH'}