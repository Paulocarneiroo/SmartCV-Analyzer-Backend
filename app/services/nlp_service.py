import spacy
from typing import List, Set

nlp = spacy.load("pt_core_news_sm")

# Skills técnicas mais comuns (expandível)
TECH_SKILLS = {
    "python", "java", "spring", "spring boot",
    "fastapi", "django",
    "react", "react native", "flutter",
    "docker", "kubernetes",
    "postgresql", "mysql", "mongodb",
    "git", "github",
    "aws", "azure", "gcp",
    "rest", "api", "microserviços"
}

def normalize(text: str) -> str:
    return text.lower()


def extract_skills(text: str) -> Set[str]:
    text = normalize(text)
    doc = nlp(text)

    found_skills = set()

    for skill in TECH_SKILLS:
        if skill in text:
            found_skills.add(skill)

    return found_skills
