## Setting Up Google Maps Scraper API

Follow these steps to set up the Google Maps Scraper API.

1. **Log in to your Bright Data account.** Click on the **Web Scraper API** tab.

2. In the search bar, type **Map** and choose **Google Maps Reviews**.

   <img width="650" alt="bright-data-google-maps-scraper-api-search" src="https://github.com/user-attachments/assets/c4fd4d7c-fb9e-4d00-ba48-4cceb13475ee">

3. Click **Start setting an API call** to start configuring your API.

   <img width="650" alt="bright-data-google-maps-scraper-api-setting-api-call" src="https://github.com/user-attachments/assets/e6dafe83-5a26-4bc1-b6e7-744c055a8e93">

4. Click **Get API Token**  to generate a unique API token.

   <img width="650" alt="bright-data-google-maps-scraper-api-get-api-token" src="https://github.com/user-attachments/assets/01313a95-b494-4222-98fc-80745d18f3f8">

5. Click **Refresh Token** to view your newly created API token.

   <img width="650" alt="bright-data-google-maps-scraper-api-refresh-token" src="https://github.com/user-attachments/assets/a680c95d-9302-4b3d-a839-09325664525b">

6. Save your API token securely. You’ll need it to make API calls.

   <img width="650" alt="bright-data-google-maps-scraper-api-token" src="https://github.com/user-attachments/assets/db459bcb-e21b-49cd-85e4-d34801458bc2">

7. To find **Dataset ID**, go to the **Management APIs** tab.

   <img width="650" alt="bright-data-google-maps-scraper-api-dataset-id" src="https://github.com/user-attachments/assets/15143817-d83e-4273-a015-9d85b9c86b05">

8. In the **Data Collection APIs** tab, use the Add inputs option to add multiple inputs, such as `URL` and `days_limit`. You can also adjust parameters like result limits or error report inclusion.

   <img width="650" alt="bright-data-google-maps-scraper-api-add-inputs" src="https://github.com/user-attachments/assets/13fa3994-2cfd-45ef-84d9-78cf828eebc0">

9. As you adjust parameters, a CURL command will generate on the right. You can use this command to [Trigger Data Collection API](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/trigger-a-collection#request) directly or [pass these parameters](https://github.com/triposat/google-maps?tab=readme-ov-file#customizing-data-collection-with-api-parameters) in the [`_trigger_collection`](https://github.com/triposat/google-maps/blob/main/api-scraper/scraper.py) function in your code.
