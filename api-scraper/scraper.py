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
