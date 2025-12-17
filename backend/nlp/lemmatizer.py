"""
Converts words to base form (running → run)
"""
import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SimpleLemmatizer:
    def __init__(self):
        self.lemma_rules = {
            'running': 'run',
            'ran': 'run',
            'runs': 'run',
            'walking': 'walk',
            'walked': 'walk',
            'walks': 'walk',
            'studies': 'study',
            'studied': 'study',
            'studying': 'study',
            'goes': 'go',
            'going': 'go',
            'went': 'go',
            'admission': 'admit',
            'admissions': 'admit',
            'admitted': 'admit',
            'courses': 'course',
            'coursework': 'course',
            'faculty': 'faculty',
            'faculties': 'faculty',
            'academics': 'academic',
            'academic': 'academic',
            'education': 'educate',
            'educational': 'educate',
            'engineers': 'engineer',
            'engineering': 'engineer',
            'engineering': 'engineer',
            'learning': 'learn',
            'learned': 'learn',
            'learns': 'learn',
            'developing': 'develop',
            'developed': 'develop',
            'development': 'develop',
            'develops': 'develop',
        }

        self.suffix_rules = [
            ('ies', 'y'),
            ('es', ''),
            ('s', ''),
            ('ed', ''),
            ('ing', ''),
        ]

    def lemmatize_word(self, word: str) -> str:
        """Lemmatize a single word"""
        if not word:
            return word

        word_lower = word.lower()

        if word_lower in self.lemma_rules:
            return self.lemma_rules[word_lower]

        for suffix, replacement in self.suffix_rules:
            if word_lower.endswith(suffix):
                root = word_lower[:-len(suffix)] + replacement
                if len(root) > 2:
                    return root

        return word_lower

    def lemmatize_text(self, text: str) -> str:
        """Lemmatize all words in text"""
        if not text:
            return ''

        words = text.split()
        lemmatized_words = [self.lemmatize_word(word) for word in words]

        return ' '.join(lemmatized_words)

    def lemmatize_tokens(self, tokens: List[str]) -> List[str]:
        """Lemmatize a list of tokens"""
        return [self.lemmatize_word(token) for token in tokens]

    def get_lemma_mapping(self, words: List[str]) -> Dict[str, str]:
        """Get lemma mapping for words"""
        return {word: self.lemmatize_word(word) for word in words}
