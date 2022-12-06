import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'google_shopping_search',
    'domain': 'com',
    'query': 'adidas',
    'pages': 4,
    'context': [
        {'key': 'sort_by', 'value': 'pd'},
        {'key': 'min_price', 'value': 20},
    ],
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())