import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'google_shopping_product',
    'domain': 'com',
    'query': '5007040952399054528',
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