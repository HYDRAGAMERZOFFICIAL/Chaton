"""
Logging helper
"""
import logging
import logging.handlers
from pathlib import Path
from backend.config import settings


def setup_logger(name: str, log_file: str = None, level: str = "INFO"):
    """Setup logging for a module"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        if log_file:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            file_handler = logging.handlers.RotatingFileHandler(
                log_file,
                maxBytes=10485760,
                backupCount=5
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger


def get_logger(name: str):
    """Get a logger instance"""
    return setup_logger(name, str(settings.LOG_FILE), settings.LOG_LEVEL)
