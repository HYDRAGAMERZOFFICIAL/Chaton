AI_Chatbot\
│
├── backend\
│   ├── main.py                     # FastAPI entry point
│   ├── config.py                   # App settings, thresholds
│   ├── database.py                 # SQLite / logs
│
│   ├── api\
│   │   ├── chat_api.py             # /ask endpoint
│   │   └── health.py               # Health check
│
│   ├── nlp\
│   │   ├── preprocess.py           # Text cleaning
│   │   ├── tokenizer.py            # Tokenization
│   │   └── lemmatizer.py            # Lemmatization
│
│   ├── ml\
│   │   ├── train.py                # Model training
│   │   ├── predict.py              # Intent + confidence
│   │   ├── evaluator.py            # Accuracy metrics
│   │   └── retrain.py              # Retraining
│
│   ├── pipeline\
│   │   ├── data_loader.py          # Load dataset
│   │   ├── feature_engineering.py  # TF-IDF
│   │   ├── confidence.py           # Confidence scoring
│   │   └── response_selector.py    # Final reply logic
│
│   ├── knowledge_base\
│   │   ├── sfgc_intents.json       # Training data
│   │   ├── responses.py            # Intent → response
│   │   └── fallback.json           # Safe replies
│
│   ├── models\
│   │   ├── intent_model.pkl
│   │   └── vectorizer.pkl
│
│   ├── logs\
│   │   ├── chat_logs.txt
│   │   └── low_confidence_queries.json
│
│   └── utils\
│       ├── logger.py
│       └── helpers.py
│
├── data\
│   ├── scraper\
│   │   ├── scrape_sfgc.py           # Website scraper
│   │   ├── page_parser.py           # Clean scraped text
│   │   └── intent_mapper.py         # Website → intents
│   │
│   ├── raw\
│   │   └── scraped_sfgc_data.json
│   │
│   └── processed\
│       └── sfgc_intents.json
│
├── frontend\
│   ├── app.py                       # Streamlit UI
│   └── ui_components.py
│
├── tests\
│   ├── test_scraper.py
│   ├── test_nlp.py
│   ├── test_ml.py
│   └── test_api.py
│
├── requirements.txt
├── README.md
├── run.bat                          # Windows run script
└── .venv\                           # Virtual environment
