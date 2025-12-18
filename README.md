# 📄 Resume ATS Scorer

A machine learning–powered tool that analyzes resumes, compares them with a job description, and generates an ATS (Applicant Tracking System) score along with missing skills, strengths, and improvement suggestions.

---

## ✨ Features
- Extracts resume text (PDF) using OCR-free parsing  
- Matches resume content with job description  
- Calculates ATS score using **TF-IDF + Cosine Similarity**  
- Detects missing skills  
- Highlights strengths  
- Generates improvement suggestions  
- Clean HTML/CSS/JS frontend  
- FastAPI backend API  

---

## 🛠 Tech Stack

### 🎨 Frontend
- HTML  
- CSS  
- JavaScript (Fetch API)

### ⚙️ Backend
- Python  
- FastAPI  
- Uvicorn  

### 🧠 Machine Learning / NLP
- TF-IDF Vectorizer  
- Cosine Similarity  
- PyPDF2  
- spaCy (optional)  

### 🗄 Database
- SQLite (stores scoring logs)

---

## 📁 Project Structure
resume_ats_scorer/
│
├── backend/

│ ├── main.py

│ ├── ats_logic.py

│ ├── resume_parser.py

│ ├── database.py

│ └── skills.csv

│

├── frontend/

│ ├── index.html

│ ├── style.css

│ └── script.js

│

└── README.md

# 1️⃣ Clone the Repository
git clone https://github.com/<your-username>/resume_ats_scorer.git
cd resume_ats_scorer/backend

# 2️⃣ Create a Virtual Environment (optional)
python -m venv venv

# Activate Virtual Environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# 3️⃣ Install Dependencies
pip install fastapi uvicorn scikit-learn PyPDF2 python-multipart spacy

# Download spaCy model (optional but recommended)
python -m spacy download en_core_web_sm

# 4️⃣ Initialize Database
python database.py

# 5️⃣ Start Backend Server
uvicorn main:app --reload

# Backend now runs at:
# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs  (Swagger API Docs)

# 6️⃣ Run Frontend
# Simply open the file below in your browser:
# ../frontend/index.html
