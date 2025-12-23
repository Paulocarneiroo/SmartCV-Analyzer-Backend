from app.services.text_extractor import extract_text
from app.services.nlp_service import extract_skills

ANALYSIS_STORE = {}


def analyze_skills(cv_text: str, job_skills: set):
    cv_skills = extract_skills(cv_text)

    strengths = []
    weaknesses = []

    for skill in cv_skills:
        strengths.append(f"Conhecimento em {skill}")

    missing_skills = job_skills - cv_skills
    for skill in missing_skills:
        weaknesses.append(f"Não menciona experiência com {skill}")

    return cv_skills, strengths, weaknesses


def calculate_score(cv_skills: set, job_skills: set) -> int:
    if not job_skills:
        return 0

    match = cv_skills & job_skills
    score = int((len(match) / len(job_skills)) * 100)
    return score


def process_cv(
    analysis_id: str,
    file_path: str,
    job_skills: set
):
    try:
        ANALYSIS_STORE[analysis_id] = {"status": "PROCESSING"}

        text = extract_text(file_path)

        cv_skills, strengths, weaknesses = analyze_skills(text, job_skills)

        score = calculate_score(cv_skills, job_skills)

        ANALYSIS_STORE[analysis_id] = {
            "status": "DONE",
            "result": {
                "strengths": strengths,
                "weaknesses": weaknesses,
                "compatibility_score": score
            }
        }

    except Exception as e:
        ANALYSIS_STORE[analysis_id] = {
            "status": "ERROR",
            "error": str(e)
        }
