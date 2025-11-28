from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import requests
import pandas as pd
import os
import json
from datetime import datetime
import time
import re
from urllib.parse import urljoin, urlparse
from threading import Lock
import signal
# Load environment variables from .env file (for local development)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, that's OK - use environment variables or config.py
    pass

# Global progress tracking
progress_lock = Lock()
current_progress = {
    'status': 'idle',
    'current_step': '',
    'companies_found': 0,
    'total_steps': 0,
    'current_step_num': 0,
    'details': []
}

# Search history file path
HISTORY_FILE = 'search_history.json'
history_lock = Lock()
MAX_HISTORY_ITEMS = 1000  # Maximum items to store globally

def update_progress(status, step, companies=0, detail=''):
    """Update progress tracking"""
    global current_progress
    with progress_lock:
        current_progress['status'] = status
        current_progress['current_step'] = step
        current_progress['companies_found'] = companies
        if detail:
            current_progress['details'].append({
                'time': datetime.now().strftime('%H:%M:%S'),
                'message': detail
            })
            # Keep only last 50 details
            if len(current_progress['details']) > 50:
                current_progress['details'] = current_progress['details'][-50:]

def get_search_history():
    """Read search history from file"""
    try:
        if os.path.exists(HISTORY_FILE):
            with history_lock:
                with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
        return []
    except Exception as e:
        print(f'Error reading search history: {e}')
        return []

def save_search_history(history):
    """Save search history to file"""
    try:
        with history_lock:
            # Ensure directory exists
            os.makedirs(os.path.dirname(HISTORY_FILE) if os.path.dirname(HISTORY_FILE) else '.', exist_ok=True)
            with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f'Error saving search history: {e}')

def add_to_history(search_type, query, industry_filter=''):
    """Add a search to history"""
    history = get_search_history()
    new_item = {
        'id': int(time.time() * 1000),  # Use timestamp as ID
        'type': search_type,
        'query': query.strip(),
        'industry_filter': industry_filter.strip(),
        'timestamp': datetime.now().isoformat()
    }
    
    # Remove duplicates (same type and query)
    history = [item for item in history 
               if not (item.get('type') == search_type and 
                      item.get('query', '').lower() == query.strip().lower())]
    
    # Add new item at the beginning
    history.insert(0, new_item)
    
    # Keep only last MAX_HISTORY_ITEMS
    history = history[:MAX_HISTORY_ITEMS]
    
    save_search_history(history)

app = Flask(__name__)
CORS(app)

# Configuration - Users should add their API keys here
# Try to load from config.py first, then environment variables
try:
    from config import GOOGLE_PLACES_API_KEY, YELP_API_KEY, CLEARBIT_API_KEY, ZOOMINFO_API_KEY, APOLLO_API_KEY
except ImportError:
    GOOGLE_PLACES_API_KEY = os.environ.get('GOOGLE_PLACES_API_KEY', '')
    YELP_API_KEY = os.environ.get('YELP_API_KEY', '')
    CLEARBIT_API_KEY = os.environ.get('CLEARBIT_API_KEY', '')
    ZOOMINFO_API_KEY = os.environ.get('ZOOMINFO_API_KEY', '')
    APOLLO_API_KEY = os.environ.get('APOLLO_API_KEY', '')

# Business types to EXCLUDE (retail stores, small shops, etc.)
EXCLUDED_TYPES = [
    'restaurant', 'cafe', 'coffee_shop', 'bakery', 'food',
    'clothing_store', 'shoe_store', 'jewelry_store', 'book_store',
    'convenience_store', 'supermarket', 'grocery_or_supermarket',
    'hair_care', 'beauty_salon', 'spa', 'gym', 'fitness_center',
    'gas_station', 'pharmacy', 'drugstore', 'bank', 'atm',
    'real_estate_agency', 'travel_agency', 'tourist_attraction',
    'store', 'shopping_mall', 'department_store'
]

# Business types to PRIORITIZE (companies needing transportation)
PRIORITY_TYPES = [
    'manufacturing', 'factory', 'warehouse', 'distribution',
    'logistics', 'freight', 'shipping', 'transportation',
    'wholesale', 'industrial', 'construction', 'mining',
    'agriculture', 'farm', 'processing', 'assembly'
]

# Keywords that indicate transportation/logistics needs
TRANSPORTATION_KEYWORDS = [
    'manufacturing', 'factory', 'warehouse', 'distribution',
    'logistics', 'freight', 'shipping', 'transport',
    'wholesale', 'industrial', 'construction', 'mining',
    'agriculture', 'farm', 'processing', 'assembly',
    'supply chain', 'fulfillment', 'storage', 'cargo',
    'import', 'export', 'trucking', 'delivery'
]

def is_transportation_relevant_company(place_data, company_name='', address=''):
    """Check if a company is relevant for transportation services"""
    # Get business types from place data
    types = place_data.get('types', [])
    business_status = place_data.get('business_status', '')
    
    # Exclude if it's in excluded types
    for excluded_type in EXCLUDED_TYPES:
        if excluded_type in types:
            return False
    
    # Check if it's a priority type
    for priority_type in PRIORITY_TYPES:
        if priority_type in types:
            return True
    
    # Check company name and address for transportation keywords
    name_lower = company_name.lower()
    address_lower = address.lower()
    combined_text = f"{name_lower} {address_lower}"
    
    for keyword in TRANSPORTATION_KEYWORDS:
        if keyword in combined_text:
            return True
    
    # Exclude small retail stores (check for common retail indicators)
    retail_indicators = ['store', 'shop', 'retail', 'outlet', 'mall']
    if any(indicator in name_lower for indicator in retail_indicators):
        # But allow if it's wholesale or distribution
        if 'wholesale' not in name_lower and 'distribution' not in name_lower:
            return False
    
    # If business status is not operational, exclude
    if business_status and business_status != 'OPERATIONAL':
        return False
    
    # Default: include if it's a business establishment
    return 'establishment' in types or 'point_of_interest' in types

def search_google_places(industry, location, max_results=50, search_context='', timeout_seconds=25):
    """Search for companies using Google Places API with progress tracking"""
    companies = []
    start_time = time.time()
    
    if not GOOGLE_PLACES_API_KEY:
        return companies
    
    try:
        # Reduce max_results to avoid timeout (Render free tier has 30s limit)
        max_results = min(max_results, 30)  # Limit to 30 to stay under timeout
        
        # Search in multiple locations
        locations = ['Canada', 'United States']
        results_per_location = max_results // 2
        
        update_progress('searching', f'Searching Google Places in {locations[0]}...', len(companies))
        
        for idx, loc in enumerate(locations):
            query = f"{industry} companies in {loc}" if not search_context else f"{industry} in {loc}"
            update_progress('searching', f'Searching {loc}... ({idx+1}/{len(locations)})', len(companies), f'Query: {query}')
            
            # Use Text Search API with timeout
            url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
            params = {
                'query': query,
                'key': GOOGLE_PLACES_API_KEY,
                'type': 'establishment'
            }
            
            try:
                response = requests.get(url, params=params, timeout=10)
                data = response.json()
            except requests.Timeout:
                update_progress('warning', 'timeout', len(companies), f'Timeout searching {loc}, skipping...')
                continue
            
            if data.get('status') == 'OK':
                places = data.get('results', [])[:results_per_location]
                update_progress('processing', f'Processing {len(places)} results from {loc}...', len(companies))
                
                # Check timeout before processing places
                elapsed_total = time.time() - start_time
                if elapsed_total > timeout_seconds:
                    print(f"Timeout warning: {elapsed_total:.1f}s elapsed, stopping search")
                    update_progress('warning', 'timeout', len(companies), f'Stopping search to avoid timeout ({elapsed_total:.1f}s)')
                    break
                
                # Limit places to process to avoid timeout
                places_to_process = min(len(places), 15)  # Process max 15 per location
                
                for place_idx, place in enumerate(places[:places_to_process]):
                    # Check timeout during processing
                    if time.time() - start_time > timeout_seconds:
                        print(f"Timeout during processing, stopping at {place_idx}/{places_to_process}")
                        break
                    
                    # Filter out retail stores and small shops
                    if not is_transportation_relevant_company(
                        place, 
                        place.get('name', ''), 
                        place.get('formatted_address', '')
                    ):
                        continue
                    
                    place_id = place.get('place_id', '')
                    company_name = place.get('name', '')
                    
                    # Skip detail fetching to save time - use data from search results
                    # This is the main bottleneck causing timeout
                    update_progress('processing', f'Processing: {company_name[:40]}...', len(companies))
                    
                    # Use data from search results directly (faster)
                    # Only fetch details if we have time
                    company_details = {}
                    if time.time() - start_time < timeout_seconds - 3:  # Leave 3s buffer
                        try:
                            company_details = get_place_details(place_id, timeout=2)  # Reduced timeout
                        except:
                            pass  # Use basic data if details fail
                    
                    # Determine industry field based on search context
                    industry_field = search_context if search_context else industry
                    
                    company = {
                        'name': company_name,
                        'address': place.get('formatted_address', ''),
                        'phone': company_details.get('phone', place.get('formatted_phone_number', '')),
                        'email': company_details.get('email', ''),
                        'website': company_details.get('website', place.get('website', '')),
                        'rating': place.get('rating', ''),
                        'country': loc,
                        'industry': industry_field,
                        'place_id': place_id,
                        'business_type': ', '.join([t for t in place.get('types', []) if t not in ['point_of_interest', 'establishment']][:3])
                    }
                    companies.append(company)
                    update_progress('found', f'Found: {company_name[:40]}...', len(companies))
                    
                    # Early return if we have enough companies
                    if len(companies) >= 20:  # Return early with 20 companies
                        print(f"Found enough companies ({len(companies)}), returning early")
                        break
            
            elif data.get('status') == 'OVER_QUERY_LIMIT':
                update_progress('error', 'quota', len(companies), f'API quota exceeded for {loc}')
            elif data.get('status') == 'REQUEST_DENIED':
                update_progress('error', 'denied', len(companies), f'Request denied for {loc}: {data.get("error_message", "")}')
            
            time.sleep(0.2)  # Rate limiting
            
    except Exception as e:
        update_progress('error', 'exception', len(companies), f'Error: {str(e)[:50]}')
    
    update_progress('completed', 'Google Places search completed', len(companies), f'Found {len(companies)} companies')
    return companies

def get_place_details(place_id, timeout=5):
    """Get detailed information about a place including contact info with timeout"""
    details = {
        'phone': '',
        'email': '',
        'website': ''
    }
    
    if not place_id or not GOOGLE_PLACES_API_KEY:
        return details
    
    try:
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_params = {
            'place_id': place_id,
            'key': GOOGLE_PLACES_API_KEY,
            'fields': 'formatted_phone_number,international_phone_number,website,email,opening_hours'
        }
        
        # Use timeout to prevent hanging - skip if takes more than 5 seconds
        start_time = time.time()
        response = requests.get(details_url, params=details_params, timeout=timeout)
        elapsed = time.time() - start_time
        
        if elapsed > 4.5:
            update_progress('warning', 'slow', detail=f'Slow API response ({elapsed:.1f}s)')
        
        details_data = response.json()
        
        if details_data.get('status') == 'OK':
            result = details_data.get('result', {})
            details['phone'] = result.get('formatted_phone_number', result.get('international_phone_number', ''))
            details['website'] = result.get('website', '')
            
            # Google Places API doesn't provide email directly, so try to extract from website
            if details['website']:
                email = extract_email_from_website(details['website'])
                if email:
                    details['email'] = email
                else:
                    details['email'] = ''
            else:
                details['email'] = ''
        
        time.sleep(0.1)  # Rate limiting
        
    except requests.Timeout:
        update_progress('warning', 'timeout', detail=f'Timeout getting details (>{timeout}s), skipping...')
        return details
    except Exception as e:
        update_progress('warning', 'error', detail=f'Error getting place details: {str(e)[:50]}')
    
    return details

def extract_email_from_website(url):
    """Try to extract email from website contact page"""
    try:
        if not url or not url.startswith('http'):
            return ''
        
        # Common contact page URLs
        contact_urls = [
            urljoin(url, '/contact'),
            urljoin(url, '/contact-us'),
            urljoin(url, '/contact.html'),
            urljoin(url, '/about/contact'),
        ]
        
        # Try to fetch contact page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        for contact_url in contact_urls[:2]:  # Limit to first 2 attempts
            try:
                response = requests.get(contact_url, headers=headers, timeout=5, allow_redirects=True)
                if response.status_code == 200:
                    # Look for email patterns in the HTML
                    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    emails = re.findall(email_pattern, response.text)
                    
                    # Filter out common non-business emails
                    filtered_emails = [e for e in emails if not any(
                        x in e.lower() for x in ['example.com', 'test.com', 'placeholder', 'noreply', 'no-reply']
                    )]
                    
                    if filtered_emails:
                        return filtered_emails[0]  # Return first valid email
            except:
                continue
        
        return ''
        
    except Exception as e:
        print(f"Error extracting email: {e}")
        return ''

def search_yelp(industry, location, max_results=50):
    """Search for companies using Yelp API"""
    companies = []
    
    if not YELP_API_KEY:
        return companies
    
    try:
        headers = {
            'Authorization': f'Bearer {YELP_API_KEY}'
        }
        
        locations = ['CA', 'US']
        results_per_location = max_results // 2
        
        for loc in locations:
            url = "https://api.yelp.com/v3/businesses/search"
            params = {
                'term': industry,
                'location': loc,
                'limit': min(results_per_location, 50),
                'sort_by': 'rating'
            }
            
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            
            if 'businesses' in data:
                for business in data.get('businesses', []):
                    # Try to get more details from Yelp if available
                    business_id = business.get('id', '')
                    yelp_details = get_yelp_business_details(business_id) if business_id else {}
                    
                    company = {
                        'name': business.get('name', ''),
                        'address': ', '.join(business.get('location', {}).get('display_address', [])),
                        'phone': business.get('phone', '') or yelp_details.get('phone', ''),
                        'email': yelp_details.get('email', ''),
                        'website': business.get('url', '') or yelp_details.get('website', ''),
                        'rating': business.get('rating', ''),
                        'country': 'Canada' if loc == 'CA' else 'United States',
                        'industry': industry,
                        'place_id': business_id
                    }
                    companies.append(company)
            
            time.sleep(0.2)  # Rate limiting
            
    except Exception as e:
        print(f"Error in Yelp search: {e}")
    
    return companies

def get_yelp_business_details(business_id):
    """Get detailed information from Yelp API"""
    details = {
        'phone': '',
        'email': '',
        'website': ''
    }
    
    if not business_id or not YELP_API_KEY:
        return details
    
    try:
        url = f"https://api.yelp.com/v3/businesses/{business_id}"
        headers = {
            'Authorization': f'Bearer {YELP_API_KEY}'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            details['phone'] = data.get('phone', '')
            details['website'] = data.get('url', '')
            # Yelp API doesn't provide email directly
        
        time.sleep(0.1)  # Rate limiting
        
    except Exception as e:
        print(f"Error getting Yelp business details: {e}")
    
    return details

def search_google_places_nearby(industry, location, max_results=50):
    """Search using Nearby Search API for better results"""
    companies = []
    
    if not GOOGLE_PLACES_API_KEY:
        return companies
    
    try:
        # Major cities in Canada and USA
        cities = [
            {'lat': 43.6532, 'lng': -79.3832, 'name': 'Toronto, Canada'},
            {'lat': 45.5017, 'lng': -73.5673, 'name': 'Montreal, Canada'},
            {'lat': 49.2827, 'lng': -123.1207, 'name': 'Vancouver, Canada'},
            {'lat': 40.7128, 'lng': -74.0060, 'name': 'New York, USA'},
            {'lat': 34.0522, 'lng': -118.2437, 'name': 'Los Angeles, USA'},
            {'lat': 41.8781, 'lng': -87.6298, 'name': 'Chicago, USA'},
            {'lat': 29.7604, 'lng': -95.3698, 'name': 'Houston, USA'},
            {'lat': 37.7749, 'lng': -122.4194, 'name': 'San Francisco, USA'},
        ]
        
        results_per_city = max_results // len(cities)
        
        for city in cities:
            # Focus on transportation-relevant industries
            # Modify query to prioritize B2B companies
            query_terms = []
            if industry.lower() not in TRANSPORTATION_KEYWORDS:
                # Add transportation-related terms to the query
                query_terms.append(f"{industry} manufacturing")
                query_terms.append(f"{industry} distribution")
                query_terms.append(f"{industry} warehouse")
            else:
                query_terms.append(f"{industry}")
            
            # Use the first query term
            query = f"{query_terms[0]} in {city['name']}"
            
            # First, find places using text search
            url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
            params = {
                'query': query,
                'key': GOOGLE_PLACES_API_KEY,
                'type': 'establishment'
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            if data.get('status') == 'OK':
                for place in data.get('results', [])[:results_per_city]:
                    # Filter out retail stores and small shops
                    if not is_transportation_relevant_company(
                        place,
                        place.get('name', ''),
                        place.get('formatted_address', '')
                    ):
                        continue
                    
                    # Get detailed information
                    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
                    details_params = {
                        'place_id': place.get('place_id'),
                        'key': GOOGLE_PLACES_API_KEY,
                        'fields': 'name,formatted_address,formatted_phone_number,website,rating,business_status,types'
                    }
                    
                    details_response = requests.get(details_url, params=details_params)
                    details_data = details_response.json()
                    
                    if details_data.get('status') == 'OK':
                        place_details = details_data.get('result', {})
                        
                        # Determine country
                        address = place_details.get('formatted_address', '')
                        country = 'Canada' if 'Canada' in address or city['name'].endswith('Canada') else 'United States'
                        
                        # Get email if available
                        email = place_details.get('email', '')
                        if not email and place_details.get('website'):
                            email = extract_email_from_website(place_details.get('website'))
                        
                        company = {
                            'name': place_details.get('name', ''),
                            'address': address,
                            'phone': place_details.get('formatted_phone_number', place_details.get('international_phone_number', '')),
                            'email': email,
                            'website': place_details.get('website', ''),
                            'rating': place_details.get('rating', ''),
                            'country': country,
                            'industry': industry,
                            'place_id': place.get('place_id', ''),
                            'business_type': ', '.join([t for t in place_details.get('types', []) if t not in ['point_of_interest', 'establishment']][:3])
                        }
                        companies.append(company)
            
            time.sleep(0.3)  # Rate limiting
            
    except Exception as e:
        print(f"Error in Google Places nearby search: {e}")
    
    return companies

def search_clearbit_api(industry, location, max_results=50):
    """Search for companies using Clearbit API (if available)"""
    companies = []
    
    if not CLEARBIT_API_KEY:
        return companies
    
    try:
        # Clearbit API endpoint for company search
        # Note: Clearbit works differently - it searches by domain
        # This is a placeholder for future integration
        # You'd need to use their company search API differently
        pass
    except Exception as e:
        print(f"Error in Clearbit search: {e}")
    
    return companies

def search_zoominfo_api(industry, location, max_results=50):
    """Search for companies using ZoomInfo API (if available)"""
    companies = []
    
    if not ZOOMINFO_API_KEY:
        return companies
    
    try:
        # ZoomInfo API endpoint
        # Note: Requires API key and specific endpoint
        # This is a placeholder for future integration
        pass
    except Exception as e:
        print(f"Error in ZoomInfo search: {e}")
    
    return companies

def search_apollo_api(industry, location, max_results=50, search_type='industry', product=''):
    """Search for companies using Apollo.io API"""
    companies = []
    
    if not APOLLO_API_KEY:
        return companies
    
    try:
        # Apollo.io API endpoint for searching organizations
        url = "https://api.apollo.io/v1/organizations/search"
        
        # Apollo uses HTTP Basic Auth - API key as username, 'X' as password
        auth = (APOLLO_API_KEY, 'X')
        
        # Determine location codes
        location_codes = []
        if 'canada' in location.lower() or 'north america' in location.lower():
            location_codes.append('Canada')
        if 'usa' in location.lower() or 'united states' in location.lower() or 'north america' in location.lower():
            location_codes.append('United States')
        
        # Build search query based on search type
        if search_type == 'product' and product:
            # Product-based search - look for manufacturers
            search_query = f"{product} manufacturer OR {product} manufacturing OR {product} factory"
        else:
            # Industry-based search
            search_query = industry
            if industry.lower() not in TRANSPORTATION_KEYWORDS:
                # Add transportation modifiers
                search_query = f"{industry} manufacturing OR {industry} distribution OR {industry} warehouse OR {industry} logistics"
        
        # Prepare request payload
        payload = {
            'api_key': APOLLO_API_KEY,
            'q_keywords': search_query,
            'page': 1,
            'per_page': min(max_results, 25),  # Apollo limits per page
            'organization_locations': location_codes,
            # Filter for companies that need transportation
            'organization_keywords': ['manufacturing', 'warehouse', 'distribution', 'logistics', 'freight', 'wholesale', 'industrial'],
            'organization_num_employees_ranges': ['1,10', '11,50', '51,200', '201,500', '501,1000', '1001,5000', '5001,10000', '10001,'],
            # Exclude retail and small shops
            'exclude_organization_keywords': ['restaurant', 'cafe', 'retail store', 'shop', 'salon', 'spa', 'gym'],
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache'
        }
        
        response = requests.post(url, json=payload, headers=headers, auth=auth, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            organizations = data.get('organizations', [])
            
            for org in organizations:
                # Filter out retail stores
                org_name = org.get('name', '').lower()
                if any(excluded in org_name for excluded in ['restaurant', 'cafe', 'retail', 'shop', 'store']):
                    # Skip unless it's wholesale or distribution
                    if 'wholesale' not in org_name and 'distribution' not in org_name:
                        continue
                
                # Get location info
                locations = org.get('organization_raw_addresses', [])
                address = ''
                country = 'United States'
                
                if locations:
                    primary_location = locations[0]
                    address_parts = []
                    if primary_location.get('street_address'):
                        address_parts.append(primary_location['street_address'])
                    if primary_location.get('city'):
                        address_parts.append(primary_location['city'])
                    if primary_location.get('state'):
                        address_parts.append(primary_location['state'])
                    if primary_location.get('postal_code'):
                        address_parts.append(primary_location['postal_code'])
                    address = ', '.join(address_parts)
                    
                    country = primary_location.get('country', 'United States')
                
                # Get contact info
                phone = org.get('phone_numbers', [{}])[0].get('raw_number', '') if org.get('phone_numbers') else ''
                website = org.get('website_url', '')
                email = org.get('email', '')
                
                # Get industry/type
                industry_tags = org.get('industry', '')
                if isinstance(industry_tags, list):
                    industry_tags = ', '.join(industry_tags[:3])
                
                # Determine industry field
                industry_field = industry if search_type == 'industry' else (product + ' manufacturer')
                
                company = {
                    'name': org.get('name', ''),
                    'address': address,
                    'phone': phone,
                    'email': email,
                    'website': website,
                    'rating': '',
                    'country': country,
                    'industry': industry_field,
                    'place_id': org.get('id', ''),
                    'business_type': industry_tags or 'B2B Company',
                    'employee_count': org.get('estimated_num_employees', ''),
                    'revenue': org.get('estimated_annual_revenue', '')
                }
                
                # Only add if it's transportation-relevant
                if is_transportation_relevant_company(
                    {'types': org.get('industry', [])},
                    company['name'],
                    company['address']
                ):
                    companies.append(company)
        
        elif response.status_code == 401:
            print("Apollo API: Authentication failed. Check your API key.")
        elif response.status_code == 429:
            print("Apollo API: Rate limit exceeded. Please wait.")
        else:
            print(f"Apollo API Error: Status {response.status_code} - {response.text[:200]}")
        
        time.sleep(0.5)  # Rate limiting for Apollo
        
    except Exception as e:
        print(f"Error in Apollo API search: {e}")
        import traceback
        traceback.print_exc()
    
    return companies

def search_product_manufacturers(product, industry_filter=''):
    """Search for companies that manufacture a specific product"""
    companies = []
    
    # Build search queries for product manufacturers
    if industry_filter:
        search_terms = [
            f"{product} manufacturer {industry_filter}",
            f"{product} manufacturing {industry_filter}",
            f"{product} factory {industry_filter}",
            f"{product} production {industry_filter}"
        ]
    else:
        # Auto-detect - try common manufacturing terms
        search_terms = [
            f"{product} manufacturer",
            f"{product} manufacturing",
            f"{product} factory",
            f"{product} production",
            f"{product} maker",
            f"{product} producer"
        ]
    
    update_progress('searching', f'Searching for manufacturers of: {product}', 0, f'Looking for companies that make {product}...')
    
    # Search each term
    for term in search_terms[:3]:  # Limit to first 3 terms
        update_progress('searching', f'Searching: {term}...', len(companies), f'Query: {term}')
        # Pass product as search_context so industry field is set correctly
        google_companies = search_google_places(term, 'North America', 30, search_context=f"{product} manufacturer")
        companies.extend(google_companies)
        update_progress('found', f'Found {len(google_companies)} companies for "{term}"', len(companies))
    
    return companies

def get_companies_from_directories(industry, search_type='industry', product='', industry_filter=''):
    """Get companies from multiple sources, filtered for transportation needs"""
    companies = []
    
    if search_type == 'product' and product:
        # Product-based search
        update_progress('searching', f'Searching for manufacturers of: {product}', 0, 'Starting product manufacturer search...')
        product_companies = search_product_manufacturers(product, industry_filter)
        companies.extend(product_companies)
        print(f"Found {len(product_companies)} product manufacturers")
        
        # Also try with industry filter if provided
        if industry_filter:
            additional_companies = search_google_places(f"{product} {industry_filter} manufacturer", 'North America', 30)
            companies.extend(additional_companies)
    else:
        # Industry-based search (original functionality)
        # Modify industry query to focus on B2B/transportation-relevant companies
        search_queries = [industry]
        
        # Add transportation-related modifiers if not already present
        if industry.lower() not in TRANSPORTATION_KEYWORDS:
            search_queries.extend([
                f"{industry} manufacturing",
                f"{industry} distribution",
                f"{industry} warehouse",
                f"{industry} wholesale"
            ])
        
        # Try Google Places Text Search first (faster)
        # Reduced max_results to avoid timeout
        print(f"Searching Google Places for {industry} (filtering for transportation-relevant companies)...")
        google_companies = search_google_places(industry, 'North America', 30, timeout_seconds=20)  # Reduced to 30, 20s timeout
        companies.extend(google_companies)
        print(f"Found {len(google_companies)} transportation-relevant companies from Google Places")
        
        # Early return if we have enough
        if len(companies) >= 20:
            print(f"Found {len(companies)} companies, returning early to avoid timeout")
            return companies[:20]
    
    # Skip Nearby Search and Yelp - they're too slow and cause timeout
    # Try Apollo.io API (faster than multiple Google searches)
    if len(companies) < 20 and APOLLO_API_KEY:
        if search_type == 'product' and product:
            print(f"Searching Apollo.io for manufacturers of {product}...")
            apollo_companies = search_apollo_api(product, 'North America', 20, 'product', product)  # Reduced to 20
        else:
            print(f"Searching Apollo.io for {industry}...")
            apollo_companies = search_apollo_api(industry, 'North America', 20)  # Reduced to 20
        companies.extend(apollo_companies)
        print(f"Found {len(apollo_companies)} companies from Apollo.io")
    
    # Skip Yelp and Nearby Search - they're too slow and cause timeout
    # Return what we have to avoid timeout
    
    # Remove duplicates based on name and address
    seen = set()
    unique_companies = []
    for company in companies:
        name_lower = company['name'].lower().strip()
        address_lower = company['address'].lower().strip() if company['address'] else ''
        
        # Create a key for deduplication
        key = (name_lower, address_lower)
        if key not in seen and name_lower:  # Only add if name exists
            seen.add(key)
            unique_companies.append(company)
    
    print(f"Total unique companies found: {len(unique_companies)}")
    # Return max 20 companies to avoid timeout (reduced from 100)
    return unique_companies[:20]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/progress', methods=['GET'])
def get_progress():
    """Get current search progress"""
    global current_progress
    try:
        with progress_lock:
            # Create a safe copy to avoid any threading issues
            progress_copy = {
                'status': current_progress.get('status', 'idle'),
                'current_step': current_progress.get('current_step', ''),
                'companies_found': current_progress.get('companies_found', 0),
                'total_steps': current_progress.get('total_steps', 0),
                'current_step_num': current_progress.get('current_step_num', 0),
                'details': current_progress.get('details', [])[-10:]  # Only return last 10 for performance
            }
            return jsonify(progress_copy)
    except Exception as e:
        return jsonify({
            'status': 'error',
            'current_step': 'Error getting progress',
            'companies_found': 0,
            'details': [{'time': datetime.now().strftime('%H:%M:%S'), 'message': f'Error: {str(e)}'}]
        }), 500

@app.route('/api/search', methods=['POST'])
def search_companies():
    global current_progress
    try:
        # Log that request was received
        print("=== SEARCH REQUEST RECEIVED ===")
        print(f"Request method: {request.method}")
        print(f"Content-Type: {request.content_type}")
        
        # Reset progress
        with progress_lock:
            current_progress = {
                'status': 'starting',
                'current_step': 'Initializing search...',
                'companies_found': 0,
                'total_steps': 0,
                'current_step_num': 0,
                'details': []
            }
        
        # Check if request has JSON data
        if not request.is_json:
            print("ERROR: Request is not JSON")
            return jsonify({
                'error': 'Request must be JSON',
                'companies': [],
                'count': 0
            }), 400
        
        data = request.json
        print(f"Received data: {data}")
        search_type = data.get('search_type', 'industry')
        industry = data.get('industry', '').strip()
        product = data.get('product', '').strip()
        industry_filter = data.get('industry_filter', '').strip()
        
        # Validate based on search type
        if search_type == 'product':
            if not product:
                update_progress('error', 'validation', 0, 'Product name is required')
                return jsonify({'error': 'Product name is required'}), 400
            search_query = product
        else:
            if not industry:
                update_progress('error', 'validation', 0, 'Industry is required')
                return jsonify({'error': 'Industry is required'}), 400
            search_query = industry
        
        # Check if API keys are configured
        print(f"GOOGLE_PLACES_API_KEY exists: {bool(GOOGLE_PLACES_API_KEY)}")
        print(f"YELP_API_KEY exists: {bool(YELP_API_KEY)}")
        print(f"APOLLO_API_KEY exists: {bool(APOLLO_API_KEY)}")
        
        if not GOOGLE_PLACES_API_KEY and not YELP_API_KEY:
            print("ERROR: No API keys configured")
            update_progress('error', 'config', 0, 'No API keys configured')
            return jsonify({
                'error': 'No API keys configured. Please set GOOGLE_PLACES_API_KEY or YELP_API_KEY environment variables. See README.md for instructions.',
                'companies': []
            }), 400
        
        if search_type == 'product':
            update_progress('searching', f'Searching for manufacturers of: {product}', 0, f'Looking for companies that manufacture {product}...')
        else:
            update_progress('searching', f'Searching for: {industry}', 0, 'Starting company search...')
        
        # Get companies based on search type
        print(f"Starting search: type={search_type}, industry={industry}, product={product}")
        search_start_time = time.time()
        try:
            if search_type == 'product':
                companies = get_companies_from_directories('', search_type, product, industry_filter)
            else:
                companies = get_companies_from_directories(industry, search_type, '', '')
            search_elapsed = time.time() - search_start_time
            print(f"Search completed: Found {len(companies)} companies in {search_elapsed:.1f}s")
            
            # If search took too long, return what we have
            if search_elapsed > 25:
                print(f"WARNING: Search took {search_elapsed:.1f}s, close to timeout limit")
        except Exception as search_error:
            search_elapsed = time.time() - search_start_time
            print(f"ERROR in get_companies_from_directories after {search_elapsed:.1f}s: {str(search_error)}")
            import traceback
            print(traceback.format_exc())
            # Return empty list instead of raising to avoid timeout
            companies = []
        
        # Accept fewer companies to avoid timeout (reduced from 10 to 5)
        if len(companies) < 5:
            update_progress('warning', 'low_results', len(companies), f'Only found {len(companies)} companies')
            return jsonify({
                'error': f'Only found {len(companies)} companies. Please try a different industry or check your API keys.',
                'companies': companies,
                'count': len(companies)
            }), 200
        
        update_progress('completed', 'Search completed successfully', len(companies), f'Found {len(companies)} companies')
        
        # Save to search history
        if search_type == 'product':
            add_to_history('product', product, industry_filter)
        else:
            add_to_history('industry', industry, '')
        
        return jsonify({
            'success': True,
            'count': len(companies),
            'companies': companies
        })
        
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print("=" * 50)
        print("ERROR IN SEARCH_COMPANIES")
        print(f"Error: {str(e)}")
        print(f"Type: {type(e).__name__}")
        print("Traceback:")
        print(error_trace)
        print("=" * 50)
        
        try:
            update_progress('error', 'exception', 0, f'Error: {str(e)}')
        except:
            pass  # Don't fail if progress update fails
        
        # Always return valid JSON, even on error
        try:
            return jsonify({
                'error': str(e),
                'companies': [],
                'count': 0,
                'error_type': type(e).__name__
            }), 500
        except Exception as json_error:
            # Last resort - return simple text response
            print(f"CRITICAL: Could not return JSON error: {json_error}")
            return f"Error: {str(e)}", 500, {'Content-Type': 'text/plain'}

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get all search history"""
    try:
        search_type = request.args.get('type', None)  # Optional filter by type
        history = get_search_history()
        
        # Filter by type if specified
        if search_type:
            history = [item for item in history if item.get('type') == search_type]
        
        return jsonify({
            'success': True,
            'history': history,
            'count': len(history)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['POST'])
def save_history():
    """Save a search to history (called from frontend)"""
    try:
        data = request.json
        search_type = data.get('type', 'industry')
        query = data.get('query', '').strip()
        industry_filter = data.get('industry_filter', '').strip()
        
        if not query:
            return jsonify({'error': 'Query is required'}), 400
        
        add_to_history(search_type, query, industry_filter)
        
        return jsonify({
            'success': True,
            'message': 'Search saved to history'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/export', methods=['POST'])
def export_to_excel():
    try:
        data = request.json
        companies = data.get('companies', [])
        search_query = data.get('search_query', 'companies')
        
        if not companies:
            return jsonify({'error': 'No companies to export'}), 400
        
        # Create DataFrame
        df = pd.DataFrame(companies)
        
        # Reorder columns (include Apollo.io fields if available)
        column_order = ['name', 'industry', 'business_type', 'address', 'phone', 'email', 'website', 'employee_count', 'revenue', 'rating', 'country']
        # Only include columns that exist in the dataframe
        available_columns = [col for col in column_order if col in df.columns]
        # Add any other columns that weren't in the order
        other_columns = [col for col in df.columns if col not in column_order]
        df = df[available_columns + other_columns]
        
        # Sanitize search query for filename (remove invalid characters)
        sanitized_query = re.sub(r'[<>:"/\\|?*]', '', search_query)
        sanitized_query = re.sub(r'\s+', '_', sanitized_query.strip())
        sanitized_query = sanitized_query[:50]  # Limit length to 50 characters
        
        # Generate filename with search query
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'{sanitized_query}_{timestamp}.xlsx'
        filepath = os.path.join('exports', filename)
        
        # Create exports directory if it doesn't exist
        os.makedirs('exports', exist_ok=True)
        
        # Export to Excel
        df.to_excel(filepath, index=False, engine='openpyxl')
        
        return send_file(filepath, as_attachment=True, download_name=filename)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Get port from environment variable (for production) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Only run in debug mode if not in production
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)

