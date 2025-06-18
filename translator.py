import requests

def translate_text(text, target_lang="en"):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": target_lang,
        "dt": "t",
        "q": text
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        result = response.json()
        return result[0][0][0]
    except requests.exceptions.RequestException as e:
        print(f"Translation error: {e}")
        return "⚠️ অনুবাদ করতে ব্যর্থ।"
