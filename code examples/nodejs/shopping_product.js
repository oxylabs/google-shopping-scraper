import fetch from 'node-fetch';

const username = 'YOUR_USERNAME';
const password = 'YOUR_PASSWORD';
const body = {
  'source': 'google_shopping_product',
  // Get the product token from search results
  'query': 'eyJjYXRhbG9naWQiOiAiODU5MDM3MTQzMDU2NjE1ODI1MiIsICJncGNpZCI6ICIxMDgzMzg0MTk4NjQ2MjAyMTYzMSIsICJpbWFnZURvY2lkIjogIjk1ODcyNDM4NDcwODcwNzM1ODYiLCAibWlkIjogIjU3NjQ2MjUxMTM1NDY1MjkyOSIsICJwdm8iOiAiMTkiLCAicHZ0IjogImEiLCAicmRzIjogIlBDXzEwODMzODQxOTg2NDYyMDIxNjMxfFBST0RfUENfMTA4MzM4NDE5ODY0NjIwMjE2MzEiLCAicHJvZHVjdGlkIjogIiIsICJxdWVyeSI6ICJhZGlkYXMifQ==',
  'geo_location': 'New York,New York,United States',
  'parse': true
};
const response = await fetch('https://realtime.oxylabs.io/v1/queries', {
  method: 'post',
  body: JSON.stringify(body),
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + Buffer.from(`${username}:${password}`).toString('base64'),
  }
});

console.log(await response.json());