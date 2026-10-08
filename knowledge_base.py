import re

KNOWLEDGE_DATA = [
    # -------------------------------------------------------------
    # SPECIFIC MATCHES FIRST (REST API, C++, MERN, MEAN, etc.)
    # -------------------------------------------------------------

    # REST API (before generic API)
    {
        "patterns": [
            "what is rest api",
            "what is rest",
            "explain rest api",
            "tell me about rest api",
            "rest api",
            "restful api"
        ],
        "keywords": ["rest api", "restful api"],
        "response": "A REST API (Representational State Transfer API) is an architectural style for APIs that uses standard HTTP requests (GET, POST, PUT, DELETE) to access and manipulate data."
    },

    # Web Dev - MERN Stack
    {
        "patterns": [
            "what is mern",
            "what is mern stack",
            "what is meant by mern stack",
            "explain mern stack",
            "explain mern",
            "tell me about mern",
            "what technologies are used in mern",
            "mern stack meaning",
            "mern stack",
            "mern"
        ],
        "keywords": ["mern stack", "mern"],
        "response": "MERN is a full-stack web development technology stack made up of MongoDB, Express.js, React, and Node.js. MongoDB is used for the database, Express.js and Node.js are used for the backend, and React is used for building the frontend."
    },

    # Web Dev - MEAN Stack
    {
        "patterns": [
            "what is mean stack",
            "what is mean",
            "explain mean stack",
            "tell me about mean stack",
            "mean stack meaning",
            "mean stack"
        ],
        "keywords": ["mean stack"],
        "response": "MEAN is a full-stack web technology stack consisting of MongoDB, Express.js, Angular, and Node.js used for building web applications."
    },

    # Programming - C++ (before generic C)
    {
        "patterns": [
            "what is c++",
            "what is cpp",
            "explain c++",
            "explain cpp",
            "tell me about c++",
            "c++ programming",
            "c plus plus",
            "cpp"
        ],
        "keywords": ["c++", "cpp", "c plus plus"],
        "response": "C++ is an extension of the C programming language that supports object-oriented programming, commonly used for high-performance applications, games, and systems software."
    },

    # Programming - TypeScript (before JS/Java)
    {
        "patterns": [
            "what is typescript",
            "what is ts",
            "explain typescript",
            "explain ts",
            "tell me about typescript",
            "typescript meaning",
            "typescript"
        ],
        "keywords": ["typescript"],
        "response": "TypeScript is a strongly typed programming language built on JavaScript that adds static typing, helping developers catch errors early in large applications."
    },

    # Programming - JavaScript (before Java)
    {
        "patterns": [
            "what is javascript",
            "what is js",
            "explain javascript",
            "explain js",
            "tell me about javascript",
            "javascript meaning",
            "js meaning",
            "javascript"
        ],
        "keywords": ["javascript"],
        "response": "JavaScript is a lightweight, dynamic programming language primarily used to build interactive and dynamic content on web pages."
    },

    # Cybersecurity (before single letter C)
    {
        "patterns": [
            "what is cybersecurity",
            "explain cybersecurity",
            "tell me about cybersecurity",
            "cyber security",
            "cybersecurity"
        ],
        "keywords": ["cybersecurity", "cyber security"],
        "response": "Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks, unauthorized access, or damage."
    },

    # -------------------------------------------------------------
    # GENERAL TECHNICAL & DOMAIN MATCHES
    # -------------------------------------------------------------

    # AI
    {
        "patterns": [
            "what is ai",
            "what is artificial intelligence",
            "explain ai",
            "tell me about ai",
            "ai meaning",
            "define ai",
            "artificial intelligence"
        ],
        "keywords": ["artificial intelligence"],
        "exact_words": ["ai"],
        "response": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think, learn, and solve problems like humans."
    },
    # Machine Learning
    {
        "patterns": [
            "what is machine learning",
            "what is ml",
            "explain machine learning",
            "explain ml",
            "machine learning meaning",
            "tell me about machine learning",
            "tell me about ml",
            "machine learning"
        ],
        "keywords": ["machine learning"],
        "exact_words": ["ml"],
        "response": "Machine Learning (ML) is a subset of AI that enables systems to automatically learn and improve from experience without being explicitly programmed."
    },
    # Data Science
    {
        "patterns": [
            "what is data science",
            "what is data analysis",
            "explain data science",
            "explain data analysis",
            "data science meaning",
            "data analysis meaning",
            "tell me about data science",
            "tell me about data analysis",
            "data science",
            "data analysis"
        ],
        "keywords": ["data science", "data analysis"],
        "response": "Data Science is an interdisciplinary field that combines statistics, data analysis, and machine learning to analyze raw data and extract meaningful insights."
    },
    # Programming - Python
    {
        "patterns": [
            "what is python",
            "explain python",
            "tell me about python",
            "python meaning",
            "python programming",
            "python language",
            "python"
        ],
        "keywords": ["python"],
        "response": "Python is a high-level, interpreted programming language known for its easy-to-read syntax, versatility, and widespread use in web development, data science, and automation."
    },
    # Programming - Java
    {
        "patterns": [
            "what is java",
            "explain java",
            "tell me about java",
            "java meaning",
            "java programming",
            "java language"
        ],
        "keywords": ["java"],
        "exact_words": ["java"],
        "response": "Java is a popular, class-based, object-oriented programming language designed to run on any device using the Java Virtual Machine (JVM)."
    },
    # Programming - C
    {
        "patterns": [
            "what is c language",
            "explain c language",
            "tell me about c language",
            "c programming",
            "c language"
        ],
        "exact_words": ["c"],
        "response": "C is a powerful, efficient procedural programming language developed in the early 1970s, widely used for system programming, operating systems, and embedded software."
    },
    # Web Dev - HTML
    {
        "patterns": [
            "what is html",
            "explain html",
            "tell me about html",
            "html meaning",
            "html"
        ],
        "keywords": ["html"],
        "response": "HTML (HyperText Markup Language) is the standard markup language used to create the structure and skeleton of web pages."
    },
    # Web Dev - CSS
    {
        "patterns": [
            "what is css",
            "explain css",
            "tell me about css",
            "css meaning",
            "css"
        ],
        "keywords": ["css"],
        "response": "CSS (Cascading Style Sheets) is a stylesheet language used to design and describe the visual presentation and layout of HTML web pages."
    },
    # Web Dev - React
    {
        "patterns": [
            "what is react",
            "what is reactjs",
            "explain react",
            "explain reactjs",
            "tell me about react",
            "reactjs"
        ],
        "keywords": ["react", "reactjs"],
        "response": "React is an open-source JavaScript library developed by Meta for building user interfaces, especially fast single-page applications using reusable components."
    },
    # Web Dev - Node.js
    {
        "patterns": [
            "what is nodejs",
            "what is node js",
            "what is node",
            "explain nodejs",
            "explain node js",
            "tell me about nodejs",
            "node.js",
            "nodejs",
            "node js"
        ],
        "keywords": ["nodejs", "node js"],
        "response": "Node.js is an open-source, cross-platform JavaScript runtime environment that allows developers to execute JavaScript code on the server side."
    },
    # Web Dev - Express.js
    {
        "patterns": [
            "what is expressjs",
            "what is express js",
            "what is express",
            "explain expressjs",
            "explain express",
            "express.js",
            "expressjs",
            "express js"
        ],
        "keywords": ["expressjs", "express js"],
        "response": "Express.js is a minimal and flexible Node.js web application framework that provides robust features for building web applications and REST APIs."
    },
    # Web Dev - Frontend
    {
        "patterns": [
            "what is frontend",
            "explain frontend",
            "tell me about frontend",
            "frontend development",
            "frontend"
        ],
        "keywords": ["frontend"],
        "response": "Frontend development refers to building the visible user interface (UI) and user experience (UX) of a website or app that users interact with directly."
    },
    # Web Dev - Backend
    {
        "patterns": [
            "what is backend",
            "explain backend",
            "tell me about backend",
            "backend development",
            "backend"
        ],
        "keywords": ["backend"],
        "response": "Backend development refers to the server-side logic, databases, APIs, and business rules that operate behind the scenes of an application."
    },
    # Web Dev - Full Stack
    {
        "patterns": [
            "what is full stack",
            "explain full stack",
            "tell me about full stack",
            "full stack development",
            "fullstack",
            "full stack"
        ],
        "keywords": ["full stack", "fullstack"],
        "response": "Full Stack development involves working on both the client-side (frontend) and server-side (backend) portion of web applications."
    },
    # Web Dev - General
    {
        "patterns": [
            "what is web development",
            "explain web development",
            "tell me about web development",
            "web development meaning",
            "web dev"
        ],
        "keywords": ["web development", "web dev"],
        "response": "Web development refers to the tasks and processes involved in building, creating, and maintaining websites and web applications on the internet."
    },
    # APIs - General API
    {
        "patterns": [
            "what is an api",
            "what is api",
            "explain api",
            "tell me about api",
            "api meaning"
        ],
        "keywords": ["api"],
        "exact_words": ["api"],
        "response": "An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other."
    },
    # APIs - JSON
    {
        "patterns": [
            "what is json",
            "explain json",
            "tell me about json",
            "json meaning",
            "json"
        ],
        "keywords": ["json"],
        "response": "JSON (JavaScript Object Notation) is a lightweight, text-based data interchange format that is easy for humans to read and write, and easy for machines to parse."
    },
    # APIs - HTTP
    {
        "patterns": [
            "what is http",
            "explain http",
            "tell me about http",
            "http meaning"
        ],
        "keywords": ["http"],
        "exact_words": ["http"],
        "response": "HTTP (Hypertext Transfer Protocol) is the fundamental protocol used for transferring data and web pages across the World Wide Web."
    },
    # APIs - HTTPS
    {
        "patterns": [
            "what is https",
            "explain https",
            "tell me about https",
            "https meaning",
            "https"
        ],
        "keywords": ["https"],
        "response": "HTTPS (Hypertext Transfer Protocol Secure) is an encrypted version of HTTP that uses SSL/TLS encryption to securely transfer data over the internet."
    },
    # APIs - URL
    {
        "patterns": [
            "what is url",
            "explain url",
            "tell me about url",
            "url meaning"
        ],
        "keywords": ["url"],
        "exact_words": ["url"],
        "response": "A URL (Uniform Resource Locator) is the unique web address used to identify and locate a specific resource or page on the internet."
    },
    # APIs - DNS
    {
        "patterns": [
            "what is dns",
            "explain dns",
            "tell me about dns",
            "dns meaning"
        ],
        "keywords": ["dns"],
        "exact_words": ["dns"],
        "response": "DNS (Domain Name System) translates human-friendly domain names (like google.com) into numerical IP addresses that computers use to connect to servers."
    },
    # Databases - Database / DBMS
    {
        "patterns": [
            "what is database",
            "what is a database",
            "explain database",
            "tell me about database",
            "database meaning",
            "database"
        ],
        "keywords": ["database"],
        "response": "A Database is an organized collection of data stored electronically, managed by a Database Management System (DBMS) for easy retrieval, modification, and storage."
    },
    {
        "patterns": [
            "what is dbms",
            "explain dbms",
            "tell me about dbms",
            "dbms meaning",
            "dbms"
        ],
        "keywords": ["dbms"],
        "response": "A DBMS (Database Management System) is software designed to store, manage, retrieve, and define data in databases efficiently."
    },
    # Databases - SQL
    {
        "patterns": [
            "what is sql",
            "explain sql",
            "tell me about sql",
            "sql meaning"
        ],
        "keywords": ["sql"],
        "exact_words": ["sql"],
        "response": "SQL (Structured Query Language) is the standard domain-specific language used for managing and querying data in relational database management systems."
    },
    # Databases - MySQL
    {
        "patterns": [
            "what is mysql",
            "explain mysql",
            "tell me about mysql",
            "mysql"
        ],
        "keywords": ["mysql"],
        "response": "MySQL is a popular open-source relational database management system (RDBMS) that uses SQL for querying and managing data."
    },
    # Databases - MongoDB
    {
        "patterns": [
            "what is mongodb",
            "explain mongodb",
            "tell me about mongodb",
            "mongodb meaning",
            "mongo db",
            "mongodb"
        ],
        "keywords": ["mongodb", "mongo db"],
        "response": "MongoDB is a popular NoSQL document-oriented database that stores data in flexible, JSON-like document structures."
    },
    # Databases - PostgreSQL
    {
        "patterns": [
            "what is postgresql",
            "what is postgres",
            "explain postgresql",
            "tell me about postgresql",
            "postgresql",
            "postgres"
        ],
        "keywords": ["postgresql", "postgres"],
        "response": "PostgreSQL is a powerful, open-source object-relational database system known for its reliability, feature robustness, and performance."
    },
    # Databases - NoSQL
    {
        "patterns": [
            "what is nosql",
            "explain nosql",
            "tell me about nosql",
            "nosql meaning",
            "nosql"
        ],
        "keywords": ["nosql"],
        "response": "NoSQL (Not Only SQL) databases are non-relational databases designed to store and handle unstructured or semi-structured data at high speeds."
    },
    # Tools - Git
    {
        "patterns": [
            "what is git",
            "explain git",
            "tell me about git",
            "git meaning"
        ],
        "keywords": ["git"],
        "exact_words": ["git"],
        "response": "Git is a distributed version control system designed to track changes in source code during software development and support team collaboration."
    },
    # Tools - GitHub
    {
        "patterns": [
            "what is github",
            "explain github",
            "tell me about github",
            "github"
        ],
        "keywords": ["github"],
        "response": "GitHub is a cloud-based hosting platform for Git repositories that allows developers to host code, collaborate, and manage software projects."
    },
    # Tools - GitLab
    {
        "patterns": [
            "what is gitlab",
            "explain gitlab",
            "tell me about gitlab",
            "gitlab"
        ],
        "keywords": ["gitlab"],
        "response": "GitLab is a DevOps platform providing Git repository hosting, issue tracking, continuous integration (CI/CD), and deployment tools."
    },
    # Tools - VS Code
    {
        "patterns": [
            "what is vs code",
            "what is vscode",
            "explain vs code",
            "explain vscode",
            "tell me about vs code",
            "visual studio code",
            "vscode"
        ],
        "keywords": ["vs code", "vscode", "visual studio code"],
        "response": "Visual Studio Code (VS Code) is a lightweight, extensible source-code editor developed by Microsoft, supporting syntax highlighting, debugging, and extensions."
    },
    # Cloud - Cloud Computing
    {
        "patterns": [
            "what is cloud computing",
            "what is cloud",
            "explain cloud computing",
            "tell me about cloud computing",
            "cloud computing"
        ],
        "keywords": ["cloud computing"],
        "response": "Cloud Computing is the on-demand delivery of computing services—including servers, storage, databases, and software—over the internet."
    },
    # Cloud - AWS
    {
        "patterns": [
            "what is aws",
            "explain aws",
            "tell me about aws",
            "amazon web services",
            "aws"
        ],
        "keywords": ["aws", "amazon web services"],
        "exact_words": ["aws"],
        "response": "AWS (Amazon Web Services) is a comprehensive cloud computing platform provided by Amazon, offering over 200 fully featured services globally."
    },
    # Cloud - Azure
    {
        "patterns": [
            "what is azure",
            "explain azure",
            "tell me about azure",
            "microsoft azure",
            "azure"
        ],
        "keywords": ["azure", "microsoft azure"],
        "response": "Microsoft Azure is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications through Microsoft-managed data centers."
    },
    # Cloud - Google Cloud
    {
        "patterns": [
            "what is google cloud",
            "explain google cloud",
            "tell me about google cloud",
            "gcp",
            "google cloud platform",
            "google cloud"
        ],
        "keywords": ["google cloud", "gcp"],
        "response": "Google Cloud Platform (GCP) is a suite of cloud computing services offered by Google that runs on the same infrastructure Google uses internally."
    },
    # Cloud - Docker
    {
        "patterns": [
            "what is docker",
            "explain docker",
            "tell me about docker",
            "docker container",
            "docker"
        ],
        "keywords": ["docker"],
        "response": "Docker is an open-source platform that enables developers to package applications and their dependencies into standardized units called containers."
    },
    # Cloud - Linux
    {
        "patterns": [
            "what is linux",
            "explain linux",
            "tell me about linux",
            "linux operating system",
            "linux os",
            "linux"
        ],
        "keywords": ["linux"],
        "response": "Linux is an open-source Unix-like operating system kernel widely used in servers, cloud infrastructure, Android devices, and supercomputers."
    },
    # Cybersecurity - Authentication
    {
        "patterns": [
            "what is authentication",
            "explain authentication",
            "tell me about authentication",
            "authentication"
        ],
        "keywords": ["authentication"],
        "response": "Authentication is the security process of verifying the identity of a user, device, or system before granting access."
    },
    # Cybersecurity - JWT
    {
        "patterns": [
            "what is jwt",
            "explain jwt",
            "tell me about jwt",
            "json web token",
            "jwt"
        ],
        "keywords": ["jwt", "json web token"],
        "exact_words": ["jwt"],
        "response": "JWT (JSON Web Token) is a compact, URL-safe standard for securely transmitting information between parties as a JSON object."
    },
    # Cybersecurity - Encryption
    {
        "patterns": [
            "what is encryption",
            "explain encryption",
            "tell me about encryption",
            "encryption"
        ],
        "keywords": ["encryption"],
        "response": "Encryption is the process of encoding information or data into a scrambled format so that only authorized parties with a key can read it."
    },
    # Cybersecurity - Hashing
    {
        "patterns": [
            "what is hashing",
            "explain hashing",
            "tell me about hashing",
            "hashing"
        ],
        "keywords": ["hashing"],
        "response": "Hashing is the transformation of a string of characters into a fixed-length value or key using a mathematical function for data integrity or password storage."
    },
    # Software - Software Development
    {
        "patterns": [
            "what is software development",
            "explain software development",
            "tell me about software development",
            "software engineering",
            "software development"
        ],
        "keywords": ["software development", "software engineering"],
        "response": "Software development is the process of conceiving, designing, programming, testing, and maintaining applications or software components."
    },
    # Software - Software Testing
    {
        "patterns": [
            "what is software testing",
            "explain software testing",
            "tell me about software testing",
            "software testing",
            "testing"
        ],
        "keywords": ["software testing"],
        "response": "Software testing is the process of evaluating and verifying that a software application works as expected and is free of bugs or defects."
    },
    # Software - Debugging
    {
        "patterns": [
            "what is debugging",
            "explain debugging",
            "tell me about debugging",
            "debug",
            "debugging"
        ],
        "keywords": ["debugging", "debug"],
        "response": "Debugging is the process of finding, analyzing, and fixing bugs or errors in software code."
    },
    # Software - Algorithms
    {
        "patterns": [
            "what is an algorithm",
            "what is algorithm",
            "explain algorithm",
            "tell me about algorithms",
            "algorithm",
            "algorithms"
        ],
        "keywords": ["algorithm", "algorithms"],
        "response": "An algorithm is a step-by-step procedure or formula for solving a problem or completing a task in computing."
    },
    # Software - Data Structures
    {
        "patterns": [
            "what is a data structure",
            "what is data structure",
            "explain data structure",
            "explain data structures",
            "data structures",
            "data structure"
        ],
        "keywords": ["data structure", "data structures"],
        "response": "A data structure is a specialized format for organizing, processing, retrieving, and storing data efficiently."
    },
    # General Knowledge - Basic Mathematics
    {
        "patterns": [
            "what is math",
            "what is mathematics",
            "explain math",
            "tell me about math",
            "mathematics"
        ],
        "keywords": ["mathematics"],
        "exact_words": ["math"],
        "response": "Mathematics is the science and study of numbers, quantities, shapes, logic, and patterns."
    },
    # General Knowledge - General Science
    {
        "patterns": [
            "what is science",
            "explain science",
            "tell me about science",
            "general science",
            "science"
        ],
        "keywords": ["science"],
        "response": "Science is a systematic enterprise that builds and organizes knowledge in the form of testable explanations and predictions about the universe."
    },
    # General Knowledge - Earth
    {
        "patterns": [
            "what is earth",
            "tell me about earth",
            "earth planet"
        ],
        "keywords": ["earth planet"],
        "response": "Earth is the third planet from the Sun and the only astronomical object known to harbor life."
    },
    # General Knowledge - General Knowledge
    {
        "patterns": [
            "what is general knowledge",
            "general knowledge",
            "gk"
        ],
        "keywords": ["general knowledge"],
        "response": "General knowledge encompasses culturally valued information about social, historical, scientific, and everyday topics."
    }
]

def get_knowledge_response(normalized_text: str):
    """
    Searches KNOWLEDGE_DATA for matching patterns, keywords, or exact words using word boundaries.
    Returns the response string if matched, otherwise None.
    """
    for entry in KNOWLEDGE_DATA:
        # 1. Check patterns using exact match or regex word boundary match
        for pattern in entry.get("patterns", []):
            clean_pattern = pattern.lower().strip()
            if normalized_text == clean_pattern or re.search(r'\b' + re.escape(clean_pattern) + r'\b', normalized_text):
                return entry["response"]
        
        # 2. Check keywords
        for kw in entry.get("keywords", []):
            if re.search(r'\b' + re.escape(kw.lower()) + r'\b', normalized_text):
                return entry["response"]

        # 3. Check exact words
        for ew in entry.get("exact_words", []):
            if re.search(r'\b' + re.escape(ew.lower()) + r'\b', normalized_text):
                return entry["response"]

    return None
