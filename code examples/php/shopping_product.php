<?php

$params = array(
    'source' => 'google_shopping_product',
    // Get the product token from search results
    'query' => 'eyJjYXRhbG9naWQiOiAiODU5MDM3MTQzMDU2NjE1ODI1MiIsICJncGNpZCI6ICIxMDgzMzg0MTk4NjQ2MjAyMTYzMSIsICJpbWFnZURvY2lkIjogIjk1ODcyNDM4NDcwODcwNzM1ODYiLCAibWlkIjogIjU3NjQ2MjUxMTM1NDY1MjkyOSIsICJwdm8iOiAiMTkiLCAicHZ0IjogImEiLCAicmRzIjogIlBDXzEwODMzODQxOTg2NDYyMDIxNjMxfFBST0RfUENfMTA4MzM4NDE5ODY0NjIwMjE2MzEiLCAicHJvZHVjdGlkIjogIiIsICJxdWVyeSI6ICJhZGlkYXMifQ==',
    'geo_location' => 'New York,New York,United States',
    'parse' => true
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "https://realtime.oxylabs.io/v1/queries");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($params));
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_USERPWD, "user" . ":" . "pass1");


$headers = array();
$headers[] = "Content-Type: application/json";
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$result = curl_exec($ch);
echo $result;

if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
}
curl_close ($ch);
?>