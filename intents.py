import re

def normalize_input(text: str) -> str:
    """
    Normalizes user input:
    - Converts text to lowercase
    - Strips leading and trailing whitespace
    - Removes punctuation marks
    - Collapses multiple whitespace spaces into a single space
    """
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

GREETING_PATTERNS = [
    "hi",
    "hello",
    "hey",
    "hi there",
    "hello bot",
    "good morning",
    "good afternoon",
    "good evening",
    "greetings",
    "hey there"
]

HELP_PATTERNS = [
    "help",
    "what can you do",
    "how can you help me",
    "what do you know",
    "commands"
]

SMALL_TALK_PATTERNS = {
    "how_are_you": [
        "how are you",
        "how are you doing",
        "how do you do",
        "how is it going",
        "how are things"
    ],
    "identity": [
        "what is your name",
        "who are you",
        "what are you",
        "tell me about yourself",
        "your name"
    ],
    "nice_to_meet": [
        "nice to meet you",
        "pleased to meet you",
        "glad to meet you"
    ],
    "thanks": [
        "thank you",
        "thanks",
        "thank you so much",
        "thanks a lot"
    ],
    "affirmative": [
        "yes",
        "yeah",
        "sure",
        "yep",
        "ok",
        "okay"
    ]
}

ENDING_PATTERNS = [
    "bye",
    "goodbye",
    "exit",
    "quit",
    "see you",
    "thats all",
    "that is all",
    "that's all",
    "bye bye"
]

def match_intent(normalized_text: str):
    """
    Checks if normalized_text matches any intent pattern.
    Returns a tuple of (intent_type, response) or None if no match.
    """
    # 1. Check ENDING patterns first
    for pattern in ENDING_PATTERNS:
        clean_pattern = normalize_input(pattern)
        if normalized_text == clean_pattern or re.search(r'\b' + re.escape(clean_pattern) + r'\b', normalized_text):
            return ("ending", "Goodbye! Have a great day!")

    # 2. Check GREETING patterns
    for pattern in GREETING_PATTERNS:
        clean_pattern = normalize_input(pattern)
        if normalized_text == clean_pattern or re.search(r'\b' + re.escape(clean_pattern) + r'\b', normalized_text):
            return ("greeting", "Hello! How can I help you today?")

    # 3. Check HELP patterns
    for pattern in HELP_PATTERNS:
        clean_pattern = normalize_input(pattern)
        if clean_pattern in normalized_text:
            return ("help", "I am a rule-based chatbot. You can ask me about programming (Python, Java, C++, JS), web development (HTML, CSS, React, MERN, MEAN), APIs, databases, developer tools, cloud, cybersecurity, software engineering, and general knowledge! How can I help you?")

    # 4. Check SMALL TALK patterns
    for category, patterns in SMALL_TALK_PATTERNS.items():
        for pattern in patterns:
            clean_pattern = normalize_input(pattern)
            if normalized_text == clean_pattern or re.search(r'\b' + re.escape(clean_pattern) + r'\b', normalized_text):
                if category == "how_are_you":
                    return ("small_talk", "I'm doing great, thank you for asking! How can I assist you today?")
                elif category == "identity":
                    return ("small_talk", "I am Simple Rule-Based Chatbot, your friendly assistant!")
                elif category == "nice_to_meet":
                    return ("small_talk", "Nice to meet you too! What would you like to know?")
                elif category == "thanks":
                    return ("small_talk", "You're very welcome! Feel free to ask me another question.")
                elif category == "affirmative":
                    return ("small_talk", "Sure! What would you like to know?")

    return None
