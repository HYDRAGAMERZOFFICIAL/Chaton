"""
Optional SQLite setup for logs (can be file-based instead)
"""
import sqlite3
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Database:
    def __init__(self, db_path: str = "backend/college_chatbot.db"):
        self.db_path = db_path
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        """Create database and tables if they don't exist"""
        try:
            Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS chat_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    user_query TEXT NOT NULL,
                    intent TEXT,
                    confidence REAL,
                    response TEXT,
                    response_source TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS low_confidence_queries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    user_query TEXT NOT NULL,
                    predicted_intent TEXT,
                    confidence REAL,
                    all_scores TEXT
                )
            ''')

            conn.commit()
            conn.close()
            logger.info(f"Database initialized at {self.db_path}")
        except Exception as e:
            logger.error(f"Error initializing database: {e}")

    def log_chat(self, user_query: str, intent: str, confidence: float,
                 response: str, response_source: str) -> bool:
        """Log a chat interaction"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            timestamp = datetime.now().isoformat()
            cursor.execute('''
                INSERT INTO chat_logs (timestamp, user_query, intent, confidence, response, response_source)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (timestamp, user_query, intent, confidence, response, response_source))

            conn.commit()
            conn.close()
            logger.debug(f"Chat logged: {intent} ({confidence:.2f})")
            return True
        except Exception as e:
            logger.error(f"Error logging chat: {e}")
            return False

    def log_low_confidence_query(self, user_query: str, predicted_intent: str,
                                 confidence: float, all_scores: str) -> bool:
        """Log a low-confidence query for learning"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            timestamp = datetime.now().isoformat()
            cursor.execute('''
                INSERT INTO low_confidence_queries (timestamp, user_query, predicted_intent, confidence, all_scores)
                VALUES (?, ?, ?, ?, ?)
            ''', (timestamp, user_query, predicted_intent, confidence, all_scores))

            conn.commit()
            conn.close()
            logger.info(f"Low-confidence query logged: {user_query}")
            return True
        except Exception as e:
            logger.error(f"Error logging low-confidence query: {e}")
            return False

    def get_chat_logs(self, limit: int = 100) -> List[Dict]:
        """Get recent chat logs"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM chat_logs
                ORDER BY timestamp DESC
                LIMIT ?
            ''', (limit,))

            logs = [dict(row) for row in cursor.fetchall()]
            conn.close()
            return logs
        except Exception as e:
            logger.error(f"Error retrieving chat logs: {e}")
            return []

    def get_statistics(self) -> Dict:
        """Get chatbot statistics"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('SELECT COUNT(*) as total_chats FROM chat_logs')
            total_chats = cursor.fetchone()[0]

            cursor.execute('SELECT COUNT(*) as low_conf FROM low_confidence_queries')
            low_confidence_count = cursor.fetchone()[0]

            cursor.execute('SELECT AVG(confidence) as avg_confidence FROM chat_logs')
            avg_confidence = cursor.fetchone()[0] or 0.0

            conn.close()

            return {
                'total_chats': total_chats,
                'low_confidence_queries': low_confidence_count,
                'average_confidence': round(avg_confidence, 4)
            }
        except Exception as e:
            logger.error(f"Error getting statistics: {e}")
            return {}
