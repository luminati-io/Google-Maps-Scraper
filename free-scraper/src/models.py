from dataclasses import dataclass
from typing import List


@dataclass
class ReviewData:
    """Data structure for storing review information"""
    reviewer_name: str
    reviewer_link: str
    reviewer_image: str
    rating: int
    date: str
    text: str
    photos: List[str]
    likes_count: str