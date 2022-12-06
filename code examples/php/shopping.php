<?php

$params = array(
    'source' => 'google',
    'url' => 'https://www.google.com/search?tbm=shop&q=adidas&hl=en',
    'geo_location' => 'New York,New York,United States'
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "https://data.oxylabs.io/v1/queries");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($params));
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_USERPWD, "YOUR_USERNAME" . ":" . "YOUR_PASSWORD"); //Your credentials go here

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