"""
Common utility functions
"""
import json
from datetime import datetime
from typing import Any, Dict, List


def format_response(data: Any, status: str = "success", message: str = "") -> Dict:
    """Format API response"""
    return {
        "status": status,
        "message": message,
        "data": data,
        "timestamp": datetime.now().isoformat()
    }


def format_error_response(error_message: str, status_code: int = 400) -> Dict:
    """Format error response"""
    return {
        "status": "error",
        "message": error_message,
        "timestamp": datetime.now().isoformat()
    }


def validate_query(query: str, min_length: int = 2) -> tuple:
    """Validate user query"""
    if not query:
        return False, "Query cannot be empty"

    query = query.strip()
    if len(query) < min_length:
        return False, f"Query must be at least {min_length} characters long"

    if len(query) > 500:
        return False, "Query is too long (max 500 characters)"

    return True, query


def sanitize_query(query: str) -> str:
    """Sanitize user query"""
    query = query.strip()
    query = query.replace('\n', ' ').replace('\r', ' ')
    query = ' '.join(query.split())
    return query


def get_timestamp() -> str:
    """Get current timestamp"""
    return datetime.now().isoformat()


def batch_queries(queries: List[str], batch_size: int = 10) -> List[List[str]]:
    """Batch queries for batch processing"""
    return [queries[i:i + batch_size] for i in range(0, len(queries), batch_size)]


def format_confidence(confidence: float) -> str:
    """Format confidence as percentage"""
    return f"{confidence * 100:.2f}%"


def get_intent_badge(intent: str) -> str:
    """Get emoji badge for intent"""
    badges = {
        'admissions': '🎓',
        'courses': '📚',
        'faculty': '👨‍🏫',
        'contact': '📞',
        'about': 'ℹ️',
        'academics': '🏫',
        'general': '💬'
    }
    return badges.get(intent, '🤖')


def json_to_dict(json_str: str) -> Dict:
    """Convert JSON string to dictionary"""
    try:
        return json.loads(json_str)
    except Exception:
        return {}


def dict_to_json(data: Dict) -> str:
    """Convert dictionary to JSON string"""
    return json.dumps(data, ensure_ascii=False, indent=2)
