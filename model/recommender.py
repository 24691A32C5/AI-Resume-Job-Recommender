import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "dataset", "jobs.csv")


def load_jobs():
    df = pd.read_csv(DATASET_PATH)
    return df


def parse_skill_list(skill_string):
    """Turn 'python, sql, django' into ['python', 'sql', 'django']."""
    return [s.strip().lower() for s in skill_string.split(",") if s.strip()]


def recommend_jobs(resume_skills, top_n=5):
    df = load_jobs()
    resume_skills_lower = [s.strip().lower() for s in resume_skills]

    resume_text = " ".join(resume_skills_lower)
    job_texts = df["required_skills"].fillna("").tolist()
    all_texts = job_texts + [resume_text]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    resume_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(resume_vector, job_vectors).flatten()
    df["match_score"] = (similarities * 100).round(2)

    results_df = df.sort_values(by="match_score", ascending=False).head(top_n)
    results = results_df.to_dict(orient="records")

    # Enrich each job with skill gap analysis
    for job in results:
        required = parse_skill_list(job["required_skills"])
        matched = [skill for skill in required if skill in resume_skills_lower]
        missing = [skill for skill in required if skill not in resume_skills_lower]

        readiness = round((len(matched) / len(required)) * 100) if required else 0

        job["matched_skills"] = matched
        job["missing_skills"] = missing
        job["readiness_score"] = readiness

    return results