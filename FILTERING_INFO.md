# Filtering & Transportation Focus

## Overview

The application has been enhanced to filter out retail stores and small walk-in shops, focusing specifically on companies that need transportation services.

## What Gets Filtered OUT

The following business types are automatically excluded:

### Retail & Consumer Services
- Restaurants, cafes, coffee shops, bakeries
- Clothing stores, shoe stores, jewelry stores
- Book stores, convenience stores, supermarkets
- Beauty salons, spas, gyms, fitness centers
- Gas stations, pharmacies, banks, ATMs
- Real estate agencies, travel agencies
- Tourist attractions, shopping malls

### Small Businesses
- Small retail shops
- Online-only stores (when detectable)
- Small service businesses

## What Gets INCLUDED

The application focuses on companies that typically need transportation/logistics services:

### Priority Business Types
- **Manufacturing companies** - Factories, production facilities
- **Warehouses** - Storage and distribution facilities
- **Distribution centers** - Logistics hubs
- **Freight & Shipping companies** - Transportation providers
- **Wholesale businesses** - B2B suppliers
- **Industrial companies** - Large-scale operations
- **Construction companies** - Need material transport
- **Mining companies** - Resource extraction
- **Agriculture/Farming** - Crop and livestock transport
- **Processing facilities** - Food, materials processing
- **Assembly plants** - Manufacturing assembly

## How Filtering Works

1. **Business Type Check**: Uses Google Places API business types to identify and exclude retail stores
2. **Keyword Analysis**: Analyzes company names and addresses for transportation-related keywords
3. **Name Pattern Matching**: Filters out common retail indicators (store, shop, outlet) unless they're wholesale/distribution
4. **Status Verification**: Only includes operational businesses

## Search Query Enhancement

When you search for an industry, the app automatically:

1. **Adds transportation modifiers** if your search term isn't already transportation-focused
   - Example: "Technology" → searches for "Technology manufacturing", "Technology distribution", etc.

2. **Prioritizes B2B companies** over consumer-facing businesses

3. **Focuses on physical locations** that would need freight/logistics services

## Example Searches

### Good Searches (Transportation-Focused)
- "Manufacturing"
- "Distribution"
- "Warehouse"
- "Logistics"
- "Wholesale"
- "Freight"
- "Industrial"

### Also Works (Auto-Enhanced)
- "Technology" → searches for "Technology manufacturing", "Technology distribution"
- "Food" → searches for "Food processing", "Food distribution"
- "Automotive" → searches for "Automotive manufacturing", "Automotive parts distribution"

## Results Include

Each company result includes:
- Company name
- Business type (e.g., "manufacturing, warehouse, storage")
- Full address
- Phone number (clickable)
- Email address (when available)
- Website
- Rating
- Country

## Excel Export

The exported Excel file includes a "Business Type" column showing the company's classification, making it easy to identify the type of transportation services they might need.

## Tips for Best Results

1. **Use transportation-focused terms** when possible
2. **Be specific** - "Manufacturing" is better than "Business"
3. **Try industry + modifier** - "Food distribution" is better than just "Food"
4. **Check the business_type column** in Excel to see what type of company it is

## Future Enhancements

Additional APIs can be integrated for even better filtering:
- **Hunter.io** - For finding email addresses
- **Apollo.io** - For B2B company database
- **Clearbit** - For company enrichment
- See `API_OPTIONS.md` for more details

