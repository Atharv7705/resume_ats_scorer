from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text, job_desc, skills_list):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    score = round(similarity * 100, 2)

    resume_words = set(resume_text.split())
    missing_skills = [skill for skill in skills_list if skill not in resume_words]

    strengths = list(set(skills_list) - set(missing_skills))

    suggestions = []
    if missing_skills:
        suggestions.append(f"Add the following missing skills to your resume: {', '.join(missing_skills)}")
    else:
        suggestions.append("Your resume covers all the key skills mentioned!")

    suggestions.extend([
        "Use more action verbs to describe your achievements",
        "Customize your resume for each job application",
        "Quantify your accomplishments with numbers where possible"
    ])

    return score, missing_skills, strengths, suggestions
