"""
Simple endpoint to check if backend is running
"""
from fastapi import APIRouter, HTTPException
from backend.config import settings
from backend.database import Database
from backend.utils.helpers import format_response
from pathlib import Path

router = APIRouter(prefix="/health", tags=["health"])
db = Database()


@router.get("/status")
async def health_check():
    """Check if backend is running and healthy"""
    try:
        status_data = {
            "status": "healthy",
            "service": settings.API_TITLE,
            "version": settings.API_VERSION
        }
        return format_response(status_data, "success", "Backend is running")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats")
async def get_stats():
    """Get chatbot statistics"""
    try:
        stats = db.get_statistics()
        return format_response(stats, "success", "Statistics retrieved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/config")
async def get_config():
    """Get API configuration"""
    try:
        config_data = {
            "title": settings.API_TITLE,
            "version": settings.API_VERSION,
            "description": settings.API_DESCRIPTION,
            "confidence_threshold": settings.CONFIDENCE_THRESHOLD
        }
        return format_response(config_data, "success", "Configuration retrieved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
