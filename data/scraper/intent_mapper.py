"""
Converts website text into chatbot intents
"""
import json
import logging
from typing import Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IntentMapper:
    def __init__(self):
        self.intent_patterns = {
            'admissions': ['admission', 'apply', 'enrollment', 'registration', 'how to apply', 'requirements'],
            'courses': ['course', 'program', 'curriculum', 'degree', 'subject', 'syllabus'],
            'faculty': ['faculty', 'professor', 'staff', 'teacher', 'instructor', 'department'],
            'contact': ['contact', 'email', 'phone', 'address', 'location', 'get in touch'],
            'about': ['about', 'history', 'mission', 'vision', 'college', 'institution'],
            'academics': ['academics', 'learning', 'education', 'study', 'classes', 'semester'],
        }

    def detect_intent(self, text: str) -> str:
        """Detect intent from text based on keywords"""
        if not text:
            return 'general'

        text_lower = text.lower()

        for intent, keywords in self.intent_patterns.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return intent

        return 'general'

    def create_intent_object(self, page_data: Dict, intent: str) -> Dict:
        """Create an intent object from parsed page data"""
        return {
            'intent': intent,
            'patterns': [
                page_data.get('title', ''),
            ] + page_data.get('sentences', [])[:3],
            'responses': [
                page_data.get('content', '')
            ],
            'context': {
                'url': page_data.get('url', ''),
                'page_type': page_data.get('page_type', ''),
                'keywords': page_data.get('keywords', [])
            }
        }

    def map_pages_to_intents(self, parsed_pages: List[Dict]) -> List[Dict]:
        """Convert parsed pages to intent format"""
        intents = {}

        for page in parsed_pages:
            intent = self.detect_intent(page.get('content', ''))

            intent_obj = self.create_intent_object(page, intent)

            if intent not in intents:
                intents[intent] = {
                    'intent': intent,
                    'patterns': [],
                    'responses': [],
                    'context': []
                }

            intents[intent]['patterns'].extend(intent_obj['patterns'])
            intents[intent]['responses'].extend(intent_obj['responses'])
            intents[intent]['context'].append(intent_obj['context'])

        return list(intents.values())

    def save_intents(self, intents: List[Dict], filename: str) -> None:
        """Save intents to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(intents, f, indent=2, ensure_ascii=False)
            logger.info(f"Intents saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving intents: {e}")

    def process(self, parsed_pages: List[Dict], output_file: str) -> List[Dict]:
        """Process pages and save intents"""
        intents = self.map_pages_to_intents(parsed_pages)
        self.save_intents(intents, output_file)
        logger.info(f"Mapped {len(intents)} intents")
        return intents
