"""
Cleans scraped HTML text
"""
import re
import logging
from typing import Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PageParser:
    def __init__(self):
        self.patterns = {
            'extra_whitespace': re.compile(r'\s+'),
            'special_chars': re.compile(r'[^\w\s\-\.]'),
            'urls': re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'),
        }

    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        if not text:
            return ''

        text = text.strip()
        text = self.patterns['extra_whitespace'].sub(' ', text)
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

        return text.strip()

    def extract_sentences(self, text: str) -> List[str]:
        """Extract sentences from text"""
        if not text:
            return []

        sentences = re.split(r'(?<=[.!?])\s+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        return sentences

    def extract_keywords(self, text: str, min_length: int = 3) -> List[str]:
        """Extract meaningful keywords from text"""
        if not text:
            return []

        words = text.lower().split()
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those'
        }

        keywords = [
            w for w in words
            if len(w) >= min_length and w not in stop_words and w.isalpha()
        ]

        return list(set(keywords))

    def parse_page(self, page_data: Dict) -> Dict:
        """Parse and clean a page"""
        try:
            cleaned_data = {
                'url': page_data.get('url', ''),
                'page_type': page_data.get('page_type', ''),
                'title': self.clean_text(page_data.get('title', '')),
                'content': self.clean_text(page_data.get('content', '')),
                'sentences': [],
                'keywords': [],
                'links': page_data.get('links', [])
            }

            if cleaned_data['content']:
                cleaned_data['sentences'] = self.extract_sentences(cleaned_data['content'])
                cleaned_data['keywords'] = self.extract_keywords(cleaned_data['content'])

            return cleaned_data
        except Exception as e:
            logger.error(f"Error parsing page: {e}")
            return None

    def parse_multiple_pages(self, pages_data: List[Dict]) -> List[Dict]:
        """Parse multiple pages"""
        parsed_pages = []
        for page in pages_data:
            parsed = self.parse_page(page)
            if parsed:
                parsed_pages.append(parsed)

        logger.info(f"Parsed {len(parsed_pages)} pages")
        return parsed_pages
