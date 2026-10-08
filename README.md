# Simple Rule-Based Chatbot

> **Week 2 Internship Project**  
> A lightweight, beginner-friendly, web-based conversational chatbot powered purely by Python, Flask, and deterministic pattern-matching rules.

---

## 📌 Project Overview

**Simple Rule-Based Chatbot** is a clean, interactive web application developed as part of a Week 2 Internship assignment. Unlike modern AI/LLM chatbots that use machine learning or external APIs, this chatbot operates strictly on predefined conditional logic and pattern matching algorithms.

It offers an intuitive chat interface built with HTML, CSS, and Vanilla JavaScript that connects seamlessly to a Flask backend, allowing users to ask tech and general knowledge questions, engage in small talk, and receive instantaneous rule-based responses.

---

## ✨ Features

- 🎯 **Pure Rule-Based Engine**: Uses string normalization and regular expressions for deterministic pattern matching without machine learning or external AI APIs.
- 💡 **Broad Knowledge Base**: Answers questions across multiple technical and general domains (AI, Machine Learning, Data Science, Web Development, Programming Languages, APIs, Databases, Tools, Cloud, Cybersecurity, Software Engineering, and General Knowledge).
- 🧩 **Comprehensive Tech Stack Answers**: Fully supports detailed questions regarding popular stacks like **MERN** and **MEAN**.
- 💬 **Interactive UI**: Responsive, modern light-themed interface with auto-scrolling chat history and smooth typing indicators.
- 🔄 **Conversation Flow & Continuation**: Keeps conversations alive by asking interactive follow-up questions instead of abrupt endings.
- 📜 **Conversation Logging**: Automatically logs every conversation with timestamps into `logs/conversation.log`.
- 🔒 **Zero Dependencies & No Auth**: Starts directly into the chatbot with no login, signup, database, or API keys required.

---

## 🛠️ Technologies Used

- **Language**: Python 3.x
- **Backend Framework**: Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript (ES6, Fetch API)
- **Logging**: Standard Python File I/O
- **No Database / No LLMs / No External APIs**

---

## 📁 Project Structure

```text
simple-rule-based-chatbot/
│
├── app.py                  # Flask web application & endpoint handlers
├── chatbot.py              # Core rule-based decision logic
├── intents.py              # Pattern matching for greetings, help, small talk & endings
├── knowledge_base.py       # Domain knowledge base pattern rules & answers
├── logger.py               # Utility to log user & bot messages with timestamps
├── templates/
│   └── index.html          # Clean HTML5 chat interface
├── static/
│   ├── style.css           # Modern CSS styling (Light theme & blue accents)
│   └── script.js           # AJAX fetch logic & chat UI management
├── logs/
│   └── conversation.log    # Auto-created log file storing conversation records
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies (Flask)
```

---

## 🧠 How the Rule-Based Chatbot Works

1. **User Input Normalization**:
   When a user types a message (e.g., `"What is Python?"`), the input is converted to lowercase, stripped of leading/trailing whitespace, and cleaned of punctuation.
   
2. **Intent Matching (`intents.py`)**:
   The normalized message is checked against predefined intent categories:
   - **Greeting**: `"hi"`, `"hello"`, `"good morning"`
   - **Help**: `"help"`, `"what can you do"`
   - **Small Talk**: `"how are you"`, `"what is your name"`, `"thank you"`, `"yes/yeah/sure"`
   - **Ending**: `"bye"`, `"goodbye"`, `"quit"`, `"exit"`

3. **Knowledge Base Matching (`knowledge_base.py`)**:
   If no basic intent is matched, the message is evaluated against structured rules containing string patterns, regex word boundaries (`\b`), and keywords.

4. **Fallback Mechanism**:
   If the message matches neither an intent nor a knowledge rule, the chatbot returns a friendly fallback message:  
   `"I'm not sure about that yet. Please try asking me another question."`

5. **Logging**:
   Every message pair is formatted with a timestamp (`YYYY-MM-DD HH:MM:SS`) and saved to `logs/conversation.log`.

---

## 🚀 How to Install and Run

### 1. Prerequisites
Ensure Python 3.8+ is installed on your machine.

### 2. Set Up Virtual Environment (Optional but Recommended)
On Windows (PowerShell / Command Prompt):
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Open in Web Browser
Navigate to:
```text
http://127.0.0.1:5000
```

---

## ❓ Example Questions You Can Ask

- **Greetings & Small Talk**:
  - *"Hello bot!"*
  - *"How are you?"*
  - *"What is your name?"*
  - *"Thank you!"*

- **Web Development & Stacks**:
  - *"What is MERN stack?"*
  - *"Explain MERN"*
  - *"What is HTML?"*
  - *"Tell me about React"*

- **Programming Languages**:
  - *"What is Python?"*
  - *"Explain Java"*
  - *"Tell me about C++"*
  - *"What is JavaScript?"*

- **APIs & Databases**:
  - *"What is a REST API?"*
  - *"What is JSON?"*
  - *"What is SQL?"*
  - *"Explain MongoDB"*

- **Cloud, Tools & Security**:
  - *"What is Git?"*
  - *"What is Docker?"*
  - *"Explain AWS"*
  - *"What is Cybersecurity?"*

- **End Conversation**:
  - *"bye"* or *"goodbye"*

---

## ⚠️ Limitations

- **Strict Pattern Dependent**: Cannot answer queries outside its predefined rules or variations not covered by patterns.
- **No Machine Learning Context**: Does not retain multi-turn context memory or adapt dynamically over time.
- **No Generative AI Capabilities**: Only returns exact rule-based strings.

---

## 🎓 Internship Information

- **Project Title**: Simple Rule-Based Chatbot
- **Project Type**: Internship Project (Week 2)
- **Author**: Internship Developer
- **Status**: Completed & Fully Tested
