import requests, os
from dotenv import load_dotenv
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def get_ai_response(prompt):
    url = "https://api-inference.huggingface.co/models/google/flan-t5-large"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}", "Content-Type": "application/json"}
    payload = {"inputs": prompt}
    try:
        res = requests.post(url, headers=headers, json=payload, timeout=15).json()
        if isinstance(res, list) and "generated_text" in res[0]:
            return res[0]["generated_text"]
        elif isinstance(res, dict) and "error" in res:
            return f"⚠️ AI Model Error: {res['error']}"
    except Exception as e:
        return f"⚠️ API Request Error: {e}"
    return "⚠️ Unexpected AI response format."
