\# Resume ATS Scorer



\## Description

An Applicant Tracking System (ATS) Resume Scorer that analyzes a resume

against a job description using NLP and Machine Learning.



\## Features

\- ATS Score calculation

\- Missing skills detection

\- Strength summary

\- Resume improvement suggestions



\## Tech Stack

\- Frontend: HTML, CSS, JavaScript

\- Backend: Python, FastAPI

\- ML: TF-IDF, Cosine Similarity

\- Database: SQLite



\## Setup Instructions

1\. Clone repository

2\. Install dependencies

&nbsp;  pip install -r requirements.txt

3\. Run backend

&nbsp;  uvicorn main:app --reload

4\. Open frontend/index.html



\## API Endpoint

POST /analyze

\- resume (PDF file)

\- job\_description (text)



\## Database Schema

Table: results

\- id (INTEGER)

\- score (INTEGER)

\- missing\_skills (TEXT)

\- strengths (TEXT)



\## Future Enhancements

\- Deep learning embeddings (BERT)

\- Resume ranking

\- Authentication

\- Cloud deployment



