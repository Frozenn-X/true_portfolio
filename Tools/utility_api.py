import openai 

from core.settings import CONTENU, CHATGPT_MODEL_ENGINE, CHAT_GPT_KEY, RÔLES, UTILISATEUR

openai.api_key = CHAT_GPT_KEY

def send_request_to_chat_gpt(message, temperature=0.5):
    if not message:
        return 
    return openai.ChatCompletion.create(
        model=CHATGPT_MODEL_ENGINE,
        messages=[{RÔLES: UTILISATEUR, CONTENU: message}],
        temperature=temperature,
        max_tokens=2048, 
    )