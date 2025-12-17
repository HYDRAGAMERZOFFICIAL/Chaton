"""
Receives user question and returns chatbot response
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import json

from backend.config import settings
from backend.database import Database
from backend.ml.predict import IntentPredictor
from backend.knowledge_base.responses import ResponseGenerator
from backend.pipeline.response_selector import ResponseSelector
from backend.pipeline.confidence import ConfidenceChecker
from backend.utils.helpers import format_response, format_error_response, validate_query, sanitize_query
from backend.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter(prefix="/chat", tags=["chat"])

db = Database()
predictor = IntentPredictor()
response_gen = ResponseGenerator()
response_selector = ResponseSelector()
confidence_checker = ConfidenceChecker(settings.CONFIDENCE_THRESHOLD)

models_loaded = False


class QueryRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    user_query: str
    intent: str
    confidence: float
    response: str
    source: str


def initialize_models():
    """Initialize ML models on startup"""
    global models_loaded
    try:
        if predictor.load_models():
            models_loaded = True
            logger.info("Models loaded successfully")
        else:
            logger.warning("Failed to load models, responses will use fallback")
            models_loaded = False
    except Exception as e:
        logger.error(f"Error initializing models: {e}")
        models_loaded = False


@router.on_event("startup")
async def startup_event():
    """Initialize on app startup"""
    initialize_models()


@router.post("/ask", response_model=ChatResponse)
async def ask_question(request: QueryRequest):
    """Process user query and return chatbot response"""
    try:
        user_query = request.message
        is_valid, result = validate_query(user_query)

        if not is_valid:
            raise HTTPException(status_code=400, detail=result)

        user_query = sanitize_query(user_query)

        if not models_loaded:
            raise HTTPException(status_code=503, detail="Models not loaded. Please try again later.")

        intent, confidence = predictor.predict_intent(user_query)

        response_text = response_gen.get_response(intent)
        if not response_text:
            response_text = response_selector.get_random_fallback()

        final_response, source, is_confident = response_selector.select_response(
            intent, response_text, confidence, settings.CONFIDENCE_THRESHOLD
        )

        db.log_chat(user_query, intent, confidence, final_response, source)

        if not is_confident:
            db.log_low_confidence_query(
                user_query, intent, confidence,
                json.dumps(predictor.get_intent_details(user_query))
            )

        return ChatResponse(
            user_query=user_query,
            intent=intent,
            confidence=confidence,
            response=final_response,
            source=source
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/logs")
async def get_chat_logs(limit: int = 50):
    """Get recent chat logs"""
    try:
        logs = db.get_chat_logs(limit)
        return format_response(logs, "success", f"Retrieved {len(logs)} logs")
    except Exception as e:
        logger.error(f"Error getting logs: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/intents")
async def get_available_intents():
    """Get list of available intents"""
    try:
        intents = response_gen.get_all_intents()
        return format_response(intents, "success", f"Retrieved {len(intents)} intents")
    except Exception as e:
        logger.error(f"Error getting intents: {e}")
        raise HTTPException(status_code=500, detail=str(e))
