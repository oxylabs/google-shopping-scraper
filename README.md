# Google Shopping Scraper

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/google-news-scraper/refs/heads/main/Scrape%20Google%20data%20with%20Web%20Scraper%20API.png)](https://oxylabs.io/products/scraper-api/serp/google?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=google-shopping-scraper-github&transaction_id=102c8d36f7f0d0e5797b8f26152160)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.com/invite/Pds3gBmKMH)

- [Google Shopping Scraper](#google-shopping-scraper)
  * [Free Google Shoppping Scraper](#free-google-shoppping-scraper)
    + [Prerequisites](#prerequisites)
    + [Installation](#installation)
    + [Scraping Google Shopping](#scraping-google-shopping)
    + [Notes](#notes)
  * [Scraping Google Shopping with Oxylabs API](#scraping-google-shopping-with-oxylabs-api)
    + [How it works](#how-it-works)
    + [Overview](#overview)
    + [URL](#url)
      - [Query parameters](#query-parameters)
      - [Python code example](#python-code-example)
    + [Shopping Search](#shopping-search)
      - [Query parameters](#query-parameters-1)
      - [Python code example](#python-code-example-1)
    + [Shopping Product](#shopping-product)
      - [Query parameters](#query-parameters-2)
      - [Python code example](#python-code-example-2)
    + [Product Pricing](#product-pricing)
      - [Query parameters](#query-parameters-3)
      - [Python code example](#python-code-example-3)

In this tutorial, we'll demonstrate how to extract data from Google Shopping. In the first part of the tutorial, we'll use a free tool, built for smaller scale scraping. In the second part, we'll show how to use Oxylabs API for more effective, bigger scale scraping. To use Oxylabs API, get a **free trial** [here](https://dashboard.oxylabs.io/).

## Free Google Shoppping Scraper

A free tool used to get shopping items from Google Shopping for a provided search query.

### Prerequisites

To run this tool, you need to have Python 3.11 installed in your system.

### Installation

Open up a terminal window, navigate to this repository and run this command:

```make install```

### Scraping Google Shopping

To scrape shopping items from Google Shopping, simply run this command in your terminal with a query of your choosing:

```make scrape QUERY="<your_shopping_search_query>"```

For this example, let's try scraping Google Shopping results for cat food. The command should look something like this:

```make scrape QUERY="cat food"```

Make sure to enclose your query in quotation marks, otherwise the tool might have trouble parsing it.

After running the command, your terminal should look something like this:

<img width="786" alt="image" src="https://github.com/user-attachments/assets/43b10ce1-1f4f-49c7-bdbd-81246c5bc875">

After the tool has finished running, you should see a file named `shopping.csv` in your current directory.

This file contains shopping listings for the query you entered. 
The generated CSV file contains these columns of data:

- `title` - The title of the item.
- `price` - The price of the item.
- `delivery_price` - The delivery price of the item.
- `review` - An optional review field, which can contain a rating of up to 5 stars, and a total number of reviews.
- `url` - The URL of the Google Shopping page for that item.

Here's an example of how the data can look like:

<img width="1058" alt="image" src="https://github.com/user-attachments/assets/7176c269-b28a-4333-abb6-992e2a40b153">

### Notes

In case the code doesn't work or your project is of bigger scale, please refer to the second part of the tutorial. There, we showcase how to scrape public data with Oxylabs API.

## Scraping Google Shopping with Oxylabs API

[Google Shopping Scraper](https://oxy.yt/qadX) (a part of Web Scraper API) extracts timely e-commerce data in raw HTML or structured JSON format. The scraper offers a maintenance-free data collection infrastructure that automates the bulk of underlying processes, from sending HTTP requests to data parsing. 

The underlying measures, such as proxies, ensure considerably fewer CAPTCHAs and IP blocks. The scraper supports localized results from almost any locale worldwide (195 countries) with country-level and postal code targeting.

Additionally, the scraper can automate recurring scraping and parsing jobs through [**Scheduler**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/scheduler), load dynamic websites that use JavaScript for rendering content, and retrieve results via the API or directly to Amazon S3, Google Cloud Storage, Alibaba Cloud OSS, or any other S3-compatible destination.

You can also customize the folder and file names of the results delivered to your cloud storage by using template variables like `{{source}}`, `{{query}}`, `{{job_id}}`, and `{{extension}}` in your `storage_url`. This makes it easier to identify files at a glance and keep your storage organized by search term, job ID, or other criteria.

Keep in mind that to access this tool, you'll need an active subscription – a paid plan or a free trial. You can claim your trial via our self-service [dashboard](https://dashboard.oxylabs.io/).  

### How it works

There are various page types we can scrape and parse on Google Shopping. You can either provide us with a full [**URL**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/google/url) or a few input parameters via specifically built data sources (e.g. [**Search**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/google/shopping-search), [**Product**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/google/shopping-product), [**Product Pricing**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/google/product-pricing) so we can form the URL on our end.

### Overview

Below is a quick overview of all the available data `source` values we support with Google Shopping.

| Source                    | Description                                               | Structured data     |
| ------------------------- | --------------------------------------------------------- | ------------------- |
| `google`                  | Submit any Google Shopping URL you like.                  | Depends on the URL. |
| `google_shopping_search`  | Search results for a search term of your choice.          | Yes.                |
| `google_shopping_product` | Product page of a product ID of your choice.              | Yes.                |
| `google_shopping_pricing` | List of offers available for a product ID of your choice. | Yes.                |

### URL

The `google` source is designed to retrieve content from various Google Shopping URLs. Instead of sending multiple parameters and letting us form and scrape Google Shopping URLs, you can provide us with a URL to the required Google Shopping page. We do not strip any parameters or alter your URLs in any other way.

This data source also supports parsed data (structured data in JSON format), as long as the URL submitted links to a page that we can parse. You can also get [multiple result types](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/result-processing-and-storage/output-types/multi-format-output) (parsed, Markdown, screenshots, XHR, and raw) simultaneously in a single API response.

#### Query parameters

| Parameter                                                 | Description                                                                                                                                                                                                                                                    | Default Value |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| <mark style="background-color:green;">**`source`**</mark> | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/google).                                                                                                                                                           | `google`      |
| <mark style="background-color:green;">**`url`**</mark>    | Direct URL (link) to Google page                                                                                                                                                                                                                               | -             |
| `user_agent_type`                                         | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/user-agent-type).                                                                                                              | `desktop`     |
| `render`                                                  | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/javascript-rendering)                                                                                                                                          |               |
| `callback_url`                                            | URL to your callback endpoint. [**More info.**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/integration-methods/push-pull#callback)                                                                                                                                  | -             |
| `geo_location`                                            | The geographical location that the result should be adapted for. Using this parameter correctly is extremely important to get the right data. For more information, read about our suggested `geo_location` parameter structures [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/geo-location#google). | -             |
| `parse`                                                   | `true` will return parsed data, as long as the URL submitted is for Google Search.                                                                                                                                                                             | -             |

\- required parameter

#### Python code example

In this example, we make a request to retrieve a Google Shopping Search result for keyword `adidas`, as seen in New York, USA.

```python 
import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'google',
    'url': 'https://www.google.com/search?tbm=shop&q=adidas&hl=en',
    'geo_location': 'New York,New York,United States'
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
```

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/google-shopping-scraper/tree/main/code%20examples)

### Shopping Search

The `google_shopping_search` source is designed to retrieve Google Shopping search results.

#### Query parameters

| Parameter                                                 | Description                                                                                                                                                                                                                                                    | Default Value            |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| <mark style="background-color:green;">**`source`**</mark> | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/google).                                                                                                                                                           | `google_shopping_search` |
| `domain`                                                  | Domain localization                                                                                                                                                                                                                                            | com                      |
| <mark style="background-color:green;">**`query`**</mark>  | UTF-encoded keyword                                                                                                                                                                                                                                            | -                        |
| `start_page`                                              | Starting page number                                                                                                                                                                                                                                           | `1`                      |
| `pages`                                                   | Number of pages to retrieve                                                                                                                                                                                                                                    | `1`                      |
| `locale`                                                  | `Accept-Language` header value which changes your Google Shopping page web interface language. [**More info**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/domain-locale-results-language#locale-1).                                                                                                                              | -                        |
| `results_language`                                        | Results language. List of supported Google languages can be found [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/domain-locale-results-language#results-language).                                                                                                                                                                | -                        |
| `geo_location`                                            | The geographical location that the result should be adapted for. Using this parameter correctly is extremely important to get the right data. For more information, read about our suggested `geo_location` parameter structures [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/geo-location#google). | -                        |
| `user_agent_type`                                         | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/user-agent-type).                                                                                                              | `desktop`                |
| `render`                                                  | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/javascript-rendering)                                                                                                                                          | -                        |
| `callback_url`                                            | URL to your callback endpoint. [**More info.**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/integration-methods/push-pull#callback)                                                                                                                                  | -                        |
| `parse`                                                   | `true` will return parsed data.                                                                                                                                                          | -                        |
| <p><code>context</code>:<br><code>nfpr</code></p>         | `true` will turn off spelling auto-correction.                                                                                                                                                                                                                 | `false`                  |
| <p><code>context</code>:<br><code>sort_by</code></p>      | Sort product list by a given criteria. `r` applies default Google sorting, `rv` - by review score, `p` - by price ascending, `pd` - by price descending                                                                                                        | `r`                      |
| <p><code>context</code>:<br><code>min_price</code></p>    | Minimum price of products to filter                                                                                                                                                                                                                            | -                        |
| <p><code>context</code>:<br><code>max_price</code></p>    | Maximum price of products to filter                                                                                                                                                                                                                            | -                        |

\- required parameter

#### Python code example

In this example, we make a request to retrieve the first `4` pages of Google Shopping search for the search term `adidas`, sorted by descending price and minimum price of `$20`.

```python
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
```
Code examples for other languages can be found [**here.**](https://github.com/oxylabs/google-shopping-scraper/tree/main/code%20examples)

### Shopping Product

The `google_shopping_product` source is designed to retrieve Google Shopping product page for a specified product.

#### Query parameters

| Parameter                                                 | Description                                                                                                                                                                                                                                                    | Default Value             |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| <mark style="background-color:green;">**`source`**</mark> | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/google).                                                                                                                                                           | `google_shopping_product` |
| `domain`                                                  | Domain localization                                                                                                                                                                                                                                            | com                       |
| <mark style="background-color:green;">**`query`**</mark>  | UTF-encoded product code                                                                                                                                                                                                                                       | -                         |
| `locale`                                                  | `Accept-Language` header value which changes your Google Shopping page web interface language. [**More info**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/domain-locale-results-language#locale-1).                                                                                                                              | -                         |
| `results_language`                                        | Results language. List of supported Google languages can be found [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/domain-locale-results-language#results-language).                                                                                                                                                                | -                         |
| `geo_location`                                            | The geographical location that the result should be adapted for. Using this parameter correctly is extremely important to get the right data. For more information, read about our suggested `geo_location` parameter structures [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/geo-location#google). | -                         |
| `user_agent_type`                                         | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/user-agent-type).                                                                                                              | `desktop`                 |
| `render`                                                  | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/javascript-rendering)                                                                                                                                          |                           |
| `callback_url`                                            | URL to your callback endpoint. [**More info**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/integration-methods/push-pull#callback).                                                                                                                                  | -                         |
| `parse`                                                   | `true` will return parsed data.                                                                                                                                                            | -                         |

\- required parameter

#### Python code example

In the code example below, we make a request to retrieve the product page for product ID `5007040952399054528` from Google Shopping on `com` domain.

```python
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
```
Code examples for other languages can be found [**here.**](https://github.com/oxylabs/google-shopping-scraper/tree/main/code%20examples)

### Product Pricing

The `google_shopping_pricing` source is designed to retrieve pages containing lists of offers available for a product ID of your choice.

#### Query parameters

| Parameter                                                 | Description                                                                                                                                                                                                                                                    | Default Value             |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| <mark style="background-color:green;">**`source`**</mark> | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/google).                                                                                                                                                           | `google_shopping_pricing` |
| `domain`                                                  | Domain localization                                                                                                                                                                                                                                            | com                       |
| <mark style="background-color:green;">**`query`**</mark>  | UTF-encoded product code                                                                                                                                                                                                                                       | -                         |
| `start_page`                                              | Starting page number                                                                                                                                                                                                                                           | `1`                       |
| `pages`                                                   | Number of pages to retrieve                                                                                                                                                                                                                                    | `1`                       |
| `locale`                                                  | `Accept-Language` header value which changes your Google Shopping page web interface language. [**More info**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/domain-locale-results-language#locale-1).                                                                                                                              | -                         |
| `results_language`                                        | Results language. List of supported Google languages can be found [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/domain-locale-results-language#results-language).                                                                                                                                                                | -                         |
| `geo_location`                                            | The geographical location that the result should be adapted for. Using this parameter correctly is extremely important to get the right data. For more information, read about our suggested `geo_location` parameter structures [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/geo-location#google). | -                         |
| `user_agent_type`                                         | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/user-agent-type).                                                                                                              | `desktop`                 |
| `render`                                                  | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/javascript-rendering)                                                                                                                                          |                           |
| `callback_url`                                            | URL to your callback endpoint. [**More info.**](https://developers.oxylabs.io/scraper-apis/web-scraper-api/integration-methods/push-pull#callback)                                                                                                                                  | -                         |
| `parse`                                                   | `true` will return parsed data.                                                                                                                                                            | -                         |
\- required parameter

#### Python code example

In the code example below, we make a request to retrieve the product pricing page for product ID `5007040952399054528` from Google Shopping on `google.com`.

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'google_shopping_pricing',
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
```

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/google-shopping-scraper/tree/main/code%20examples).

If you have questions or concerns about Google Shopping Scraper or associated features, get in touch via (support@oxylabs.io) or through the live chat on our [**website**](https://oxylabs.io/).

Read More Google Scraping Related Repositories: [Google Sheets for Basic Web Scraping](https://github.com/oxylabs/web-scraping-google-sheets), [How to Scrape Google Shopping Results](https://github.com/oxylabs/scrape-google-shopping), [Google Maps Scraper](https://github.com/oxylabs/google-maps-scraper), [Google Play Scraper](https://github.com/oxylabs/google-play-scraper), [How To Scrape Google Jobs](https://github.com/oxylabs/how-to-scrape-google-jobs), [Google News Scrpaer](https://github.com/oxylabs/google-news-scraper), [How to Scrape Google Scholar](https://github.com/oxylabs/how-to-scrape-google-scholar), [How to Scrape Google Flights with Python](https://github.com/oxylabs/how-to-scrape-google-flights), [How To Scrape Google Images](https://github.com/oxylabs/how-to-scrape-google-images), [Scrape Google Search Results](https://github.com/oxylabs/scrape-google-python), [Scrape Google Trends](https://github.com/oxylabs/how-to-scrape-google-trends)

Also, check this tutorial on [pypi](https://pypi.org/project/google-shopping-scraper-api/)
