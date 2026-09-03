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