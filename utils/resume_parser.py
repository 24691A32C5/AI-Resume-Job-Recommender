import re
import PyPDF2
import docx

# A master list of skills we can detect in resumes.
# This should roughly match the skills mentioned in dataset/jobs.csv
SKILL_KEYWORDS = [
    "python", "java", "javascript", "html", "css", "react", "redux",
    "node.js", "express", "mongodb", "sql", "mysql", "postgresql",
    "django", "flask", "rest api", "api development", "spring boot",
    "hibernate", "kotlin", "android studio", "xml", "sqlite",
    "swift", "xcode", "ios", "uikit", "core data",
    "docker", "kubernetes", "aws", "azure", "terraform", "linux",
    "networking", "ci/cd", "network security", "penetration testing",
    "siem", "firewalls", "figma", "adobe xd", "wireframing",
    "prototyping", "user research", "product strategy", "agile",
    "jira", "communication", "market research", "requirements gathering",
    "power bi", "excel", "selenium", "manual testing",
    "automation testing", "database design", "backup recovery",
    "cisco", "tcp/ip", "routing switching", "data structures",
    "algorithms", "git", "php", "troubleshooting", "customer service",
    "windows", "sap", "erp", "business process", "seo",
    "google analytics", "content strategy", "hr analytics",
    "solidity", "ethereum", "blockchain", "smart contracts",
    "c#", "unity", "game design", "3d modeling", "c++",
    "machine learning", "deep learning", "tensorflow", "pytorch",
    "pandas", "numpy", "scikit-learn", "data visualization",
    "spark", "etl", "airflow", "research"
    "verilog", "vhdl", "vlsi design", "cadence", "digital design",
    "embedded c", "microcontrollers", "rtos", "pcb design", "arm",
    "circuit design", "altium", "analog electronics",
    "signal processing", "matlab", "wireless communication", "rf design",
    "iot protocols", "sensors",
    "power systems analysis", "autocad electrical", "plc programming",
    "panel design", "wiring diagrams", "scada", "control systems",
    "instrumentation", "automation", "solar design", "pvsyst",
    "calibration", "process control",
    "autocad", "solidworks", "gd&t", "mechanical design", "manufacturing",
    "lean manufacturing", "six sigma", "production planning",
    "quality control", "hvac design", "thermodynamics", "energy analysis",
    "catia", "vehicle dynamics", "cad", "preventive maintenance", "plc",
    "troubleshooting", "mechanical systems", "safety standards",
    "staad pro", "site supervision", "structural design",
    "project management", "etabs", "structural analysis",
    "concrete design", "primavera", "budgeting", "traffic analysis",
    "autocad civil 3d", "highway design", "gis", "project planning",
    "environmental impact assessment", "water treatment",
    "regulatory compliance", "sustainability",
    "process design", "chemical engineering", "aspen plus",
    "process simulation", "analytical chemistry", "lab testing",
    "gc-ms", "documentation", "reservoir engineering",
    "drilling operations", "petroleum engineering",
    "molecular biology", "pcr", "lab techniques",
    "food science", "haccp", "product development",
    "textile engineering", "fabric design",
    "mine planning", "surveying", "geotechnical analysis",
    "aerodynamics", "robotics", "ros", "marine engineering"
]


def extract_text_from_pdf(file_path):
    """Extract raw text from a PDF file."""
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_text_from_docx(file_path):
    """Extract raw text from a DOCX file."""
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text


def extract_text(file_path):
    """Detect file type and extract text accordingly."""
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")


def extract_skills(text):
    """Find which known skills appear in the resume text."""
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        # Use word-boundary-safe matching so 'java' doesn't match inside 'javascript'
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return list(set(found_skills))


def parse_resume(file_path):
    """Main function: extract text and skills from a resume file."""
    text = extract_text(file_path)
    skills = extract_skills(text)
    return {
        "raw_text": text,
        "skills": skills
    }
def check_resume_sections(text):
    """Check which standard resume sections are present."""
    text_lower = text.lower()
    sections = {
        "education": ["education", "b.tech", "degree", "university", "college"],
        "projects": ["project", "projects"],
        "skills": ["skills", "technical skills"],
        "certifications": ["certification", "certificate", "coursera", "udemy"],
        "experience": ["experience", "internship", "work history"],
        "contact_info": ["@", "phone", "email", "contact"],
    }

    found = {}
    for section, keywords in sections.items():
        found[section] = any(kw in text_lower for kw in keywords)

    return found


def check_measurable_achievements(text):
    """Rough check for numbers/metrics in the resume (signals measurable impact)."""
    import re
    number_pattern = r'\b\d+%|\b\d+\+|\bimproved\b|\breduced\b|\bincreased\b'
    matches = re.findall(number_pattern, text.lower())
    return len(matches) > 0


def generate_resume_suggestions(text, skills):
    """Generate a list of improvement suggestions based on simple rule-based checks."""
    suggestions = []
    sections = check_resume_sections(text)

    if sections["education"]:
        suggestions.append({"type": "good", "message": "Education section detected."})
    else:
        suggestions.append({"type": "warning", "message": "No clear education section found — consider adding one."})

    if sections["projects"]:
        suggestions.append({"type": "good", "message": "Projects section detected."})
    else:
        suggestions.append({"type": "warning", "message": "No projects section found — adding relevant projects strengthens your resume significantly."})

    if sections["certifications"]:
        suggestions.append({"type": "good", "message": "Certifications detected."})
    else:
        suggestions.append({"type": "warning", "message": "No certifications found — relevant certifications can boost your profile."})

    if sections["experience"]:
        suggestions.append({"type": "good", "message": "Experience/internship section detected."})
    else:
        suggestions.append({"type": "warning", "message": "No experience or internship mentioned — consider adding any relevant work, even short-term."})

    if not check_measurable_achievements(text):
        suggestions.append({"type": "warning", "message": "Add measurable achievements to your projects (e.g., 'improved accuracy by 15%', 'reduced load time by 2x')."})
    else:
        suggestions.append({"type": "good", "message": "Measurable achievements detected in your resume."})

    if len(skills) < 5:
        suggestions.append({"type": "warning", "message": "Few technical skills detected — consider listing more relevant tools and technologies."})
    else:
        suggestions.append({"type": "good", "message": f"{len(skills)} relevant skills detected — good keyword coverage."})

    return suggestions


def calculate_ats_score(text, skills):
    """
    Approximate ATS compatibility score based on simple, transparent rules.
    This is NOT identical to real commercial ATS systems, but reflects
    common factors they check: sections present, keyword density, resume length.
    """
    score = 0
    max_score = 100
    sections = check_resume_sections(text)

    # Section presence (50 points total)
    section_weight = 50 / len(sections)
    for present in sections.values():
        if present:
            score += section_weight

    # Skill/keyword count (30 points, capped)
    skill_score = min(len(skills) * 3, 30)
    score += skill_score

    # Measurable achievements (10 points)
    if check_measurable_achievements(text):
        score += 10

    # Reasonable length check (10 points) - not too short, not excessively long
    word_count = len(text.split())
    if 150 <= word_count <= 1000:
        score += 10
    elif word_count > 0:
        score += 5

    return round(min(score, max_score))