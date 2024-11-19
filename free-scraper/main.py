import asyncio
from src.scraper import ReviewsScraper

async def main():
    # List of URLs to scrape
    urls = [
        "https://www.google.com/maps/place/Joe's+Pizza+Broadway/@40.7546835,-73.989604,17z/data=!3m1!5s0x89c259ab3e91ed73:0x4074c4cfa25e210b!4m8!3m7!1s0x89c259ab3c1ef289:0x3b67a41175949f55!8m2!3d40.7546795!4d-73.9870291!9m1!1b1!16s%2Fg%2F11bw4ws2mt?entry=ttu",
        "https://www.google.com/maps/place/Googleplex/@37.4220583,-122.0878991,17z/data=!4m8!3m7!1s0x808fba02425dad8f:0x6c296c66619367e0!8m2!3d37.4220541!4d-122.0853242!9m1!1b1!16zL20vMDNiYnkx?hl=en&entry=ttu",
        "https://www.google.com/maps/place/Apple+Apple+Park+Visitor+Center/@37.3327772,-122.0079593,17z/data=!4m18!1m9!3m8!1s0x808fb5c5d7e7a3d1:0x1741de234d732f80!2sApple+Apple+Park+Visitor+Center!8m2!3d37.332773!4d-122.0053844!9m1!1b1!16s%2Fg%2F11rjtz4vtg!3m7!1s0x808fb5c5d7e7a3d1:0x1741de234d732f80!8m2!3d37.332773!4d-122.0053844!9m1!1b1!16s%2Fg%2F11rjtz4vtg?entry=ttu"
        # Add more URLs here
    ]

    scraper = ReviewsScraper()
    
    # Scrape all reviews
    all_reviews = await scraper.scrape_multiple_places(urls)
    
    # Save to JSON file
    scraper.save_reviews(all_reviews)

if __name__ == "__main__":
    asyncio.run(main())