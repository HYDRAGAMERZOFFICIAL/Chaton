PROJECT INFORMATION
🔹 Project Title

AI-Based College Information Chatbot Using NLP, Machine Learning and Web Scraping (SFGC Case Study)

🔹 Project Category

Artificial Intelligence / Machine Learning / Natural Language Processing

🔹 Project Type

Academic Mini / Major Project (Python-based, Windows-compatible)

🔹 Problem Statement

In colleges, students and parents frequently have queries related to admissions, courses, fees, facilities, and contact details. These queries are usually handled manually by administrative staff, which is time-consuming and inefficient. There is a need for an automated system that can provide accurate and instant responses using official college information.

🔹 Proposed Solution

The proposed system is an AI-powered chatbot that automatically answers college-related queries by:

Scraping official information from sfgc.ac.in

Training a Machine Learning model for intent classification

Using Natural Language Processing (NLP) to understand user queries

Providing responses with confidence-based fallback logic

The system runs entirely on Python and works on Windows OS.

🔹 Project Objectives

To build an intelligent chatbot for college-related queries

To use NLP for understanding natural language questions

To implement ML-based intent classification

To automatically extract training data from the college website

To provide accurate responses with confidence scoring

To reduce manual workload in college information handling

🔹 Scope of the Project

Handles queries related to:

College overview

Courses offered

Admission process

Contact details

Facilities (as available on the website)

Works as a 24/7 information assistant

Designed for students, parents, and visitors

Can be extended to other colleges easily

🔹 System Users

Prospective students

Existing students

Parents

General public

(No login or authentication required)

🔹 Technologies Used
Programming Language

Python 3.9+

Backend

FastAPI

Uvicorn

Frontend

Streamlit (Python-based UI)

Machine Learning & NLP

scikit-learn

NLP preprocessing (tokenization, lemmatization)

TF-IDF Vectorization

Logistic Regression (Intent Classification)

Web Scraping

Requests

BeautifulSoup

Data Storage

JSON files

Pickle (.pkl) for trained models

Optional SQLite for logs

Platform

Windows 10 / 11

🔹 System Architecture (Brief)

User enters a query through the chatbot UI

NLP module preprocesses the input

ML model predicts the intent and confidence score

If confidence is high, a response is fetched from the knowledge base

If confidence is low, a fallback response is returned

Low-confidence queries are logged for future learning

🔹 Key Features

AI-based query understanding

Automated website scraping

ML-driven intent classification

Confidence score & fallback mechanism

Python-only implementation

Windows-compatible execution

Modular and scalable architecture

🔹 Advantages of the System

Instant response to user queries

Reduces human effort

Uses official college data

Easy to maintain and update

Lightweight and cost-effective

No special hardware required

🔹 Limitations

Accuracy depends on training data quality

Limited to information available on the website

No voice or multilingual support (can be added later)

🔹 Future Enhancements

Multilingual chatbot support

Voice-based interaction

Scheduled automatic retraining

Integration with mobile apps

Expansion to ERP/LMS systems

🔹 Conclusion

This project demonstrates the practical application of AI, Machine Learning, and NLP in solving real-world problems in the education domain. The chatbot provides an efficient, scalable, and automated solution for handling college-related queries using official web data.