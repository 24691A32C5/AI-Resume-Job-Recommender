import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from utils.resume_parser import parse_resume
from model.recommender import recommend_jobs

app = Flask(__name__)

# Folder where uploaded resumes will be temporarily stored
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

        if not skills:
            return render_template(
                "index.html",
                error="No recognizable skills were found in your resume. Try a different file."
            )

        recommendations = recommend_jobs(skills, top_n=5)

        return render_template(
            "results.html",
            skills=skills,
            recommendations=recommendations
        )

    except Exception as e:
        return render_template("index.html", error=f"Error processing resume: {str(e)}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)