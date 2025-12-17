1️⃣ HARDWARE SUPPORT (MINIMUM)
Component	Requirement
CPU	Dual-core (i3 or equivalent)
RAM	4 GB (2 GB minimum)
Storage	5–10 GB free
GPU	❌ Not required
Internet	Required (for scraping)

✔ CPU-only ML
✔ Works on laptops

2️⃣ OPERATING SYSTEM SUPPORT
Item	Requirement
OS	Windows 10 / Windows 11
Architecture	64-bit
User Rights	Normal user (Admin not mandatory)
3️⃣ SOFTWARE SUPPORT (MANDATORY)
🔹 Python Runtime
Item	Version
Python	3.9 or higher
pip	Latest

✔ Must be added to PATH

🔹 Python Libraries

Installed via requirements.txt

Category	Libraries
Backend	fastapi, uvicorn
UI	streamlit
ML	scikit-learn
NLP	nltk / spacy
Scraping	requests, beautifulsoup4
Utilities	json, pickle
4️⃣ APPLICATION SERVER SUPPORT
Backend Server
Item	Tool
Framework	FastAPI
ASGI Server	Uvicorn
Port	8000

✔ Runs locally
✔ No Apache/Tomcat needed

5️⃣ FRONTEND SUPPORT (PYTHON UI)
Item	Tool
UI Framework	Streamlit
Port	8501
Access	Browser

✔ No HTML/JS required
✔ Python-only UI

6️⃣ ML & NLP SUPPORT
Feature	Support
Model Training	scikit-learn
Inference	CPU
Confidence Score	predict_proba
Text Cleaning	Regex
Tokenization	NLP libs

✔ No GPU
✔ No cloud ML service

7️⃣ AUTO-SCRAPING SUPPORT
Requirement	Details
Internet	Outbound HTTPS
Library	requests, BeautifulSoup
Pages	Public SFGC pages
Frequency	Manual / Scheduled

📌 Windows Task Scheduler can automate this.

8️⃣ DATA STORAGE SUPPORT
Purpose	Tool
Training Data	JSON files
Models	.pkl files
Logs	Text / JSON
Optional DB	SQLite

✔ Database is optional
✔ File-based storage is enough

9️⃣ EXECUTION & AUTOMATION SUPPORT
Item	Tool
Run Script	run.bat
Scheduler	Windows Task Scheduler
Virtual Env	.venv

✔ One-click execution possible

10️⃣ NETWORK SUPPORT
Requirement	Details
Localhost	127.0.0.1
Firewall	Allow Python
Ports	8000, 8501

✔ No external hosting required

11️⃣ OPTIONAL SUPPORT (NOT REQUIRED)
Item	Required?
Docker	❌
Nginx	❌
Linux	❌
Cloud Server	❌
Authentication	❌
🧩 SUPPORT SUMMARY TABLE
Support Type	Needed
Hardware	✅
Windows OS	✅
Python	✅
FastAPI	✅
Streamlit	✅
ML/NLP libs	✅
Scraping tools	✅
Database	❌
Cloud	❌