# Maps job titles to suggested project ideas students can build
# to strengthen their profile for that role.
PROJECT_SUGGESTIONS = {
    "VLSI Design Engineer": [
        "FPGA-based Digital Clock",
        "4-bit ALU Design in Verilog",
        "UART Communication System",
        "Traffic Light Controller using VHDL",
    ],
    "Embedded Systems Engineer": [
        "Smart Home Automation System",
        "IoT-Based Health Monitoring Device",
        "Line Following Robot",
        "Bluetooth Controlled Robot",
    ],
    "Electronics Design Engineer": [
        "PCB Design for a Power Supply Circuit",
        "Digital Multimeter using Microcontroller",
        "LED Matrix Display Driver",
    ],
    "Communication Systems Engineer": [
        "Software Defined Radio (SDR) Project",
        "Wireless Sensor Network Simulation",
        "Digital Modulation Scheme Simulator (MATLAB)",
    ],
    "IoT Engineer": [
        "Smart Agriculture Monitoring System",
        "IoT-Based Home Automation System",
        "Air Quality Monitoring using Sensors",
    ],
    "Data Scientist": [
        "Customer Churn Prediction Model",
        "Movie Recommendation System",
        "Sales Forecasting Dashboard",
    ],
    "Machine Learning Engineer": [
        "Image Classification with CNN",
        "Chatbot using NLP",
        "Fraud Detection System",
    ],
    "Backend Developer": [
        "REST API for a To-Do App",
        "E-Commerce Backend with Flask/Django",
        "User Authentication System",
    ],
    "Python Developer": [
        "Web Scraper for Data Collection",
        "Automated Report Generator",
        "Personal Finance Tracker",
    ],
    "Full Stack Developer": [
        "Blog Platform with Login System",
        "Task Management App",
        "Online Store with Cart and Checkout",
    ],
    "Mechanical Design Engineer": [
        "3D Model of a Mechanical Assembly (SolidWorks)",
        "Gearbox Design Project",
        "Stress Analysis of a Bracket using CAD",
    ],
    "Civil Site Engineer": [
        "Structural Design of a Small Building",
        "Site Layout Planning Project",
        "Cost Estimation for a Construction Project",
    ],
    "Structural Engineer": [
        "Analysis of a Multi-Story Building (STAAD Pro)",
        "Bridge Design Project",
        "Earthquake-Resistant Structure Design",
    ],
    "Robotics Engineer": [
        "Obstacle Avoiding Robot",
        "Robotic Arm using Arduino",
        "Autonomous Navigation using ROS",
    ],
    "Power Systems Engineer": [
        "Load Flow Analysis Project",
        "Fault Analysis in Power Systems (MATLAB)",
        "Solar Power System Design",
    ],
}

# Generic fallback project ideas for jobs not explicitly listed above
DEFAULT_PROJECTS = [
    "A mini project applying the core required skills for this role",
    "A portfolio piece demonstrating hands-on experience with the top 2-3 required tools",
    "An open-source contribution related to this field",
]


# Maps individual skills to a short recommended learning path
LEARNING_ROADMAP = {
    "verilog": ["Digital Logic Basics", "Verilog Syntax & Modules", "Testbenches & Simulation", "Small FPGA Project"],
    "vhdl": ["Digital Logic Basics", "VHDL Syntax", "State Machines in VHDL", "FPGA Implementation"],
    "embedded c": ["C Programming Basics", "Microcontroller Architecture", "Embedded C Programming", "Hands-on with Arduino/STM32"],
    "microcontrollers": ["Basic Electronics", "Microcontroller Architecture (8051/ARM)", "Interfacing Sensors", "Mini Embedded Project"],
    "pcb design": ["Basic Circuit Design", "PCB Design Software (Altium/Eagle)", "Layout & Routing Rules", "Build a Simple PCB"],
    "rf design": ["RF Fundamentals", "Antenna Theory", "RF Circuit Design Tools", "Simple RF Project"],
    "wireless communication": ["Signals & Systems Basics", "Modulation Techniques", "Wireless Standards (WiFi/Bluetooth)", "Simulation Project"],
    "machine learning": ["Python & Statistics Basics", "Supervised Learning Algorithms", "Scikit-learn Practice", "End-to-End ML Project"],
    "deep learning": ["Neural Network Basics", "TensorFlow/PyTorch Fundamentals", "CNNs & RNNs", "Image/Text Project"],
    "django": ["Python Basics", "Django Fundamentals", "Building REST APIs", "Full Project with Database"],
    "flask": ["Python Basics", "Flask Fundamentals", "Templates & Routing", "Small Web App Project"],
    "react": ["JavaScript Basics", "React Fundamentals", "State Management (Hooks)", "Build a Small App"],
    "sql": ["Database Basics", "SQL Queries", "Joins & Aggregations", "Design a Small Database"],
    "autocad": ["CAD Basics", "2D Drafting", "3D Modeling", "Complete a Design Project"],
    "solidworks": ["CAD Basics", "Part Modeling", "Assembly Design", "Simulation & Stress Analysis"],
    "staad pro": ["Structural Analysis Basics", "STAAD Pro Interface", "Modeling Structures", "Analyze a Small Building"],
    "plc programming": ["Basic Electrical Concepts", "PLC Fundamentals", "Ladder Logic Programming", "Automate a Simple Process"],
}

DEFAULT_ROADMAP = ["Learn the fundamentals", "Practice with small exercises", "Build a project using this skill", "Add it to your portfolio"]


def get_project_suggestions(job_title):
    return PROJECT_SUGGESTIONS.get(job_title, DEFAULT_PROJECTS)


def get_learning_roadmap(missing_skills):
    """Return a roadmap dict for each missing skill (up to 3 skills to keep it focused)."""
    roadmap = {}
    for skill in missing_skills[:3]:
        roadmap[skill] = LEARNING_ROADMAP.get(skill, DEFAULT_ROADMAP)
    return roadmap