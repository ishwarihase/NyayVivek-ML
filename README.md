NyayVivek-ML

AI-powered Legal Analysis Backend using Semantic Search, FAISS Retrieval, and Flask API.

Overview

NyayVivek is an AI-assisted legal intelligence system designed to analyze legal case descriptions and provide:

Similar Case Retrieval
IPC / Legal Section Prediction
Missing Evidence Detection
Judgment Pattern Analytics
Evidence-to-Law Mapping

The system uses:

Sentence Transformers for embeddings
FAISS for semantic similarity search
Flask for backend API integration
Features
1. Similar Case Retrieval

Retrieves semantically similar historical legal cases using vector embeddings and FAISS similarity search.

Output Includes:
Case title
Case type
Legal sections
Judgment outcome
2. IPC / Legal Section Prediction

Predicts likely IPC/legal sections based on similar retrieved cases.

Example:
{
  "section": "IPC 302",
  "confidence": 31.55
}
3. Missing Evidence Detection

Detects commonly occurring evidence missing from the current case description.

Example:
Eyewitness testimony
Medical evidence
Postmortem report
CCTV footage
4. Judgment Pattern Analytics

Analyzes outcomes from similar cases.

Example:
{
  "outcome": "Guilty",
  "percentage": 80.0
}
5. Evidence → Law Mapping

Maps commonly associated evidence to relevant legal sections.

Example:
{
  "evidence": "Eyewitness testimony",
  "related_laws": ["IPC Section 302"]
}
Tech Stack
Backend
Flask
Flask-CORS
ML / NLP
SentenceTransformers
FAISS
scikit-learn
pandas
numpy
Dataset
Excel-based legal dataset
Project Structure
NyayVivek-ML/
│
├── app.py
├── ml_engine.py
├── test_ml.py
├── new.ipynb
├── requirements.txt
├── README.md
├── temp1.xlsx
├── faiss_index.pkl
├── legal_dataset.pkl
├── .gitignore
Installation
1. Clone Repository
git clone https://github.com/iisha-git/NyayVivek-ML.git
2. Move Into Project Folder
cd NyayVivek-ML
3. Create Virtual Environment
Windows
python -m venv venv
4. Activate Virtual Environment
PowerShell
venv\Scripts\activate

If execution policy blocks activation:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Then activate again.

5. Install Dependencies
pip install -r requirements.txt
Running the Backend

Start Flask server:

python app.py

Backend runs at:

http://127.0.0.1:5000
API Endpoint
POST /analyze

Analyzes a legal case description.

Request Body
{
  "query": "The accused was involved in a murder case with eyewitness evidence."
}
Response Example
{
  "similar_cases": [
    {
      "case_title": "Albert Sinha vs State of Assam",
      "case_type": "Criminal",
      "legal_sections": "IPC Section 302",
      "judgment_outcome": "Guilty"
    }
  ],

  "predicted_sections": [
    {
      "section": "IPC 302",
      "confidence": 31.55
    }
  ],

  "missing_evidence": [
    "medical evidence",
    "postmortem report"
  ],

  "judgment_analytics": [
    {
      "outcome": "Guilty",
      "percentage": 80.0
    }
  ],

  "evidence_law_mapping": [
    {
      "evidence": "Eyewitness testimony",
      "related_laws": [
        "IPC Section 302"
      ]
    }
  ]
}
Frontend Integration Example
fetch("http://127.0.0.1:5000/analyze", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    query: "The accused was involved in a murder case..."
  })
})
.then(res => res.json())
.then(data => console.log(data))
ML Pipeline Flow
Frontend/User Query
        ↓
Flask API (app.py)
        ↓
ML Engine (ml_engine.py)
        ↓
SentenceTransformer Embeddings
        ↓
FAISS Semantic Retrieval
        ↓
Legal Analysis Pipeline
        ├── Similar Cases
        ├── IPC Prediction
        ├── Missing Evidence
        ├── Judgment Analytics
        └── Evidence-Law Mapping
        ↓
Structured JSON Response
Dataset

Dataset contains:

Case titles
Legal sections
Judgment outcomes
Evidence types
Judge observations
Legal keywords

Stored as:

temp1.xlsx
Important Files
app.py

Main Flask backend API.

ml_engine.py

Contains all ML logic and legal analysis functions.

faiss_index.pkl

Serialized FAISS similarity index.

legal_dataset.pkl

Serialized processed dataset.

new.ipynb

Research and experimentation notebook.

Current Capabilities
Semantic legal search
AI-assisted legal recommendations
Explainable legal analytics
Backend API integration
Frontend-ready JSON responses
Future Improvements
PDF upload support
OCR for scanned legal documents
Deployment on Render/Railway/AWS
FastAPI migration
Authentication system
Chat-style legal assistant
Real-time analytics dashboard
Authors

NyayVivek Team

GitHub:
NyayVivek-ML Repository