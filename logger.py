import os
import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "conversation.log")

def log_conversation(user_message: str, bot_response: str) -> None:
    """
    Logs user messages and bot responses with timestamps into logs/conversation.log.
    Creates the logs directory automatically if it does not exist.
    """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
        
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clean_bot_response = bot_response.replace('\n', ' ')
    log_entry = f"[{timestamp}] User: {user_message} | Bot: {clean_bot_response}\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
