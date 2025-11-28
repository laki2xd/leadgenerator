# Apollo.io API Setup Guide

## Overview

Apollo.io is a B2B database with over 275 million contacts and 70+ million companies. It's excellent for finding B2B companies, especially those in manufacturing, distribution, and logistics.

## Step 1: Create Apollo.io Account

1. Go to **https://www.apollo.io**
2. Click **"Sign Up"** or **"Get Started"**
3. Fill in your information and create an account
4. Verify your email address

## Step 2: Get Your API Key

1. After logging in, go to your **Apollo Dashboard**
2. Click on your profile icon (top right)
3. Go to **Settings** → **Integrations** → **API**
4. Or directly visit: **https://app.apollo.io/#/settings/integrations/api**
5. Click **"Generate API Key"** or copy your existing key
6. **Important:** Save this key immediately - you may not be able to view it again!

## Step 3: Add API Key to Your Project

### Option A: Add to config.py (Recommended)

1. Open `config.py` in your project folder
2. Find the line: `APOLLO_API_KEY = ''`
3. Add your API key:
   ```python
   APOLLO_API_KEY = 'your-apollo-api-key-here'
   ```
4. Save the file

### Option B: Set Environment Variable

**Windows PowerShell:**
```powershell
$env:APOLLO_API_KEY="your-apollo-api-key-here"
```

**Windows Command Prompt:**
```cmd
set APOLLO_API_KEY=your-apollo-api-key-here
```

**Linux/Mac:**
```bash
export APOLLO_API_KEY="your-apollo-api-key-here"
```

## Step 4: Test Your Setup

Run the application and search for companies. If Apollo.io is configured, you'll see:
```
Searching Apollo.io for [industry]...
Found X companies from Apollo.io
```

## Apollo.io API Features

### What Apollo.io Provides:
- **Company Data**: Name, address, phone, website, email
- **Employee Count**: Estimated number of employees
- **Revenue**: Estimated annual revenue
- **Industry Tags**: Industry classification
- **Location Data**: Detailed address information
- **Contact Information**: Phone numbers and emails

### Free Tier Limits:
- **50 API requests per day**
- Good for testing and small-scale use
- Paid plans offer more requests

### Paid Plans:
- **Basic**: $49/month - 1,000 requests/month
- **Professional**: $99/month - 5,000 requests/month
- **Organization**: Custom pricing - Unlimited requests

## How It Works in This App

1. **Automatic Integration**: Apollo.io is called automatically when:
   - You have less than 100 companies from Google Places
   - Your API key is configured

2. **Smart Filtering**: The app automatically:
   - Filters for transportation-relevant companies
   - Excludes retail stores and small shops
   - Focuses on B2B companies

3. **Data Enrichment**: Apollo.io provides:
   - Employee count
   - Revenue estimates
   - Industry classifications
   - Better contact information

## API Endpoint Used

The app uses Apollo's **Organizations Search API**:
- Endpoint: `https://api.apollo.io/v1/organizations/search`
- Method: POST
- Authentication: HTTP Basic Auth (API key as username, 'X' as password)

## Troubleshooting

### "Authentication failed"
- Check that your API key is correct
- Make sure there are no extra spaces or quotes
- Verify the key in Apollo.io dashboard

### "Rate limit exceeded"
- You've hit your daily limit (50 requests on free tier)
- Wait 24 hours or upgrade your plan
- The app will continue using other APIs (Google Places, Yelp)

### "No companies found"
- Apollo.io may not have companies matching your search
- Try a different industry term
- Check that your search is transportation-focused

### API Key Not Working
1. Verify the key in Apollo.io dashboard
2. Make sure you're using the API key (not your account password)
3. Check that the key hasn't expired
4. Try regenerating the key

## Best Practices

1. **Start with Free Tier**: Test with the free 50 requests/day
2. **Combine APIs**: Apollo.io works best combined with Google Places
3. **Use Specific Terms**: More specific searches yield better results
4. **Monitor Usage**: Check your API usage in Apollo.io dashboard

## Example Searches That Work Well

- "Manufacturing"
- "Distribution"
- "Warehouse"
- "Logistics"
- "Freight"
- "Wholesale"
- "Industrial"

## Additional Resources

- **Apollo.io API Docs**: https://docs.apollo.io/docs/api-overview
- **Apollo.io Dashboard**: https://app.apollo.io
- **Support**: Contact Apollo.io support through their dashboard

## Security Note

⚠️ **Never commit your API key to version control!**
- The `config.py` file is already in `.gitignore`
- Never share your API key publicly
- Regenerate your key if it's accidentally exposed

## Ready to Use!

Once you've added your API key, restart the application:
```bash
python app.py
```

The Apollo.io integration will automatically activate when you search for companies!

