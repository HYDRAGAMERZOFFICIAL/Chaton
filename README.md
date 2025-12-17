PROJECT OVERVIEW

The AI-Based College Information Chatbot is an intelligent system designed to automatically answer queries related to a college using Natural Language Processing (NLP) and Machine Learning (ML) techniques. The system acts as a virtual assistant that provides instant and accurate information regarding admissions, courses, facilities, and general college details.

The chatbot uses official data extracted from the college website (sfgc.ac.in) through an automated web scraping mechanism. This data is processed, structured, and used to train an ML-based intent classification model. When a user asks a question, the system analyzes the query, identifies the user’s intent, and responds with the most relevant answer.

The application is developed entirely using Python and is designed to run on Windows operating systems. It includes a Python-based frontend for user interaction and a backend that handles NLP processing, ML inference, confidence scoring, and response generation.

To ensure reliability, the system incorporates a confidence score mechanism. If the chatbot is not confident about a response, it provides a safe fallback message instead of incorrect information. Low-confidence queries are logged and can be used to improve the system through retraining.

Overall, this project demonstrates a practical application of AI in the education domain by reducing manual effort, improving accessibility to information, and offering a scalable, intelligent solution for college-related queries.