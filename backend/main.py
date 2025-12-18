from fastapi import FastAPI, UploadFile, Form
from resume_parser import extract_text_from_pdf
from ats_logic import calculate_ats_score
from database import save_result

app = FastAPI()

skills = ["python", "machine learning", "sql", "deep learning", "fastapi"]

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile,
    job_description: str = Form(...)
):
    resume_text = extract_text_from_pdf(resume.file)
    
    score, missing, strengths, suggestions = calculate_ats_score(
        resume_text, job_description.lower(), skills
    )

    # Save result to database
    save_result(int(score), str(missing), str(strengths))

    return {
        "ATS Score": f"{score}/100",
        "Missing Skills": missing,
        "Strengths": strengths,
        "Suggestions": suggestions
    }
@app.get("/")
def home():
    return {"message": "Resume ATS Scorer API is running"}
