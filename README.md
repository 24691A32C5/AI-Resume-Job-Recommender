AI-Based Resume Screening and Job Recommendation System
An AI-powered career guidance platform that analyzes a student's resume, identifies skill gaps, recommends suitable jobs and internships across multiple engineering branches, generates a personalized learning roadmap, suggests projects, and prepares the student for interviews.
Live demo: https://ai-resume-job-recommender-6q11.onrender.com
Note: the app is hosted on a free tier and may take 30-50 seconds to wake up on first load after a period of inactivity.
Features
Resume Parsing — extracts text and skills from uploaded PDF/DOCX resumes
AI-Based Job Matching — uses TF-IDF vectorization and cosine similarity to match resume skills against a dataset of 60+ job roles
Multi-Branch Support — covers Computer Science, ECE, Mechanical, Civil, EEE, Chemical, Biotechnology, and more
Skill Gap Analysis — shows matched vs. missing skills for each recommended job
ATS Compatibility Score — approximate, transparent scoring based on resume structure, keyword relevance, and formatting
Resume Improvement Suggestions — rule-based feedback on missing sections, achievements, and keyword coverage
Job Readiness Score — quantifies how well-matched a candidate is to each role
Readiness Improvement Simulator — projects how readiness would improve by learning specific missing skills
Personalized Learning Roadmap — step-by-step learning paths for each missing skill
Project Recommendations — suggested projects to build for each target role
Internship Recommendations — separately highlights internship-friendly roles
Interview Preparation — technical and HR questions tailored to each job role
Action Plan — a personalized summary of next steps for the candidate
Tech Stack
Layer
Technology
Backend
Python, Flask
Machine Learning
scikit-learn (TF-IDF, cosine similarity), pandas, numpy
Resume Parsing
PyPDF2, python-docx
Frontend
HTML, CSS, JavaScript (Jinja2 templating)
Deployment
Render (Gunicorn WSGI server)
Version Control
Git, GitHub
Project Structure
AI-Resume-Job-Recommender/
├── app.py                     # Flask application and routes
├── requirements.txt           # Python dependencies
├── Procfile                   # Render deployment config
├── dataset/
│   └── jobs.csv                # Job postings dataset (60+ roles)
├── model/
│   ├── recommender.py          # TF-IDF matching, readiness scoring, simulator
│   └── career_data.py          # Project suggestions, learning roadmaps, interview Q&A
├── utils/
│   └── resume_parser.py        # Resume text extraction, skill detection, ATS scoring
├── templates/
│   ├── index.html              # Upload page
│   └── results.html            # Career analysis results page
├── static/
│   ├── css/style.css           # Styling
│   └── js/script.js
└── database/                   # Reserved for future persistence layer
How It Works
Upload — the user uploads a resume in PDF or DOCX format
Parse — resume_parser.py extracts raw text and detects known technical skills using keyword matching
Match — recommender.py vectorizes the resume's skills and each job's required skills using TF-IDF, then computes cosine similarity to rank the top matching jobs
Analyze — for each recommended job, the system computes a skill gap (matched vs. missing skills), a readiness score, and a readiness improvement simulation
Enrich — career_data.py attaches relevant project ideas, a learning roadmap, and interview questions to each job
Present — results.html renders the full career analysis: readiness scores, ATS score breakdown, resume suggestions, job/internship recommendations, and a personalized action plan
Running Locally
# 1. Clone the repository
git clone https://github.com/24691A32C5/AI-Resume-Job-Recommender.git
cd AI-Resume-Job-Recommender

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open in browser
http://127.0.0.1:5000
Deployment
The app is deployed on Render using Gunicorn as the production WSGI server. Any push to the main branch on GitHub automatically triggers a redeploy.
Build command: pip install -r requirements.txt
Start command: gunicorn app:app
Limitations & Honest Notes
The ATS Compatibility Score is an approximation based on transparent, rule-based checks (section presence, keyword density, formatting, achievements) — it does not replicate any specific commercial ATS engine.
Interview questions are drawn from a static, curated question bank per job category, not dynamically generated from the candidate's specific resume content.
Skill detection relies on keyword matching against a predefined skill list; skills phrased very differently from the expected keywords may not be detected.
Future Enhancements
Resume-vs-specific-Job-Description matching
Location, salary, and experience-level filters
Collapsible/expandable job cards for a cleaner mobile UI
AI-evaluated mock interview mode
Persistent database layer to store analysis history
Native mobile app (Android APK)
Author
Project developed as a Full Stack + Data Science college project.