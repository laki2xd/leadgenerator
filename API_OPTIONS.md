# Additional API Options for Company Data

This document lists additional APIs you can integrate to enhance company search capabilities.

## Recommended APIs for B2B Company Data

### 1. **Clearbit API** (Company Enrichment)
- **Website:** https://clearbit.com
- **Use Case:** Company data enrichment, domain lookup
- **Features:** Company profiles, employee count, revenue, industry classification
- **Pricing:** Free tier available, paid plans for higher volume
- **Best For:** Enriching company data with firmographics

### 2. **ZoomInfo API** (B2B Database)
- **Website:** https://www.zoominfo.com
- **Use Case:** B2B company and contact database
- **Features:** Company data, contact information, technographics
- **Pricing:** Enterprise pricing (contact sales)
- **Best For:** Large-scale B2B lead generation

### 3. **Apollo.io API** (Sales Intelligence)
- **Website:** https://www.apollo.io
- **Use Case:** B2B contact and company data
- **Features:** Company search, contact discovery, email finder
- **Pricing:** Free tier + paid plans
- **Best For:** Sales prospecting and lead generation

### 4. **Hunter.io API** (Email Finder)
- **Website:** https://hunter.io
- **Use Case:** Find email addresses for companies
- **Features:** Email finder, email verifier, domain search
- **Pricing:** Free tier (25 searches/month), paid plans available
- **Best For:** Finding email addresses for companies

### 5. **Enrich.so API** (Company Search)
- **Website:** https://www.enrich.so
- **Use Case:** Company search by industry, location, size
- **Features:** Company profiles, filtering by multiple criteria
- **Pricing:** Free tier available
- **Best For:** Filtered company searches

### 6. **CUFinder API** (Company Data)
- **Website:** https://cufinder.io
- **Use Case:** Company search and phone number finder
- **Features:** Company profiles, phone numbers, contact info
- **Pricing:** Pay-as-you-go model
- **Best For:** Finding company contact information

### 7. **Rhetorik API** (Global Company Database)
- **Website:** https://rhetorik.com
- **Use Case:** Access to 250M+ company profiles
- **Features:** Firmographics, contact information, corporate structures
- **Pricing:** Contact for pricing
- **Best For:** Large-scale company data access

### 8. **CompanyEnrich API** (Company Enrichment)
- **Website:** https://companyenrich.com
- **Use Case:** Real-time company data enrichment
- **Features:** Firmographics, technographics, company profiles
- **Pricing:** Free tier available
- **Best For:** Real-time company data enrichment

## Free/Open Source Alternatives

### 9. **Companies House API** (UK Companies)
- **Website:** https://developer.company-information.service.gov.uk
- **Use Case:** UK company registry data
- **Features:** Free access to UK company information
- **Pricing:** Free
- **Note:** UK only, but similar APIs exist for Canada/US

### 10. **Better Business Bureau API**
- **Website:** Check BBB website for API access
- **Use Case:** Business verification and ratings
- **Features:** Business information, ratings, complaints
- **Pricing:** Varies

## Integration Priority

1. **Hunter.io** - Best for email finding (free tier available)
2. **Apollo.io** - Good B2B database with free tier
3. **Enrich.so** - Good filtering capabilities
4. **Clearbit** - Excellent for data enrichment

## How to Add APIs

1. Get API key from the provider
2. Add to `config.py`:
   ```python
   HUNTER_API_KEY = 'your-key-here'
   APOLLO_API_KEY = 'your-key-here'
   ```

3. Add search function in `app.py` similar to existing functions
4. Call from `get_companies_from_directories()`

## Current Filtering

The application now filters out:
- Restaurants, cafes, coffee shops
- Retail stores (clothing, shoes, jewelry, etc.)
- Small service businesses (salons, spas, gyms)
- Convenience stores, supermarkets
- Banks, ATMs, gas stations

And focuses on:
- Manufacturing companies
- Warehouses and distribution centers
- Logistics and freight companies
- Wholesale businesses
- Industrial companies
- Construction companies
- Mining and agriculture
- Companies with transportation/logistics needs

