"""
Test script to verify your API keys are working correctly.
Run this before using the main application.
"""

import os
import requests
import sys

def test_google_places_api(api_key):
    """Test Google Places API"""
    print("Testing Google Places API...")
    
    if not api_key:
        print("❌ Google Places API key not found!")
        return False
    
    try:
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {
            'query': 'technology companies in Toronto',
            'key': api_key
        }
        
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if data.get('status') == 'OK':
            results = data.get('results', [])
            print(f"✅ Google Places API is working! Found {len(results)} test results.")
            if results:
                print(f"   Example: {results[0].get('name', 'N/A')}")
            return True
        elif data.get('status') == 'REQUEST_DENIED':
            print(f"❌ Google Places API Error: {data.get('error_message', 'Invalid API key')}")
            return False
        elif data.get('status') == 'OVER_QUERY_LIMIT':
            print("⚠️  Google Places API: Quota exceeded. Wait 24 hours or upgrade plan.")
            return False
        else:
            print(f"⚠️  Google Places API Status: {data.get('status')}")
            print(f"   Message: {data.get('error_message', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Google Places API: {e}")
        return False

def test_yelp_api(api_key):
    """Test Yelp API"""
    print("\nTesting Yelp API...")
    
    if not api_key:
        print("⚠️  Yelp API key not set (optional)")
        return None
    
    try:
        url = "https://api.yelp.com/v3/businesses/search"
        headers = {
            'Authorization': f'Bearer {api_key}'
        }
        params = {
            'term': 'technology',
            'location': 'Toronto',
            'limit': 5
        }
        
        response = requests.get(url, headers=headers, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            businesses = data.get('businesses', [])
            print(f"✅ Yelp API is working! Found {len(businesses)} test results.")
            if businesses:
                print(f"   Example: {businesses[0].get('name', 'N/A')}")
            return True
        elif response.status_code == 401:
            print("❌ Yelp API Error: Invalid API key")
            return False
        else:
            print(f"⚠️  Yelp API Error: Status code {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Yelp API: {e}")
        return False

def main():
    print("=" * 50)
    print("  API Keys Test Script")
    print("=" * 50)
    print()
    
    # Try to load from config.py first
    try:
        from config import GOOGLE_PLACES_API_KEY, YELP_API_KEY
        print("✓ Loaded API keys from config.py")
    except ImportError:
        print("⚠️  config.py not found, checking environment variables...")
        GOOGLE_PLACES_API_KEY = os.environ.get('GOOGLE_PLACES_API_KEY', '')
        YELP_API_KEY = os.environ.get('YELP_API_KEY', '')
    
    print()
    
    # Test Google Places API (required)
    google_ok = test_google_places_api(GOOGLE_PLACES_API_KEY)
    
    # Test Yelp API (optional)
    yelp_ok = test_yelp_api(YELP_API_KEY)
    
    print()
    print("=" * 50)
    print("  Test Summary")
    print("=" * 50)
    
    if google_ok:
        print("✅ Google Places API: WORKING")
    else:
        print("❌ Google Places API: NOT WORKING (REQUIRED)")
        print("   Please check your API key and try again.")
        sys.exit(1)
    
    if yelp_ok is None:
        print("⚠️  Yelp API: Not configured (optional)")
    elif yelp_ok:
        print("✅ Yelp API: WORKING")
    else:
        print("⚠️  Yelp API: NOT WORKING (optional, but recommended)")
    
    print()
    print("=" * 50)
    if google_ok:
        print("✅ Your setup is ready! You can run the application now.")
        print("   Run: python app.py")
    else:
        print("❌ Please fix the issues above before running the application.")
    print("=" * 50)

if __name__ == '__main__':
    main()

