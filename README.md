# Google Maps Scraper

## Table of Contents
- [Free Google Maps Scraper](#free-google-maps-scraper)
  - [Setup and Installation](#setup-and-installation)
  - [How to Use the Scraper](#how-to-use-the-scraper)
  - [Output](#output)
- [Common Scraping Challenges](#common-scraping-challenges)
- [Solution: Bright Data Google Maps Scraper API](#solution-bright-data-google-maps-scraper-api)
  - [Using Google Maps Scraper API](#using-google-maps-scraper-api)
  - [Customizing Data Collection with API Parameters](#customizing-data-collection-with-api-parameters)

## Free Google Maps Scraper
Use this free scraper to extract business reviews from Google Maps. You can retrieve details about reviewers, ratings, review text, photos, and more in just a few steps.

### Setup and Installation
Before diving in, make sure you have these prerequisites installed:
- Python 3.9+
- Playwright (for browser automation)

Follow these steps to get everything set up:
1. Clone the repository to your local machine
2. Navigate to the `free-scraper` directory
3. Install the required dependencies:

    ```bash
    pip install playwright
    playwright install
    ```
### How to Use the Scraper
Let's walk through how to use the scraper:

1. Open `main.py` and add your target Google Maps URLs:

    ```python
    urls = [
            "https://www.google.com/maps/place/Joe's+Pizza+Broadway/@40.7546835,-73.989604,17z/data=!3m1!5s0x89c259ab3e91ed73:0x4074c4cfa25e210b!4m8!3m7!1s0x89c259ab3c1ef289:0x3b67a41175949f55!8m2!3d40.7546795!4d-73.9870291!9m1!1b1!16s%2Fg%2F11bw4ws2mt?entry=ttu",
            "https://www.google.com/maps/place/Googleplex/@37.4220583,-122.0878991,17z/data=!4m8!3m7!1s0x808fba02425dad8f:0x6c296c66619367e0!8m2!3d37.4220541!4d-122.0853242!9m1!1b1!16zL20vMDNiYnkx?hl=en&entry=ttu",
            # Add as many URLs as you need
        ]
    ```
2. Run the script using:

    ```bash
    python main.py
    ```
### Output
The scraper will save the results in [free_scraper_output.json](https://github.com/luminati-io/Google-Maps-Scraper/blob/main/sample_data/free_scraper_output.json), containing:
```json
{
    "reviewer_name": "Jacqueline",
    "reviewer_link": "https://www.google.com/maps/contrib/108281841745817069467/reviews?hl=en-GB",
    "reviewer_image": "https://lh3.googleusercontent.com/a-/ALV-UjUzl62rTNZOxsKGxvlnjM3leUg7DZostYzDJvG_8DUSNEtC7p-X=w36-h36-p-rp-mo-ba4-br100",
    "rating": 5,
    "date": "a week ago",
    "text": "Went for lunch on a Tuesday at around 12:45pm. As usual, there was a line, but it moved really quickly and I was able to get my pizza 10 minutes later. Don't let the line deter you from trying Joe's! The pizza is great as always and the staff are nice. Never disappointed. I tried the caprese pizza and it was great!\n\nThere are a lot of people inside and outside so it can get hectic, but turnover for seats is quite quick and I got a seat on the bench outside almost right away.",
    "photos": [
        "https://lh5.googleusercontent.com/p/AF1QipMChGwUdQgWF9NAqdvss36KeuBZw_DAiuZy5yJj=w300-h225-p-k-no",
        "https://lh5.googleusercontent.com/p/AF1QipNvachPq2HyJU0_3hs0DsRDRChaHZrQDDKOc3hz=w300-h225-p-k-no"
    ],
    "likes_count": "1"
}
```

Each review entry contains:
- **Reviewer Details**: Name, profile link, and avatar image
- **Review Content**: Star rating, date posted, and full review text
- **Media**: URLs of any attached photos
- **Engagement**: Number of likes the review received

## Common Scraping Challenges
Scraping data from Google Maps can be quite challenging. Here are some common issues you may encounter:
1. **Dynamic Content Loading:** Google Maps uses a dynamic loading mechanism where reviews are fetched via XHR/API calls as the user scrolls. Without proper handling of these dynamic requests and waiting for content to load, scrapers may only capture partial data.
2. **DOM Structure Changes:** Google frequently updates their DOM structure, class names, and data attributes. This requires regular maintenance of scraping logic to adapt to structural changes.
3. **Rate Limiting and Detection:** Scraping Google Maps can trigger anti-bot defenses, which may result in rate limiting or IP bans. 

## Solution: Bright Data Google Maps Scraper API
If you need reliable, large-scale data extraction, use [Bright Data Google Maps Scraper API](https://brightdata.com/products/serp-api/google-search/maps). Here's why it works better:
- No proxy management is needed
- Scrape from any location worldwide
- Access to 72M+ real IPs across 195 countries
- Multiple data delivery options (S3, Cloud Storage, etc.)
- GDPR and CCPA compliant
- 24/7 technical support

Plus, you get **20 free API calls** to test it out.

## Using Google Maps Scraper API
You can collect detailed Google Maps reviews by simply providing a URL.

<img width="700" alt="bright-data-web-scraper-api-google-maps-reviews" src="https://github.com/luminati-io/Google-Maps-Scraper/blob/main/google-maps-review-example.PNG">

> For a detailed guide on setting up the Google Maps Scraper API, check our [Step-by-Step Setup Guide](https://github.com/luminati-io/Google-Maps-Scraper/blob/main/scraper_api_setup.md#setting-up-google-maps-scraper-api).

**Key Input Parameters:**

| **Parameter** | **Type** | **Description**                         | **Required** |
|---------------|----------|-----------------------------------------|--------------|
| `url`         | string   | Google Maps business URL               | Yes          |
| `days_limit`  | number   | Number of days to retrieve reviews from | No           |

**Sample Output Data:**

```json
{
    "url": "https://www.google.com/maps/place/Apple+Apple+Park+Visitor+Center/@37.3327772,-122.0079593,17z/data=!4m18!1m9!3m8!1s0x808fb5c5d7e7a3d1:0x1741de234d732f80!2sApple+Apple+Park+Visitor+Center!8m2!3d37.332773!4d-122.0053844!9m1!1b1!16s%2Fg%2F11rjtz4vtg!3m7!1s0x808fb5c5d7e7a3d1:0x1741de234d732f80!8m2!3d37.332773!4d-122.0053844!9m1!1b1!16s%2Fg%2F11rjtz4vtg?entry=ttu",
    "place_id": "ChIJ0aPn18W1j4ARgC9zTSPeQRc",
    "place_name": "Apple Apple Park Visitor Center",
    "country": "US",
    "address": "10600 N Tantau Ave, Cupertino, CA 95014",
    "review_id": "ChdDSUhNMG9nS0VJQ0FnSUMzcDdqMHJRRRAB",
    "reviewer_name": "Krzysztof Wojtczak",
    "reviews_by_reviewer": 32,
    "photos_by_reviewer": "12",
    "reviewer_url": "https://www.google.com/maps/contrib/110797405132582450368/reviews?hl=en",
    "local_guide": true,
    "review_rating": 5,
    "review": "Fajnie można spędzić czas, czilując na tarasie z kawką 🤙",
    "review_date": "2024-11-09T22:18:01.713Z",
    "number_of_likes": 0,
    "response_of_owner": null,
    "response_date": null,
    "photos": [
      "https://lh5.googleusercontent.com/p/AF1QipOtSDFfVpLL5GopXJzoFbTapha0G91nmEx5aSus",
      "https://lh5.googleusercontent.com/p/AF1QipPcr5_TU6MWhAu1_K54DbxywZ4O88Q_qT7NSnhv",
      "https://lh5.googleusercontent.com/p/AF1QipNLM5jHD0iDozGHsax9ydGAWUI_pn_fujQ3Q4Wr",
      "https://lh5.googleusercontent.com/p/AF1QipPcKPwXyHDawuClpTpfV3zE7vMFO0UabmdjX9IG"
    ],
    "timestamp": "2024-11-10T07:37:58.326Z",
    "input": {
      "url": "https://www.google.com/maps/place/Apple+Apple+Park+Visitor+Center/@37.3327772,-122.0079593,17z/data=!4m18!1m9!3m8!1s0x808fb5c5d7e7a3d1:0x1741de234d732f80!2sApple+Apple+Park+Visitor+Center!8m2!3d37.332773!4d-122.0053844!9m1!1b1!16s%2Fg%2F11rjtz4vtg!3m7!1s0x808fb5c5d7e7a3d1:0x1741de234d732f80!8m2!3d37.332773!4d-122.0053844!9m1!1b1!16s%2Fg%2F11rjtz4vtg?entry=ttu",
      "days_limit": 30
    }
  }
```
You can view the full output by downloading [this sample JSON file](https://github.com/luminati-io/Google-Maps-Scraper/blob/main/sample_data/api_scraper_output.json).

**Code Example:**

Here’s a Python script to collect Google Maps reviews and store results in a JSON file:

```python
import requests
import json
import time


class BrightData:
    def __init__(self, api_token):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }

    def collect_reviews(self, urls_data):
        """
        Collect Google Maps reviews using BrightData API
        """
        # 1. Trigger data collection
        print("Starting data collection...")
        trigger_response = self._trigger_collection(urls_data)
        snapshot_id = trigger_response.get("snapshot_id")
        print(f"Snapshot ID: {snapshot_id}")

        # 2. Wait for data to be ready
        print("Waiting for data...")
        while True:
            status = self._check_status(snapshot_id)
            print(f"Status: {status}")

            if status == "ready":
                # Check if data is actually available
                data = self._get_data(snapshot_id)
                if data and len(data) > 0:
                    break
            time.sleep(10)  # Wait 10 seconds before next check

        # 3. Get and save the data
        print("Saving data...")
        filename = f"api_scraper_output.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Data saved to {filename}")
        print(f"✓ Collected {len(data)} reviews")
        return data

    def _trigger_collection(self, urls_data):
        """Trigger data collection"""
        response = requests.post(
            "https://api.brightdata.com/datasets/v3/trigger",
            headers=self.headers,
            params={"dataset_id": "gd_luzfs1dn2oa0teb81",
                    "include_errors": "true"},
            json=urls_data,
        )
        return response.json()

    def _check_status(self, snapshot_id):
        """Check collection status"""
        response = requests.get(
            f"https://api.brightdata.com/datasets/v3/progress/{snapshot_id}",
            headers=self.headers,
        )
        return response.json().get("status")

    def _get_data(self, snapshot_id):
        """Get collected data"""
        response = requests.get(
            f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}",
            headers=self.headers,
            params={"format": "json"},
        )
        return response.json()


if __name__ == "__main__":
    # Initialize with your API token
    brightdata = BrightData("<YOUR_API_TOKEN>")

    # Define URLs to collect reviews from
    urls_to_collect = [
        {
            "url": "https://www.google.com/maps/place/Apple+Apple+Park+Visitor+Center/@37.3327772,-122.0079593,17z/data=!4m18!1m9!3m8!1s0x808fb5c5d7e7a3d1:0x1741de234d732f80!2sApple+Apple+Park+Visitor+Center!8m2!3d37.332773!4d-122.0053844!9m1!1b1!16s%2Fg%2F11rjtz4vtg!3m7!1s0x808fb5c5d7e7a3d1:0x1741de234d732f80!8m2!3d37.332773!4d-122.0053844!9m1!1b1!16s%2Fg%2F11rjtz4vtg?entry=ttu",
            "days_limit": 30,
        },
        {
            "url": "https://www.google.com/maps/place/Joe's+Pizza+Broadway/@40.7546835,-73.989604,17z/data=!3m1!5s0x89c259ab3e91ed73:0x4074c4cfa25e210b!4m8!3m7!1s0x89c259ab3c1ef289:0x3b67a41175949f55!8m2!3d40.7546795!4d-73.9870291!9m1!1b1!16s%2Fg%2F11bw4ws2mt?entry=ttu",
            "days_limit": 25,
        },
    ]

    # Collect reviews
    reviews = brightdata.collect_reviews(urls_to_collect)
```

**How the Code Works:**
1. **API Token Required:** First, you'll need an API token. If you don't have one yet, follow our [Google Maps Scraper API setup guide](https://github.com/luminati-io/Google-Maps-Scraper/blob/main/scraper_api_setup.md#setting-up-google-maps-scraper-api).
2. **Start Data Collection:** Pass your API token to the code, and it will initiate data collection with your specified parameters. This returns a `snapshot_id` that you'll use to track your request.
3. **Wait for Results:** The data collection takes a few minutes to complete. During this time, our code continuously checks the `snapshot_id` status:
    - Status "running" = Data is still being collected
    - Status "ready" = Data collection is complete and saved to your JSON file
4. **Additional Parameters:** You can customize your data collection by adding more parameters to the `_trigger_collection` function. Check the [next section](https://github.com/luminati-io/Google-Maps-Scraper?tab=readme-ov-file#customizing-data-collection-with-api-parameters) to see what parameters are available and learn about different data delivery methods.

### Customizing Data Collection with API Parameters
Use the following API parameters to customize your data collection:

| **Parameter**       | **Type**   | **Description**                                                                                   | **Example**                                           |
|---------------------|------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `limit`             | `integer`  | Limit the number of results returned for each input.                                            | `limit=10`                                           |
| `include_errors`    | `boolean`   | Include an error report in the output for troubleshooting.                                      | `include_errors=true`                                |
| `notify`            | `url`      | URL where a notification is sent once the collection completes.                                  | `notify=https://notify-me.com/`                      |
| `format`            | `enum`     | Format for data delivery. Supported formats: JSON, NDJSON, JSONL, CSV.                          | `format=json`|

💡**Additional delivery methods:** You can choose to deliver the data via [webhook](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/overview#via-webhook) or through the [API](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/overview#via-api).
