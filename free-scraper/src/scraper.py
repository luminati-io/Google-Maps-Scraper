import asyncio
import json
from typing import List, Optional
from playwright.async_api import async_playwright, Page, ElementHandle
from src.models import ReviewData


class ReviewsScraper:
    async def init_browser(self) -> tuple:
        """Initialize browser and page"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()
        return self.playwright, self.browser, self.page

    async def extract_review_data(self, review_element: ElementHandle) -> Optional[ReviewData]:
        """Extract data from a single review"""
        try:
            # Extract reviewer name
            name_element = await review_element.query_selector(".d4r55")
            reviewer_name = await name_element.inner_text() if name_element else ""

            # Extract reviewer link
            link_element = await review_element.query_selector("button[data-href]")
            reviewer_link = await link_element.get_attribute("data-href") if link_element else ""

            # Extract reviewer image
            img_element = await review_element.query_selector(".NBa7we")
            reviewer_image = await img_element.get_attribute("src") if img_element else ""

            # Extract rating (count the filled stars)
            stars = await review_element.query_selector_all(".hCCjke.google-symbols.NhBTye.elGi1d")
            rating = len(stars)

            # Extract date
            date_element = await review_element.query_selector(".rsqaWe")
            date = await date_element.inner_text() if date_element else ""

            # Extract review text
            text_element = await review_element.query_selector(".wiI7pd")
            text = await text_element.inner_text() if text_element else ""

            # Click "More" button if it exists to get full text
            more_button = await review_element.query_selector("button.w8nwRe.kyuRq")
            if more_button:
                await more_button.click()
                await asyncio.sleep(1)  # Wait for text to expand
                text_element = await review_element.query_selector(".wiI7pd")
                text = await text_element.inner_text() if text_element else text

            # Extract photos
            photos = []
            photo_elements = await review_element.query_selector_all(".Tya61d")
            for photo in photo_elements:
                style = await photo.get_attribute("style")
                if style and "url(" in style:
                    url = style.split('url("')[1].split('")')[0]
                    photos.append(url)

            # Extract likes count
            likes_element = await review_element.query_selector(".pkWtMe")
            likes_count = await likes_element.inner_text() if likes_element else "0"

            return ReviewData(
                reviewer_name=reviewer_name,
                reviewer_link=reviewer_link,
                reviewer_image=reviewer_image,
                rating=rating,
                date=date,
                text=text,
                photos=photos,
                likes_count=likes_count,
            )
        except Exception as e:
            print(f"Error extracting review data: {str(e)}")
            return None

    async def scroll_reviews(self, page: Page) -> bool:
        """Scroll the reviews panel and wait for new content"""
        try:
            reviews_container = await page.query_selector('div[role="feed"]')
            if not reviews_container:
                return False

            # Get current height
            prev_height = await reviews_container.evaluate("(element) => element.scrollHeight")
            
            # Scroll to bottom
            await reviews_container.evaluate("(element) => element.scrollTo(0, element.scrollHeight)")
            
            # Wait for possible new content
            await asyncio.sleep(2)
            
            # Check if new content loaded
            new_height = await reviews_container.evaluate("(element) => element.scrollHeight")
            return new_height > prev_height

        except Exception as e:
            print(f"Error during scrolling: {e}")
            return False

    async def scrape_reviews(self, url: str) -> List[ReviewData]:
        """Scrape all reviews from a single URL"""
        playwright, browser, page = await self.init_browser()
        reviews = []
        processed_review_ids = set()

        try:
            clean_url = url.split("/@")[0]
            print(f"\nScraping reviews from: {clean_url}")
            await page.goto(url)
            await page.wait_for_selector(".jftiEf", timeout=10000)

            no_new_reviews_count = 0
            while no_new_reviews_count < 3:  # Stop after 3 attempts with no new reviews
                # Get current review elements
                review_elements = await page.query_selector_all(".jftiEf")
                initial_count = len(processed_review_ids)
                
                # Process visible reviews
                for review in review_elements:
                    review_id = await review.get_attribute("data-review-id")
                    if review_id and review_id not in processed_review_ids:
                        review_data = await self.extract_review_data(review)
                        if review_data:
                            reviews.append(review_data)
                            processed_review_ids.add(review_id)
                            print(f"Scraped review by {review_data.reviewer_name} ({len(reviews)} total)")
                
                # Check if we got new reviews
                if len(processed_review_ids) == initial_count:
                    no_new_reviews_count += 1
                    print(f"No new reviews found (attempt {no_new_reviews_count}/3)")
                else:
                    no_new_reviews_count = 0
                
                # Scroll for more reviews
                more_content = await self.scroll_reviews(page)
                if not more_content:
                    print("No more content to load")
                    break
                    
                await asyncio.sleep(1)

        except Exception as e:
            print(f"Error during scraping: {e}")
        finally:
            await browser.close()
            await playwright.stop()

        return reviews

    async def scrape_multiple_places(self, urls: List[str]) -> List[ReviewData]:
        """Scrape reviews from multiple URLs"""
        all_reviews = []
        for url in urls:
            reviews = await self.scrape_reviews(url)
            all_reviews.extend(reviews)
            print(f"Completed scraping {len(reviews)} reviews from current URL")
        return all_reviews

    def save_reviews(self, reviews: List[ReviewData], filename: str = None):
        """Save reviews to a JSON file"""
        if filename is None:
            filename = f"free_scraper_output.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                [self._review_to_dict(review) for review in reviews],
                f,
                indent=4,
                ensure_ascii=False
            )
        print(f"\nSaved {len(reviews)} reviews to {filename}")

    def _review_to_dict(self, review: ReviewData) -> dict:
        """Convert ReviewData to dictionary for JSON serialization"""
        return {
            "reviewer_name": review.reviewer_name,
            "reviewer_link": review.reviewer_link,
            "reviewer_image": review.reviewer_image,
            "rating": review.rating,
            "date": review.date,
            "text": review.text,
            "photos": review.photos,
            "likes_count": review.likes_count
        }