"""
Cleans input text (lowercase, remove symbols)
"""
import re
import string
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TextPreprocessor:
    def __init__(self):
        self.patterns = {
            'urls': re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'),
            'emails': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'numbers': re.compile(r'\b\d+\b'),
            'extra_whitespace': re.compile(r'\s+'),
            'punctuation': re.compile(f'[{re.escape(string.punctuation)}]'),
        }

    def to_lowercase(self, text: str) -> str:
        """Convert text to lowercase"""
        return text.lower()

    def remove_urls(self, text: str) -> str:
        """Remove URLs from text"""
        return self.patterns['urls'].sub('', text)

    def remove_emails(self, text: str) -> str:
        """Remove email addresses from text"""
        return self.patterns['emails'].sub('', text)

    def remove_extra_whitespace(self, text: str) -> str:
        """Remove extra whitespace and newlines"""
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        text = self.patterns['extra_whitespace'].sub(' ', text)
        return text.strip()

    def remove_punctuation(self, text: str, keep_important: bool = False) -> str:
        """Remove punctuation from text"""
        if keep_important:
            important_punctuation = {'?', '!', '.'}
            return ''.join(
                char if char not in string.punctuation or char in important_punctuation else ' '
                for char in text
            )
        return self.patterns['punctuation'].sub(' ', text)

    def remove_numbers(self, text: str) -> str:
        """Remove numbers from text"""
        return self.patterns['numbers'].sub('', text)

    def remove_special_characters(self, text: str) -> str:
        """Remove special characters"""
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)

    def clean_text(self, text: str, remove_numbers: bool = False, 
                   keep_punctuation: bool = False) -> str:
        """Complete text cleaning pipeline"""
        if not text:
            return ''

        text = self.to_lowercase(text)
        text = self.remove_urls(text)
        text = self.remove_emails(text)
        text = self.remove_extra_whitespace(text)
        text = self.remove_punctuation(text, keep_important=keep_punctuation)

        if remove_numbers:
            text = self.remove_numbers(text)

        text = self.remove_extra_whitespace(text)
        return text.strip()

    def preprocess_batch(self, texts: List[str], remove_numbers: bool = False) -> List[str]:
        """Preprocess multiple texts"""
        return [self.clean_text(text, remove_numbers) for text in texts]
