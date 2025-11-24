import json
import requests

# Structure payload.
payload = {
    'source': 'google_shopping_search',
    'query': 'adidas',
    'geo_location': 'New York,New York,United States',
    'pages': 2,
    'context': [
        {'key': 'sort_by', 'value': 'pd'},
        {'key': 'min_price', 'value': 20},
    ],
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

with open('shopping_search.json', 'w') as f:
    json.dump(response.json(), f, indent=2)