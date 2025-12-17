"""Quick test to verify backend can start"""
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    print("Testing backend imports...")
    from backend.main import app
    print("[OK] Backend app imported successfully")
    
    print("\nTesting API routes...")
    from backend.api import health, chat_api
    print("[OK] API routes imported successfully")
    
    print("\nTesting ML model loading...")
    from backend.ml.predict import IntentPredictor
    predictor = IntentPredictor()
    if predictor.load_models():
        print("[OK] ML models loaded successfully")
    else:
        print("[FAIL] Failed to load ML models")
        sys.exit(1)
    
    print("\nTesting inference...")
    intent, confidence = predictor.predict_intent("Tell me about the college")
    print("[OK] Prediction test: intent=" + intent + ", confidence=" + f"{confidence:.4f}")
    
    print("\n[SUCCESS] All backend tests passed!")
    print("\nBackend is ready to run with:")
    print("  python backend/main.py")
    print("  or")
    print("  uvicorn backend.main:app --host 0.0.0.0 --port 8000")
    
except Exception as e:
    print("[ERROR] Error: " + str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)
