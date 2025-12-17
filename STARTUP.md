# SFGC AI College Chatbot - Startup Guide

## Quick Start (Recommended)

**Windows Users**: Double-click `run.bat`

This will automatically:
1. Check dependencies
2. Train the ML model
3. Start the backend API (port 8000)
4. Launch the frontend UI (port 8501)

---

## Manual Startup (Step-by-Step)

### Prerequisites
- Python 3.9 or higher
- Windows OS
- ~500MB free disk space

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Train the ML Model

```bash
python train_model.py
```

You should see:
```
============================================================
SFGC Chatbot - Model Training Pipeline
============================================================

[Step 1/4] Importing dependencies...
[Step 2/4] Loading training data...
[Step 3/4] Feature Engineering (TF-IDF Vectorization)...
[Step 4/4] Training ML Model (Multinomial Naive Bayes)...

✅ TRAINING COMPLETED SUCCESSFULLY!
============================================================
```

### Step 3: Start Backend API

**Terminal 1:**
```bash
cd backend
python main.py
```

You should see:
```
INFO:__main__:Starting SFGC Chatbot API v1.0.0
Uvicorn running on http://0.0.0.0:8000
```

Then open your browser to:
- **Main API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health/status

### Step 4: Start Frontend UI

**Terminal 2:**
```bash
cd frontend
streamlit run app.py
```

You should see:
```
You can now view your Streamlit app in your browser.

URL: http://localhost:8501
```

---

## Verification Scripts

### Test Imports
```bash
python test_imports.py
```
Verifies all module imports are working correctly.

### Test Backend
```bash
python test_backend.py
```
Verifies backend can load and perform inference.

---

## API Endpoints

### Health Checks
- `GET /` - Welcome message
- `GET /health/status` - API status
- `GET /health/stats` - Chatbot statistics
- `GET /health/config` - API configuration

### Chat
- `POST /chat/ask` - Send a message to the chatbot
  ```json
  Request: {"message": "What courses do you offer?"}
  Response: {
    "user_query": "What courses do you offer?",
    "intent": "academics",
    "confidence": 0.87,
    "response": "Our academic programs...",
    "source": "knowledge_base"
  }
  ```

- `GET /chat/logs` - View chat history
- `GET /chat/intents` - View available intents

---

## Troubleshooting

### Port Already In Use
If port 8000 or 8501 is already in use:

**For Backend (Change port):**
```bash
cd backend
python -m uvicorn main:app --port 8001
```
Then update `frontend/app.py` line 16:
```python
API_BASE_URL = "http://localhost:8001"
```

**For Frontend:**
```bash
cd frontend
streamlit run app.py --server.port 8502
```

### Models Not Found
Train the model first:
```bash
python train_model.py
```

### Dependencies Not Installed
Upgrade pip and retry:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Python Not Found
Make sure Python 3.9+ is installed and in your PATH:
```bash
python --version
```

---

## Available Intents

The chatbot recognizes these intents:

1. **about** - Information about the college
2. **academics** - Academic programs and courses
3. **admissions** - Admission process and requirements
4. **contact** - Contact information
5. **general** - General questions

---

## Training Your Own Model

To retrain with new data:

1. Update `backend/knowledge_base/sfgc_intents.json` with new patterns
2. Run:
   ```bash
   python train_model.py
   ```
3. Restart backend API

To evaluate model performance:
```bash
python -c "from backend.ml.evaluator import ModelEvaluator; ModelEvaluator().load_and_evaluate_full()"
```

---

## File Structure

```
Chaton/
├── train_model.py              # Train ML model
├── test_imports.py             # Verify imports
├── test_backend.py             # Test backend
├── run.bat                      # Automated startup script
├── backend/                     # FastAPI backend
│   ├── main.py                 # Entry point
│   ├── config.py               # Configuration
│   ├── database.py             # SQLite database
│   ├── models/                 # Trained model files
│   ├── api/                    # API endpoints
│   ├── ml/                     # ML models (train, predict, evaluate)
│   ├── nlp/                    # NLP processing
│   ├── pipeline/               # Data pipeline
│   ├── knowledge_base/         # Training data
│   ├── utils/                  # Utilities
│   └── logs/                   # Chat logs
├── frontend/                    # Streamlit UI
│   ├── app.py                  # Main UI
│   └── ui_components.py        # UI components
├── data/                        # Raw data
│   ├── raw/                    # Scraped website data
│   ├── processed/              # Processed training data
│   └── scraper/                # Web scraper
├── tests/                       # Unit tests
├── requirements.txt            # Dependencies
└── README.md                   # Full documentation
```

---

## Next Steps

1. **Customize Training Data**: Update intents in `backend/knowledge_base/sfgc_intents.json`
2. **Retrain Model**: Run `python train_model.py`
3. **Monitor Performance**: Check logs in `backend/logs/`
4. **View Analytics**: Use frontend statistics dashboard
5. **Scale Deployment**: See README.md for production deployment

---

## Support

For detailed documentation, see: **README.md**

For development phases, see: **phase.md**

---

**Ready to run!** Start with:
```bash
run.bat
```
