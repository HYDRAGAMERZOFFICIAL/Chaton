📁 ROOT LEVEL FILES
File	Purpose
README.md	Project overview, setup steps, run instructions
requirements.txt	All Python dependencies required to run the system
run.bat	Windows batch file to run scraping → training → backend → UI
.venv/	Python virtual environment (created locally)
📁 BACKEND FOLDER

📂 backend\
Handles API, AI logic, ML inference, NLP processing

🔹 Core Backend Files
File	Purpose
main.py	Entry point of FastAPI server; starts backend
config.py	Global configurations (confidence threshold, paths)
database.py	Optional SQLite setup for logs (can be file-based instead)
📁 API Layer

📂 backend\api\

File	Purpose
chat_api.py	Receives user question and returns chatbot response
health.py	Simple endpoint to check if backend is running
📁 NLP Layer

📂 backend\nlp\
Responsible for text understanding

File	Purpose
preprocess.py	Cleans input text (lowercase, remove symbols)
tokenizer.py	Splits sentences into words
lemmatizer.py	Converts words to base form (running → run)
📁 ML Layer

📂 backend\ml\
Responsible for learning and prediction

File	Purpose
train.py	Trains ML intent classification model
predict.py	Predicts intent + confidence score
evaluator.py	Evaluates accuracy, precision (optional)
retrain.py	Retrains model using new data
📁 AI PIPELINE

📂 backend\pipeline\
Connects NLP → ML → Response

File	Purpose
data_loader.py	Loads processed training data
feature_engineering.py	Converts text to TF-IDF vectors
confidence.py	Checks confidence threshold
response_selector.py	Chooses final response or fallback
📁 KNOWLEDGE BASE

📂 backend\knowledge_base\
Contains college knowledge

File	Purpose
sfgc_intents.json	Final training dataset (intent + patterns + response)
responses.py	Maps intent → official answer
fallback.json	Safe replies when confidence is low
📁 MODEL STORAGE

📂 backend\models\

File	Purpose
intent_model.pkl	Trained ML model
vectorizer.pkl	TF-IDF vectorizer used by model
📁 LOGS

📂 backend\logs\

File	Purpose
chat_logs.txt	Stores all user–bot conversations
low_confidence_queries.json	Stores unclear questions for learning
📁 UTILITIES

📂 backend\utils\

File	Purpose
logger.py	Logging helper
helpers.py	Common utility functions
📁 DATA FOLDER

📂 data\
Handles scraping and dataset generation

📁 SCRAPER

📂 data\scraper\

File	Purpose
scrape_sfgc.py	Scrapes public pages of sfgc.ac.in
page_parser.py	Cleans scraped HTML text
intent_mapper.py	Converts website text into chatbot intents
📁 RAW DATA

📂 data\raw\

File	Purpose
scraped_sfgc_data.json	Raw text scraped from website
📁 PROCESSED DATA

📂 data\processed\

File	Purpose
sfgc_intents.json	Clean, ML-ready training dataset
📁 FRONTEND

📂 frontend\
Python-based User Interface

File	Purpose
app.py	Streamlit chatbot UI
ui_components.py	UI helper components
📁 TESTS

📂 tests\
Used for validation (optional)

File	Purpose
test_scraper.py	Tests scraping logic
test_nlp.py	Tests NLP preprocessing
test_ml.py	Tests ML predictions
test_api.py	Tests backend endpoints
🧠 COMPLETE DATA FLOW (FILE-LEVEL)
scrape_sfgc.py
 → scraped_sfgc_data.json
 → page_parser.py
 → intent_mapper.py
 → sfgc_intents.json
 → train.py
 → intent_model.pkl
 → predict.py
 → chat_api.py
 → app.py