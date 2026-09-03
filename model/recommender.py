import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Path to the jobs dataset (relative to project root)
DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "dataset", "jobs.csv")


def load_jobs():
    """Load the job postings dataset."""
    df = pd.read_csv(DATASET_PATH)
    return df


def recommend_jobs(resume_skills, top_n=5):
    """
    Given a list of skills extracted from a resume,
    return the top_n most relevant jobs from the dataset.
    """
    df = load_jobs()

    # Combine the resume skills into a single string (space-separated)
    resume_text = " ".join(resume_skills)

    # Combine each job's required_skills into a comparable text field
    job_texts = df["required_skills"].fillna("").tolist()

    # Add the resume text at the end so we can compare it against every job
    all_texts = job_texts + [resume_text]

    # Convert all text into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # The last vector is the resume; compare it to all job vectors
    resume_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(resume_vector, job_vectors).flatten()

    # Attach similarity scores to the dataframe
    df["match_score"] = (similarities * 100).round(2)

    # Sort by best match first
    results = df.sort_values(by="match_score", ascending=False).head(top_n)

    return results.to_dict(orient="records")