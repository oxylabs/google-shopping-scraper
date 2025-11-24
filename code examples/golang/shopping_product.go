package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	const Username = "YOUR_USERNAME"
	const Password = "YOUR_PASSWORD"

	payload := map[string]interface{}{
		"source": "google_shopping_product",
		// Get the product token from search results
		"query": "eyJjYXRhbG9naWQiOiAiODU5MDM3MTQzMDU2NjE1ODI1MiIsICJncGNpZCI6ICIxMDgzMzg0MTk4NjQ2MjAyMTYzMSIsICJpbWFnZURvY2lkIjogIjk1ODcyNDM4NDcwODcwNzM1ODYiLCAibWlkIjogIjU3NjQ2MjUxMTM1NDY1MjkyOSIsICJwdm8iOiAiMTkiLCAicHZ0IjogImEiLCAicmRzIjogIlBDXzEwODMzODQxOTg2NDYyMDIxNjMxfFBST0RfUENfMTA4MzM4NDE5ODY0NjIwMjE2MzEiLCAicHJvZHVjdGlkIjogIiIsICJxdWVyeSI6ICJhZGlkYXMifQ==",
		"geo_location": "New York,New York,United States",
		"parse": true,
	}

	jsonValue, _ := json.Marshal(payload)

	client := &http.Client{}
	request, _ := http.NewRequest("POST",
		"https://realtime.oxylabs.io/v1/queries",
		bytes.NewBuffer(jsonValue),
	)

	request.SetBasicAuth(Username, Password)
	response, _ := client.Do(request)

	responseText, _ := ioutil.ReadAll(response.Body)
	fmt.Println(string(responseText))
}