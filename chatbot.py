import itertools
from intents import normalize_input, match_intent
from knowledge_base import get_knowledge_response

# Rotating list of friendly continuation messages
CONTINUATION_MESSAGES = [
    "Is there anything else I can help you with?",
    "Would you like to know anything else?",
    "Feel free to ask me another question."
]

_continuation_cycle = itertools.cycle(CONTINUATION_MESSAGES)

def get_bot_response(user_message: str) -> str:
    """
    Main chatbot decision logic:
    1. Normalize user message.
    2. Check intent rules (greeting, help, small talk, ending).
    3. Check knowledge base rules.
    4. Return rule-based response with proper conversation continuation.
    """
    if not user_message or not user_message.strip():
        return "Please type a message so I can help you."

    normalized_text = normalize_input(user_message)

    # Step 1: Check Intent Matching (greeting, help, small talk, ending)
    intent_match = match_intent(normalized_text)
    if intent_match:
        intent_type, response = intent_match
        return response

    # Step 2: Check Knowledge Base
    kb_response = get_knowledge_response(normalized_text)
    if kb_response:
        continuation = next(_continuation_cycle)
        return f"{kb_response}\n\n{continuation}"

    # Step 3: Fallback Response (if no pattern recognized)
    return "I'm not sure about that yet. Please try asking me another question."
