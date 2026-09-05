import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from utils.resume_parser import parse_resume, generate_resume_suggestions, calculate_ats_score
from model.recommender import recommend_jobs, simulate_readiness_improvement, get_match_highlight, tag_job_level
from model.career_data import get_project_suggestions, get_learning_roadmap, get_interview_questions

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf", "docx"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "resume" not in request.files:
        return render_template("index.html", error="No file uploaded.")

    file = request.files["resume"]

    if file.filename == "":
        return render_template("index.html", error="No file selected.")

    if not allowed_file(file.filename):
        return render_template("index.html", error="Only PDF and DOCX files are supported.")

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    try:
        parsed = parse_resume(file_path)
        skills = parsed["skills"]
        raw_text = parsed["raw_text"]

        if not skills:
            return render_template(
                "index.html",
                error="No recognizable skills were found in your resume. Try a different file."
            )

        recommendations = recommend_jobs(skills, top_n=5)

        for job in recommendations:
            job["project_ideas"] = get_project_suggestions(job["job_title"])
            job["roadmap"] = get_learning_roadmap(job["missing_skills"])
            job["interview_questions"] = get_interview_questions(job["job_title"])
            job["simulation"] = simulate_readiness_improvement(skills, job)
            job["match_highlight"] = get_match_highlight(job)
            job["job_level"] = tag_job_level(job["job_title"])

        overall_readiness = recommendations[0]["readiness_score"] if recommendations else 0
        resume_suggestions = generate_resume_suggestions(raw_text, skills)
        ats_result = calculate_ats_score(raw_text, skills)

        top_job = recommendations[0] if recommendations else None
        internships = [job for job in recommendations if job["job_level"] == "Internship-friendly"]

        # Build a simple action plan from the top job's missing skills + projects
        action_plan = []
        if top_job:
            for skill in top_job["missing_skills"][:2]:
                action_plan.append(f"Learn {skill}")
            if top_job["project_ideas"]:
                action_plan.append(f"Build a project: {top_job['project_ideas'][0]}")
            action_plan.append("Update your resume with new skills and projects")
            action_plan.append(f"Practice interview questions for {top_job['job_title']}")
            if internships:
                action_plan.append(f"Apply for internships like {internships[0]['job_title']}")

        return render_template(
            "results.html",
            skills=skills,
            recommendations=recommendations,
            overall_readiness=overall_readiness,
            top_job=top_job["job_title"] if top_job else None,
            resume_suggestions=resume_suggestions,
            ats_result=ats_result,
            internships=internships,
            action_plan=action_plan
        )

    except Exception as e:
        return render_template("index.html", error=f"Error processing resume: {str(e)}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)