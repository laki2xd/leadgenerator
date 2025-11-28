"""
Quick verification script to test your API key setup
"""
import os
import sys

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

print("=" * 60)
print("  Verifying API Key Setup")
print("=" * 60)
print()

# Try to load from config.py
try:
    from config import GOOGLE_PLACES_API_KEY, YELP_API_KEY
    print("[OK] Found config.py")
    print(f"[OK] Google Places API Key: {'Set' if GOOGLE_PLACES_API_KEY else 'NOT SET'}")
    print(f"[OK] Yelp API Key: {'Set' if YELP_API_KEY else 'NOT SET (optional)'}")
    print()
except ImportError:
    print("[WARNING] config.py not found, checking environment variables...")
    GOOGLE_PLACES_API_KEY = os.environ.get('GOOGLE_PLACES_API_KEY', '')
    YELP_API_KEY = os.environ.get('YELP_API_KEY', '')
    if GOOGLE_PLACES_API_KEY:
        print("[OK] Found Google Places API Key in environment")
    else:
        print("[ERROR] No API keys found!")
        sys.exit(1)

if not GOOGLE_PLACES_API_KEY:
    print("[ERROR] Google Places API key is required!")
    print("   Please create config.py with your API key")
    sys.exit(1)

# Test the API key
print("Testing Google Places API...")
try:
    import requests
    
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': 'technology companies in Toronto',
        'key': GOOGLE_PLACES_API_KEY
    }
    
    response = requests.get(url, params=params, timeout=10)
    data = response.json()
    
    if data.get('status') == 'OK':
        results = data.get('results', [])
        print(f"[SUCCESS] API key is working!")
        print(f"   Found {len(results)} test results")
        if results:
            print(f"   Example company: {results[0].get('name', 'N/A')}")
        print()
        print("=" * 60)
        print("  [SUCCESS] Your setup is ready!")
        print("=" * 60)
        print()
        print("You can now run the application:")
        print("  python app.py")
        print()
        print("Then open http://localhost:5000 in your browser")
    elif data.get('status') == 'REQUEST_DENIED':
        print(f"[ERROR] {data.get('error_message', 'Invalid API key')}")
        print()
        print("Please check:")
        print("  1. Your API key is correct")
        print("  2. Places API is enabled in Google Cloud Console")
        print("  3. Billing is set up (Google gives $200/month free)")
        sys.exit(1)
    elif data.get('status') == 'OVER_QUERY_LIMIT':
        print("[WARNING] API quota exceeded")
        print("   Wait 24 hours or upgrade your Google Cloud plan")
    else:
        print(f"[WARNING] Status: {data.get('status')}")
        print(f"   Message: {data.get('error_message', 'Unknown error')}")
        
except ImportError:
    print("[ERROR] 'requests' library not installed")
    print("   Run: python -m pip install requests")
    sys.exit(1)
except Exception as e:
    print(f"[ERROR] {e}")
    sys.exit(1)

