import fetch from 'node-fetch';

const username = 'YOUR_USERNAME';
const password = 'YOUR_PASSWORD';
const body = {
  'source': 'google_shopping_search',
  'domain': 'com',
  'query': 'adidas',
  'pages': 4,
  'context': [
        {'key': 'sort_by', 'value': 'pd'},
        {'key': 'min_price', 'value': 20}
    ],
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