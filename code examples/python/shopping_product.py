import json
import requests

# Structure payload.
payload = {
    'source': 'google_shopping_product',
    # Get the product token from search results
    'query': 'eyJjYXRhbG9naWQiOiAiODU5MDM3MTQzMDU2NjE1ODI1MiIsICJncGNpZCI6ICIxMDgzMzg0MTk4NjQ2MjAyMTYzMSIsICJpbWFnZURvY2lkIjogIjk1ODcyNDM4NDcwODcwNzM1ODYiLCAibWlkIjogIjU3NjQ2MjUxMTM1NDY1MjkyOSIsICJwdm8iOiAiMTkiLCAicHZ0IjogImEiLCAicmRzIjogIlBDXzEwODMzODQxOTg2NDYyMDIxNjMxfFBST0RfUENfMTA4MzM4NDE5ODY0NjIwMjE2MzEiLCAicHJvZHVjdGlkIjogIiIsICJxdWVyeSI6ICJhZGlkYXMifQ==',
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

with open('shopping_product.json', 'w') as f:
    json.dump(response.json(), f, indent=2)