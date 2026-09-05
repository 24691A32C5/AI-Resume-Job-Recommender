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
def simulate_readiness_improvement(resume_skills, job):
    """
    Simulate readiness improvement with diminishing returns and a realistic cap.
    Each learned skill contributes less than a pure linear split would suggest,
    and we add optional 'soft' boosts (project, interview prep) capped below 100%.
    """
    resume_skills_lower = [s.strip().lower() for s in resume_skills]
    required = parse_skill_list(job["required_skills"])
    missing = job["missing_skills"]

    simulation = []
    current_known = list(resume_skills_lower)
    base_readiness = job["readiness_score"]

    for skill in missing:
        current_known.append(skill)
        matched_count = len([s for s in required if s in current_known])
        raw_readiness = (matched_count / len(required)) * 100 if required else 0
        # Apply a slight damping so it doesn't feel like each skill = exact equal share
        damped = base_readiness + (raw_readiness - base_readiness) * 0.85
        simulation.append({
            "skill_added": skill,
            "readiness_after": round(min(damped, 90))
        })

    # Soft, optional boosts beyond just learning the listed skills
    last_score = simulation[-1]["readiness_after"] if simulation else base_readiness
    if last_score < 95:
        project_boost = round(min(last_score + 6, 94))
        simulation.append({"skill_added": "a relevant project", "readiness_after": project_boost})

        interview_boost = round(min(project_boost + 4, 96))
        simulation.append({"skill_added": "interview preparation", "readiness_after": interview_boost})

    return simulation


def get_match_highlight(job):
    """Return a short human-readable summary of the strongest matching skill, if any."""
    matched = job.get("matched_skills", [])
    if not matched:
        return None
    # Just take the first matched skill as the highlight (could be made smarter later)
    return matched[0]


def tag_job_level(job_title):
    """
    Very simple heuristic to mark some roles as Internship-friendly.
    In a real system this would come from actual job posting data.
    """
    internship_friendly = [
        "Embedded Systems Engineer", "Electronics Design Engineer", "IoT Engineer",
        "Python Developer", "Frontend Developer", "Data Analyst", "Mechanical Design Engineer",
        "Civil Site Engineer", "VLSI Design Engineer",
    ]
    return "Internship-friendly" if job_title in internship_friendly else "Full-time"