import requests
import os
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def get_ai_response(prompt):
    url = "https://api-inference.huggingface.co/models/google/flan-t5-large"
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": prompt}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "error" in result:
            return f"⚠️ AI Model Error: {result['error']}"
        else:
            return "⚠️ Unexpected AI response format."
    except requests.exceptions.RequestException as e:
        return f"⚠️ API Request Error: {str(e)}"
