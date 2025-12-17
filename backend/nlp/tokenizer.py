"""
Splits sentences into words
"""
import re
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Tokenizer:
    def __init__(self):
        self.word_pattern = re.compile(r'\b\w+\b')
        self.sentence_pattern = re.compile(r'[.!?]+')

    def tokenize_words(self, text: str) -> List[str]:
        """Split text into words"""
        if not text:
            return []

        words = self.word_pattern.findall(text.lower())
        return words

    def tokenize_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        if not text:
            return []

        sentences = re.split(r'(?<=[.!?])\s+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        return sentences

    def tokenize_ngrams(self, text: str, n: int = 2) -> List[str]:
        """Generate n-grams from text"""
        if not text or n < 1:
            return []

        words = self.tokenize_words(text)
        ngrams = [' '.join(words[i:i+n]) for i in range(len(words) - n + 1)]

        return ngrams

    def get_unique_tokens(self, text: str) -> List[str]:
        """Get unique tokens from text"""
        tokens = self.tokenize_words(text)
        return list(set(tokens))

    def tokenize_batch(self, texts: List[str]) -> List[List[str]]:
        """Tokenize multiple texts"""
        return [self.tokenize_words(text) for text in texts]

    def get_vocabulary(self, texts: List[str]) -> List[str]:
        """Build vocabulary from multiple texts"""
        all_tokens = []
        for text in texts:
            all_tokens.extend(self.tokenize_words(text))

        return sorted(list(set(all_tokens)))
