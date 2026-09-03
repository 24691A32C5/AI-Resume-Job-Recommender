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
# Static interview question banks per job title
INTERVIEW_QUESTIONS = {
    "VLSI Design Engineer": {
        "technical": [
            "Explain the difference between Verilog and VHDL.",
            "What is the difference between blocking and non-blocking assignments in Verilog?",
            "Explain setup time and hold time in digital circuits.",
            "What is an FPGA and how does it differ from an ASIC?",
        ],
        "hr": [
            "Tell me about a hardware project you're proud of.",
            "Why are you interested in VLSI design?",
            "How do you stay updated with new EDA tools and techniques?",
        ],
    },
    "Embedded Systems Engineer": {
        "technical": [
            "What is the difference between a microcontroller and a microprocessor?",
            "Explain the concept of interrupts in embedded systems.",
            "What is RTOS and why is it used?",
            "How do you debug embedded C code without a screen output?",
        ],
        "hr": [
            "Describe a hardware-software integration challenge you faced.",
            "Why do you want to work in embedded systems?",
            "How do you approach debugging a device that behaves unpredictably?",
        ],
    },
    "Electronics Design Engineer": {
        "technical": [
            "What is the difference between analog and digital circuits?",
            "Explain the purpose of decoupling capacitors in PCB design.",
            "What are common causes of noise in a circuit and how do you reduce it?",
        ],
        "hr": [
            "Tell me about a circuit you designed from scratch.",
            "How do you handle tight deadlines in hardware prototyping?",
        ],
    },
    "Communication Systems Engineer": {
        "technical": [
            "Explain the difference between analog and digital modulation.",
            "What is the Nyquist theorem and why does it matter?",
            "Explain the basics of OFDM and where it's used.",
        ],
        "hr": [
            "Why are you interested in communication systems?",
            "Describe a signal processing project you've worked on.",
        ],
    },
    "IoT Engineer": {
        "technical": [
            "What are common IoT communication protocols (MQTT, CoAP, etc.)?",
            "How do you ensure security in an IoT device?",
            "Explain the role of edge computing in IoT systems.",
        ],
        "hr": [
            "Describe an IoT project you've built.",
            "How do you handle unreliable network conditions in your IoT projects?",
        ],
    },
    "Data Scientist": {
        "technical": [
            "Explain the bias-variance tradeoff.",
            "What is overfitting and how do you prevent it?",
            "Explain the difference between supervised and unsupervised learning.",
        ],
        "hr": [
            "Walk me through a data science project end-to-end.",
            "How do you communicate technical results to non-technical stakeholders?",
        ],
    },
    "Machine Learning Engineer": {
        "technical": [
            "Explain how a neural network learns.",
            "What is the difference between CNN and RNN?",
            "How do you handle imbalanced datasets?",
        ],
        "hr": [
            "Tell me about the most challenging ML project you've worked on.",
            "How do you keep up with new developments in ML?",
        ],
    },
    "Backend Developer": {
        "technical": [
            "Explain RESTful API design principles.",
            "What is the difference between SQL and NoSQL databases?",
            "How do you handle authentication and authorization in a web app?",
        ],
        "hr": [
            "Describe a backend system you built or contributed to.",
            "How do you approach debugging a production issue?",
        ],
    },
    "Python Developer": {
        "technical": [
            "What are Python decorators and how do you use them?",
            "Explain the difference between a list and a tuple.",
            "How does Python's garbage collection work?",
        ],
        "hr": [
            "Tell me about a Python project you're proud of.",
            "How do you approach writing clean, maintainable code?",
        ],
    },
    "Full Stack Developer": {
        "technical": [
            "Explain how the frontend and backend communicate in a web app.",
            "What is CORS and why does it matter?",
            "How do you manage state in a frontend application?",
        ],
        "hr": [
            "Walk me through a full stack project you've built.",
            "How do you prioritize frontend vs backend work under a deadline?",
        ],
    },
    "Mechanical Design Engineer": {
        "technical": [
            "Explain the difference between stress and strain.",
            "What is GD&T and why is it important in design?",
            "How do you approach tolerance stack-up analysis?",
        ],
        "hr": [
            "Describe a mechanical design project you've completed.",
            "How do you balance design creativity with manufacturability constraints?",
        ],
    },
    "Civil Site Engineer": {
        "technical": [
            "What are the key considerations in site layout planning?",
            "Explain the difference between dead load and live load.",
            "How do you ensure quality control on a construction site?",
        ],
        "hr": [
            "Describe a construction project you were involved in.",
            "How do you handle coordination issues between contractors?",
        ],
    },
    "Structural Engineer": {
        "technical": [
            "Explain the difference between a beam and a column.",
            "What factors affect the load-bearing capacity of a structure?",
            "How do you approach seismic design considerations?",
        ],
        "hr": [
            "Describe a structural analysis project you've worked on.",
            "How do you ensure your designs meet safety codes?",
        ],
    },
    "Robotics Engineer": {
        "technical": [
            "Explain the difference between forward and inverse kinematics.",
            "What is ROS and why is it widely used in robotics?",
            "How do you approach sensor fusion in a robotic system?",
        ],
        "hr": [
            "Describe a robotics project you've built.",
            "How do you debug unexpected robot behavior?",
        ],
    },
    "Power Systems Engineer": {
        "technical": [
            "Explain the difference between active and reactive power.",
            "What is load flow analysis and why is it important?",
            "How do protection systems work in power grids?",
        ],
        "hr": [
            "Describe a power systems project you've analyzed or designed.",
            "How do you approach troubleshooting a fault in a power system?",
        ],
    },
}

DEFAULT_INTERVIEW_QUESTIONS = {
    "technical": [
        "Explain a technical project relevant to this role in detail.",
        "What tools or technologies are essential for this role, and why?",
        "How would you approach solving a problem you've never encountered before in this field?",
    ],
    "hr": [
        "Tell me about yourself.",
        "Why are you interested in this role?",
        "Describe a challenge you faced in a project and how you overcame it.",
    ],
}


def get_interview_questions(job_title):
    return INTERVIEW_QUESTIONS.get(job_title, DEFAULT_INTERVIEW_QUESTIONS)