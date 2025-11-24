import json
import requests

# Structure payload.
payload = {
    'source': 'google',
    'url': 'https://www.google.com/search?udm=28&q=adidas&hl=en',
    'geo_location': 'New York,New York,United States',
    'parse': True
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'),
    json=payload
)
print(response.json())

with open('shopping_url.json', 'w') as f:
    json.dump(response.json(), f, indent=2)